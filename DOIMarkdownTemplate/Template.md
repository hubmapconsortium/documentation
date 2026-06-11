---
layout:
title:
spec_name:
version_label:
doi:
published:
subjects:
summary:
schema_intro:
deprecated_intro:
schema_doc_href:
validator_href:
datasets_href:
datasets_text:
citation_text:
reuse_text:
contributors_intro:
contributors_note:
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
  - "item"
deprecated_items:
  - Tiled image columns
  - Tiled image count
definitions:
  - field: metadata.tsv
    description: The main metadata file for the submission.
    rules: Required
contributors:
  - name: Contributor One
    affiliation: HuBMAP
    contact: contributor.one@example.org
    orcid: https://orcid.org/0000-0000-0000-0001
---

{% include doi-template/page.html %}
