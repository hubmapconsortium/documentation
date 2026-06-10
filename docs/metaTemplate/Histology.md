---
layout: none
title: Metadata Reporting Standards - Histology
spec_name: Histology
version_label: Version 1
doi: 10.35079/HBM788.QPBW.699
published: September 26, 2025
subjects: AB-PAS, H&E, H-DAB, LFB, PAS, SBB, Trichrome
---

# Metadata Reporting Standards

## Histology

The microscopic study of tissue composition and structure, often referred to as microscopic anatomy. It involves examining tissue samples, typically after they've been sectioned, stained, and placed under a microscope.

Published: September 26, 2025

DOI: https://doi.org/10.35079/HBM788.QPBW.699

Subjects: AB-PAS, H&E, H-DAB, LFB, PAS, SBB, Trichrome

## Descriptive Metadata

### Schema

This section mirrors the CEDAR OpenView snapshot shown in the mockup.

- Parent sample ID: unique HuBMAP or SENet identifier for the sample or subsection.
- Lab ID: internal field for site-specific tracking when needed.
- Preparation protocol DOI: DOI for the protocol used to create the specimen or image.
- Dataset type: the specific kind of dataset being produced.
- Analyte class: the biological analyte measured by the assay.

### Deprecated

Fields listed here are deprecated and should not be used for new submissions.

- Tiled image columns
- Tiled image count

[CEDAR OpenView Documentation](#)

[CEDAR Validator](#)

## File Organization

### Definitions

| Field | Description | Regexp / Rules |
| --- | --- | --- |
| `metadata.tsv` | The main metadata file for the submission. | Required |
| `extras/` | Folder for supporting files associated with the dataset. | Directory |
| `raw/` | Folder containing raw data files from the experiment. | Directory |
| `raw/images/` | Folder containing raw image files. | Directory |
| `lab_processed/images/` | Folder containing processed image outputs. | Directory |

### Example

```text
.
├── metadata.tsv
├── extras/
│   ├── contributors.tsv
│   └── microscope_hardware.json
├── raw/
│   └── images/
│       ├── Brightfield_HE_10msec_image_0001.tiff
│       ├── Brightfield_HE_10msec_image_0002.tiff
│       └── Brightfield_HE_10msec_image_0110.tiff
└── lab_processed/
    └── images/
        ├── Histology_13_95.ome.tiff
        ├── Histology_13_95.channels.csv
        └── tissue-boundary.geojson
```

## HuBMAP Datasets

The HuBMAP Data Portal is an open platform to discover, visualize, and download standardized healthy single-cell and spatial tissue data.

[View Histology Datasets](#)

## Citation

Fisher, Hardi, Morgan, Honick, O'Connor, Pillai, Blood, Silverstein, Musen. Histology Dataset Type. v1.0, HuBMAP, 26 Sept 2025. https://doi.org/10.35079/HBM788.QPBW.699

## Reuse

This standard may be reused, expanded, or referenced by external repositories.  
[Include DCWG paper citation here]

## Contributors

Below is the information for the primary contributors to the HuBMAP and SenNet metadata reporting standards. The full list of contributors can be found here [DCWG paper citation].

For questions about this standard, reach out to the individuals listed below, either via the email address listed in the table or via contact information provided on their ORCID profile page.

| Name | Affiliation | Contact | ORCID |
| --- | --- | --- | --- |
| Contributor One | HuBMAP | contributor.one@example.org | https://orcid.org/0000-0000-0000-0001 |
| Contributor Two | SenNet | contributor.two@example.org | https://orcid.org/0000-0000-0000-0002 |
| Contributor Three | HuBMAP | contributor.three@example.org | https://orcid.org/0000-0000-0000-0003 |
