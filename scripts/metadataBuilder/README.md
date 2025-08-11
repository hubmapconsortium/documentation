# Assay Metadata Markdown Generator

This repository contains scripts to fetch, process, and convert HuBMAP assay metadata templates into human-readable Markdown documentation.

## Workflow Overview

1. **Edit `fetchMeta.py`**
   - Manually add the Template IDs you want to process to the `templateIDs` array at the top of `fetchMeta.py`.
   - **How to find Template IDs:**
     - Go to [HuBMAP ingest-validation-tools schemas](https://hubmapconsortium.github.io/ingest-validation-tools/current)
     - Click the "Metadata Schema" link for the desired assay. This will open a page at [openview.metadatacenter.org](https://openview.metadatacenter.org/).
     - The Template ID is the last part of the URL after `/templates/` (e.g., `df335a89-b470-4c2c-a4c9-e8db7f166d59`).
   - Example:
     ```python
     templateIDs = [
         "c78c882d-ff27-473e-b318-540dc6e8034d", # Olink
         "20f1b25a-49dd-419e-a15d-ec02d396b7f7", # CyCif
         # ...add more as needed
     ]
     ```

2. **Run the Pipeline**
   - Use the provided script to generate all Markdown documentation in one step:
     ```sh
     python3 generate_all_md.py
     ```
   - This will:
     1. Run `fetchMeta.py` to fetch and process all templates in `templateIDs`, saving JSON files to `metaJSON/`.
     2. Convert each JSON file in `metaJSON/` to a Markdown file in `toMD/` using `json_to_md.py`.

3. **Output**
   - JSON files: `metaJSON/`
   - Markdown files: `toMD/`

## Script Descriptions

- **fetchMeta.py**: Fetches and processes metadata templates from the CEDAR API using the Template IDs. Outputs a JSON file for each assay.
- **json_to_md.py**: Converts a single JSON file to a Markdown table. Used by the batch script.
- **generate_all_md.py**: Runs the full pipeline: fetches all templates and generates Markdown for each.

## Requirements
- Python 3
- `requests` library (`pip install requests`)

## Notes
- The `templateIDs` array in `fetchMeta.py` must be manually updated with the Template IDs you wish to process.
- Template IDs can be found from the Metadata Schema links at [https://hubmapconsortium.github.io/ingest-validation-tools/current](https://hubmapconsortium.github.io/ingest-validation-tools/current).
- The scripts will create the `metaJSON/` and `toMD/` folders if they do not exist.

## Example Usage

```sh
python3 generate_all_md.py
```

This will produce Markdown documentation for all specified templates.
