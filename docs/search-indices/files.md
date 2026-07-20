---
layout: page
---
# HuBMAP File Indices

### Last Updated: 2026-07-14

## Overview:
This page describes File Info documents stored in the HuBMAP indices for Files associated with Datasets. These indices are accessible via the [HuBMAP Search API](https://smart-api.info/ui/7aaf02b838022d564da776b03f357158) using the index name `files`.  For example with the search endpoint like:
```
 POST https://search.api.hubmapconsortium.org/v3/files/search
```

## Description: 
Per the standard [Search API](https://smart-api.info/ui/7aaf02b838022d564da776b03f357158) functionality the indices are stored as a pair of [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/index.html) indices consisting of a private/consortium-only index and a public/open-to-all index.  The Search API will automatically direct to the index based on the user authorization.

Each document in the files index contains information about one File entity associated with a HuBMAP Dataset.  The structure of these documents is described below.

Files are stored at the Pittsburgh Supercomputing Center.  A nightly process seaches for changes on the PSC file system and updates ElasticSearch documents with changes.  This keeps the Files indices content no more than one day behind for all files.

## Document elements:

| Document Element     | Description                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `file_uuid`          | The 32-character UUID of the file.                                                                                            |
| `md5_checksum`       | The hexidecimal representation of the MD5 checksum of the file calculated during data ingestion.                              |
| `sha256_checksum`    | The hexidecimal representation of the SHA-256 checksum of the file calculated during data ingestion.                          |
| `size`               | Integer size of the file in bytes.                                                                                            |
| `rel_path`           | The local file system path of the file relative to its Dataset directory, including the file name.                            |
| `file_extension`     | The part of `rel_path` after the final period in the file name, which is after the final directory separator.                 |
| `last_modified_at`   | Operating system modification timestamp of the file in the PSC file system.  The format is an integer representing milliseconds since midnight, Jan 1, 1970 |
| `description`        | Free-text description of this Dataset file.                                                                                   |
| `dataset_uuid`       | The 32-character UUID of the Dataset which is the direct ancestor of this file.                                               |
| `dataset_hubmap_id`  | The HuBMAP Consortium-wide unique identifier of the Dataset which is the direct ancestor of this file.  Randomly generated.   |
| `analyte_class`      | Analytes are the target molecules being measured with the assay. From the metadata of the Dataset which is the direct ancestor of this file. |
| `assay_input_entity` | The entity from which the analyte is being captured, which is used to determine which analysis pipeline to run. From the metadata of the Dataset which is the direct ancestor of this file. |
| `is_data_product`    | Boolean indication if this Dataset file is a data product file.                                                               |
| `is_qa_qc`           | Boolean indication if this Dataset file is a QA/QC report.                                                                    |
| `data_class`         | Class of the Dataset which is the direct ancestor of this file.  One of the values: `Processed Dataset` or `Primary Dataset`. |
| `dataset_type`       | The specific assay type of the Dataset which is the direct ancestor of this file.                                             |
| `dataset_status`     | Status of the Dataset which is the direct ancestor of this file. One of the values: `QA`, `Submitted`, or `Approval` in the private/consortium-only index. `Published` is the only status in the public/open-to-all index. |
| `data_access_level`  | Visibility of the Dataset which is the direct ancestor of this file. One of the values: `public` or `consortium`.             |
| `organs`             | An array of objects described below under `organs` Array Elements, with one for each organ Sample in the Dataset.             |
| `donors`             | An array of objects described below under `donors` Array Elements, with one for each donor of an entry in the organs array.   |

### `organs` Array Elements:

| organs Element | Description                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `uuid`         | The 32-character UUID of a Sample entity whose `specimen_type` is `organ`, which is an ancestor of the Dataset which is the direct ancestor of this file. |
| `code`         | A code for the organ type of the Dataset. For a list of possible codes see the [HuBMAP Ontology/UBKG Organ List](https://ontology.api.hubmapconsortium.org/organs?application_context=HUBMAP). |
| `label`        | The label for the organ, aligned with the `code` of the organ.                                                               |
| `hierarchy`    | HuBMAP does not implement hierarchical concepts at this time, so this will track the `label` value.                          |

### `donors` Array Elements:

| donors Element | Description                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `uuid`         | The 32-character UUID of the a Donor entity which is an ancestor of a Sample included in `organs`.                           |
| `entity_type`  | The normalized entity type, which will always be `Donor` for elements of this array.                                         |

