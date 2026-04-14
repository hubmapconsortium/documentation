# Assay Metadata Markdown Generator

This directory contains scripts to fetch, process, and convert HuBMAP assay metadata templates into human-readable Markdown documentation.

## Workflow Overview
1. **Edit assays.txt**
   - List the URLs of the HuBMAP ingest-validation-tools assay metadata schema pages you want to process, one per line. Under each URL, include the intended description of the assay (also on its own line; no line breaks)
   - Example:
     ```
    https://hubmapconsortium.github.io/ingest-validation-tools/iclap/current/
    iCLAP (individual-nucleotide resolution UV-crosslinking and affinity purification) is a specialized...[etc]

    https://hubmapconsortium.github.io/ingest-validation-tools/comet/current/
    COMET is a technique used to measure DNA damage in individual cells...[etc]
     ```

2. **Run the Pipeline**
   - Use the provided script to generate all Markdown documentation in one step:
     ```sh
     python3 generate_all_md.py
     ```
   - This will:
     1. Run `fetchMeta.py` to fetch the associated metadata information from CEDAR and generate JSON files in `metaJSON/`.
     2. Convert each JSON file in `metaJSON/` to a Markdown file in `toMD/` using `json_to_md.py`.

3. **Output**
   - JSON files: `metaJSON/`
   - Markdown files: `toMD/`

   After Generation, processed files are moved to `old/` subdirectories within each folder. (This folder's included in .gitignore)

## Script Descriptions

- **fetchMeta.py**: Fetches and processes metadata templates from the CEDAR API using the Template IDs. Outputs a JSON file for each assay.
- **json_to_md.py**: Converts a single JSON file to a Markdown table. Used by the batch script.
- **generate_all_md.py**: Runs the full pipeline: fetches all templates and generates Markdown for each.

## Requirements
- Python 3
- `requests` library (`pip install requests`)

## Notes
- The URLs used in the assays.txt file can be found [here](https://hubmapconsortium.github.io/ingest-validation-tools/current/). 
- The scripts will create the `metaJSON/` and `toMD/` folders if they do not exist.
- Re-running the Script will add additional rows to each index table, but overwrite the existing assay metadata page file (vs creating a duplicate)

## Example Usage

```sh
python3 generate_all_md.py
```

This will produce Markdown documentation for all specified templates.
