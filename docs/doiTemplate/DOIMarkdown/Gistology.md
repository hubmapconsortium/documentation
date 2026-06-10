---
layout: doi-template
title: Metadata Reporting Standards - Gistology
spec_name: Gistology
version_label: Version 1
doi: 10.35079/HBM788.QPBW.699
published: September 26, 2025
subjects: "AB-PAS, H&E, H-DAB, LFB, PAS, SBB, Trichrome"
summary: The microscopic study of tissue composition and structure, often referred to as microscopic anatomy. It involves examining tissue samples, typically after they've been sectioned, stained, and placed under a microscope.
schema_intro: This section mirrors the CEDAR OpenView snapshot shown in the mockup.
deprecated_intro: Fields listed here are deprecated and should not be used for new submissions.
schema_doc_href: "#"
validator_href: "#"
datasets_href: "#"
datasets_text: The HuBMAP Data Portal is an open platform to discover, visualize, and download standardized healthy single-cell and spatial tissue data.
citation_text: Fisher, Hardi, Morgan, Honick, O'Connor, Pillai, Blood, Silverstein, Musen. Histology Dataset Type. v1.0, HuBMAP, 26 Sept 2025. https://doi.org/10.35079/HBM788.QPBW.699
reuse_text: This standard may be reused, expanded, or referenced by external repositories.  [Include DCWG paper citation here]
contributors_intro: Below is the information for the primary contributors to the HuBMAP and SenNet metadata reporting standards. The full list of contributors can be found here [DCWG paper citation].
contributors_note: For questions about this standard, reach out to the individuals listed below, either via the email address listed in the table or via contact information provided on their ORCID profile page.
example_tree: |-
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
schema_items:
  - "Parent sample ID: unique HuBMAP or SENet identifier for the sample or subsection."
  - "Lab ID: internal field for site-specific tracking when needed."
  - "Preparation protocol DOI: DOI for the protocol used to create the specimen or image."
  - "Dataset type: the specific kind of dataset being produced."
  - "Analyte class: the biological analyte measured by the assay."
deprecated_items:
  - Tiled image columns
  - Tiled image count
definitions:
  - field: metadata.tsv
    description: The main metadata file for the submission.
    rules: Required
  - field: extras/
    description: Folder for supporting files associated with the dataset.
    rules: Directory
  - field: raw/
    description: Folder containing raw data files from the experiment.
    rules: Directory
  - field: raw/images/
    description: Folder containing raw image files.
    rules: Directory
  - field: lab_processed/images/
    description: Folder containing processed image outputs.
    rules: Directory
contributors:
  - name: Contributor One
    affiliation: HuBMAP
    contact: contributor.one@example.org
    orcid: https://orcid.org/0000-0000-0000-0001
  - name: Contributor Two
    affiliation: SenNet
    contact: contributor.two@example.org
    orcid: https://orcid.org/0000-0000-0000-0002
  - name: Contributor Three
    affiliation: HuBMAP
    contact: contributor.three@example.org
    orcid: https://orcid.org/0000-0000-0000-0003
---

{% include doi-template/page.html %}
