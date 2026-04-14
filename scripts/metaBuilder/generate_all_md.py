import os
import subprocess
import glob
import threading
import itertools
import sys
import time
import requests
from bs4 import BeautifulSoup
import re

def spinner(msg, stop_event):
    for c in itertools.cycle('⠷⠯⠟⠻⠽⠾'):
        if stop_event.is_set():
            break
        sys.stdout.write(f'\r{msg} {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(msg) + 2) + '\r')

def get_assay_info(assay_url):
    response = requests.get(assay_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. Assay name (try h1 without 'category' class, then fallback)
    h1s = soup.find_all('h1')
    assay_name = None
    for h1 in h1s:
        if 'category' not in (h1.get('class') or []):
            assay_name = h1.text.strip()
            break
    if not assay_name:
        assay_name = soup.title.text.strip() if soup.title else "Unknown"

    # 2. Versions (found between <b> tags within <summary> tags)
    versions = []
    current_version = None
    for summary in soup.find_all('summary'):
        b_tag = summary.find('b')
        if b_tag:
            version = b_tag.text.strip()
            versions.append(version)
            if "use this one" in summary.text.lower():
                current_version = version

    # 3. Metadata schema links
    meta_links = []
    template_ids = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2F'):
            meta_links.append(href)
            # Extract template ID
            tid = href.split('templates%2F')[-1]
            tid = tid.split('?')[0]  # Remove any query params
            template_ids.append(tid)

    return {
        "assay_name": assay_name,
        "versions": versions,
        "current_version": current_version,
        "metadata_schema_links": meta_links,
        "template_ids": template_ids
    }

# --------- MAIN FINALIZATION ---------

# Paths
script_dir = os.path.dirname(__file__)
toMD_dir = os.path.join(script_dir, "toMD")
layout_template_path = os.path.join(script_dir, "pageLayout.md")
output_dir = os.path.abspath(os.path.join(script_dir, "../../docs/assays/metadata/"))
index_md_path = os.path.join(output_dir, "index.md")
new_index_md_path = os.path.join(output_dir, "new-metadata-test.md")
assays_txt_path = os.path.join(script_dir, "assays.txt")
meta_json_dir = os.path.join(script_dir, 'metaJSON')


# Step 1: Process assays.txt as link-description pairs
assay_infos = []
all_template_ids = []
assay_descriptions = {}
with open(assays_txt_path, "r") as f:
    lines = [l.strip() for l in f if l.strip()]
    for i in range(0, len(lines), 2):
        url = lines[i]
        description = lines[i+1] if i+1 < len(lines) else ""
        info = get_assay_info(url)
        assay_infos.append(info)
        print(f"Processed: {info['assay_name']}")
        all_template_ids.extend(info['template_ids'])
        assay_descriptions[info['assay_name']] = description

# Step 2: Call fetchMeta.py with all collected template IDs
if all_template_ids:
    template_id_args = []
    for tid in all_template_ids:
        template_id_args.extend(["--templateID", tid])
    stop_event = threading.Event()
    spin_thread = threading.Thread(target=spinner, args=('Fetching metadata', stop_event))
    spin_thread.start()
    subprocess.run(['python3', 'fetchMeta.py'] + template_id_args, check=True)
    stop_event.set()
    spin_thread.join()
    print('Fetching... done.')
else:
    print("No template IDs found to pass to fetchMeta.py")

# Step 3: Find all JSON files in metaJSON and run json_to_md.py on each
json_files = glob.glob(os.path.join(meta_json_dir, '*.json'))
for json_file in json_files:
    stop_event = threading.Event()
    spin_thread = threading.Thread(target=spinner, args=(f'Converting {os.path.basename(json_file)}', stop_event))
    spin_thread.start()
    subprocess.run(['python3', 'json_to_md.py', json_file], check=True)
    stop_event.set()
    spin_thread.join()

print('All markdown files generated into ./toMD')

# --------- FINAL STEP: Build new markdown file from pageLayout.md ---------

def build_final_md(assay_name, current_version, table_md_path, layout_template_path, output_dir):
    # Read the layout template
    with open(layout_template_path, "r") as f:
        layout = f.read()
    # Read the generated table
    with open(table_md_path, "r") as f:
        table = f.read()
    # Fill in the template
    content = layout.replace("{AssayName}", assay_name)
    content = content.replace("{Version NUMBER (current)}", current_version)
    content = content.replace("{Table Here}", table)
    # Write to the output directory
    out_path = os.path.join(output_dir, f"{assay_name}.md")
    with open(out_path, "w") as f:
        f.write(content)
    print(f"Saved: {out_path}")
    return out_path

def update_index_md(index_md_path, assay_name, description=None):
    # Add a row to the table in index.md for the new assay, keeping alphabetical order
    with open(index_md_path, "r") as f:
        lines = f.readlines()
    # Find all table rows (lines starting with "|", but skip the header and separator)
    table_rows = [(i, line) for i, line in enumerate(lines) if line.strip().startswith("|")]
    header_idx = table_rows[0][0]
    separator_idx = table_rows[1][0]
    data_rows = table_rows[2:]  # actual data rows

    # Prepare the new row
    link = f"[attributes]({assay_name})"
    desc = description or ""
    new_row = f"| {assay_name} | {link} | {desc} |\n"

    # Extract assay names from data rows for sorting
    def get_row_assay_name(row):
        # Assay name is between first and second '|'
        parts = row.split('|')
        return parts[1].strip().lower()

    # Insert the new row into the correct alphabetical position
    inserted = False
    for idx, (line_idx, row) in enumerate(data_rows):
        existing_name = get_row_assay_name(row)
        if assay_name.lower() < existing_name:
            insert_at = line_idx
            lines.insert(insert_at, new_row)
            inserted = True
            break
    if not inserted:
        # If not inserted, append at the end of the table
        last_table_row = table_rows[-1][0]
        lines.insert(last_table_row + 1, new_row)

    with open(index_md_path, "w") as f:
        f.writelines(lines)
    print(f"Updated: {index_md_path}")

# --- NEW: Update new-metadata-test.md in alphabetical order ---
def update_new_index_md(new_index_md_path, assay_name, description=None, schema_url=None):
    """
    Add a row to the table in new-metadata-test.md for the new assay, keeping alphabetical order.
    The row format is:
    | Dataset Type | Description |
    | [AssayName](schema_url) [<img src="info3.png" width="14">](AssayName "Attribute description") | description |
    """
    with open(new_index_md_path, "r") as f:
        lines = f.readlines()
    # Find all table rows (lines starting with '|', but skip the header and separator)
    table_rows = [(i, line) for i, line in enumerate(lines) if line.strip().startswith("|")]
    if len(table_rows) < 2:
        print(f"Table not found in {new_index_md_path}")
        return
    header_idx = table_rows[0][0]
    separator_idx = table_rows[1][0]
    data_rows = table_rows[2:]  # actual data rows

    # Prepare the new row
    # Use schema_url if provided, else just the assay name
    if schema_url:
        assay_link = f"[{assay_name}]({schema_url}) [<img src=\"info3.png\" width=\"14\">]({assay_name} \"Attribute description\")"
    else:
        assay_link = f"{assay_name} [<img src=\"info3.png\" width=\"14\">]({assay_name} \"Attribute description\")"
    desc = description or ""
    new_row = f"| {assay_link} | {desc} |\n"

    # Extract assay names from data rows for sorting
    def get_row_assay_name(row):
        # Assay name is between first and second '|', but may contain markdown links
        parts = row.split('|')
        # Remove markdown link if present
        name = parts[1].strip()
        if name.startswith('['):
            name = name.split(']')[0][1:]
        return name.lower()

    # Insert the new row into the correct alphabetical position
    inserted = False
    for idx, (line_idx, row) in enumerate(data_rows):
        existing_name = get_row_assay_name(row)
        if assay_name.lower() < existing_name:
            insert_at = line_idx
            lines.insert(insert_at, new_row)
            inserted = True
            break
    if not inserted:
        # If not inserted, append at the end of the table
        last_table_row = table_rows[-1][0]
        lines.insert(last_table_row + 1, new_row)

    with open(new_index_md_path, "w") as f:
        f.writelines(lines)
    print(f"Updated: {new_index_md_path}")


assay_version_map = {info['assay_name']: info['current_version'] for info in assay_infos}

# Find all generated markdown tables in toMD
md_tables = glob.glob(os.path.join(toMD_dir, "*.md"))
for table_md_path in md_tables:
    assay_name = os.path.splitext(os.path.basename(table_md_path))[0]
    # Use the actual current_version if available
    current_version = assay_version_map.get(assay_name, "Version 2 (current)")
    out_path = build_final_md(assay_name, current_version, table_md_path, layout_template_path, output_dir)
    # Use the description from assays.txt for both index.md and new-metadata-test.md
    description = assay_descriptions.get(assay_name, "")
    update_index_md(index_md_path, assay_name, description=description)
    update_new_index_md(new_index_md_path, assay_name, description=description)

# After processing, move parsed JSON and Markdown files to /old

# Ensure the /old directories exist
meta_json_old_dir = os.path.join(meta_json_dir, "old")
toMD_old_dir = os.path.join(toMD_dir, "old")
os.makedirs(meta_json_old_dir, exist_ok=True)
os.makedirs(toMD_old_dir, exist_ok=True)

# Move JSON files
for json_file in json_files:
    dest = os.path.join(meta_json_old_dir, os.path.basename(json_file))
    os.rename(json_file, dest)

# Move Markdown files
for md_file in md_tables:
    dest = os.path.join(toMD_old_dir, os.path.basename(md_file))
    os.rename(md_file, dest)