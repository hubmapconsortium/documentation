import os
import json
import sys

def json_to_markdown(json_path, md_path=None):
    with open(json_path, 'r') as f:
        data = json.load(f)
    # Use the filename (without extension) as the header
    base = os.path.basename(json_path)
    header = os.path.splitext(base)[0]
    # If the JSON has an 'assayName' field, prefer that for the header
    if isinstance(data, dict) and 'assayName' in data:
        header = data['assayName']
        properties = data.get('properties', [])
    elif isinstance(data, dict) and 'properties' in data:
        properties = data['properties']
    elif isinstance(data, list):
        properties = data
    else:
        raise ValueError('Unrecognized JSON structure')

    md_lines = [f"# {header}", ""]
    md_lines.append("| Attribute Name | Type | Description | Allowable Values | Required |")
    md_lines.append("|---------------|------|-------------|------------------|----------|")
    for prop in properties:
        attr = prop.get('attribute', '')
        typ = prop.get('type', '')
        desc = prop.get('description', '').replace('\n', ' ')
        # Allowable Values: join list or show as string
        val = prop.get('value', '')
        if isinstance(val, list):
            val = ', '.join(f'```{str(v)}```' for v in val)
        elif val is None:
            val = ''
        else:
            val = f'```{val}```' if val else ''
        req = str(prop.get('required', ''))
        md_lines.append(f"| {attr} | {typ} | {desc} | {val} | {req} |")
    md_content = '\n'.join(md_lines)
    if not md_path:
        base = os.path.basename(json_path)
        md_name = os.path.splitext(base)[0] + ".md"
        md_dir = os.path.join(os.path.dirname(json_path), "../toMD")
        md_dir = os.path.abspath(md_dir)
        os.makedirs(md_dir, exist_ok=True)
        md_path = os.path.join(md_dir, md_name)
    with open(md_path, 'w') as f:
        f.write(md_content)
    # print(f"{header} markdown exported to ./toMD")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python json_to_md.py <input_json_file> [output_md_file]")
        sys.exit(1)
    json_file = sys.argv[1]
    md_file = sys.argv[2] if len(sys.argv) > 2 else None
    json_to_markdown(json_file, md_file)
