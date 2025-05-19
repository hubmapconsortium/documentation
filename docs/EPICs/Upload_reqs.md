---
layout: default
---

## Minimum Requirements for an EPIC Upload
Like non-EPIC data uploads, EPICs have file requirements that are necessary for successful data submission (Fig 6):
- An _assay metadata_ file titled "metadata.tsv" 
  - A list of currently-supported epics can be found [here](https://docs.hubmapconsortium.org/metadata).
- A _contributors metadata_ file titled "contributors.tsv" 
  - The contributors metadata template can be found [here](https://hubmapconsortium.github.io/ingest-validation-tools/contributors/current/).
- **Note:** The "metadata.tsv" and "contributors.tsv" files should be validated using the [Metadata Spreadsheet Validator](https://metadatavalidator.metadatacenter.org/).
- Data files required by the EPIC's directory schema.
  - A list of currently-supported epics can be found [here](https://docs.hubmapconsortium.org/metadata).
  - Each EPIC dataset should have a corresponding _subdirectory_ containing all the files in the directory schema.
  - Each row of the metadata file should reference one of these subdirectories via the data_path field.

![Required Files EPIC datasets](EPICs-Fig6B.png)

**Figure 6:** Reqired Metadata, Contributor, and Data files (and directories) for EPIC datasets.
