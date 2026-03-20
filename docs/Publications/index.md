---
layout: default
---

# Publication Page Upload Workflow
## Introduction
_What is the purpose of publication pages?_<br>
The purpose of [publication pages](https://portal.hubmapconsortium.org/publications) in the HuBMAP Data Portal is to:
- provide an overview of and showcase HuBMAP publications
- make it easy for members of the community to find datasets, samples, and donors included in HuBMAP publications
- feature exciting data through interactive [Vitessce-based visualizations](https://vitessce.io) in ways not possible in PDF-based publications
  
_Who can contribute to a publication page?_ <br>
- **Any HuBMAP member can submit a publication page for any of their publications that use publicly available data in the HuBMAP Data Portal.**
- Both preprints and published papers can be shared as publication pages.
- **Note:** The HuBMAP HIVE will _not_ be responsible for the creation of publication pages or maintenance of their content beyond regular HuBMAP Data Portal maintenance. 

_What is the process of submitting a publication page?_ <br>
To re-use existing HuBMAP infrastructure and processes, publication pages use a process that is very similar to regular dataset submissions, see details below. 
- Like datasets, a publication page (or “publication dataset”) can be updated at any time by the authors.
- Initially, publication pages will be in “QA” status and only accessible to consortium members.
- Once they have been reviewed by the authors, the HuBMAP HIVE curation team will switch the status to “Published.”

## Prerequisites
1. The Globus organization associated with your Globus user account must be a “Data Provider” group. If you previously submitted data to the HuBMAP Data Portal, that will be the case. If not, please contact the [HuBMAP Helpdesk](mailto:help@hubmapconsortium.org). 
2. Your data needs to be prepared according to the instructions included in the “Upload Files” section of this document. The process of preparing the data for a publication page is the same as preparing any other dataset for upload to the portal. The “assay type” in this case is “publication.” See the [metadata and directory schemas](https://hubmapconsortium.github.io/ingest-validation-tools/publication/) for a publication.

### Contacts
- For all general questions, including communication regarding QA, please contact the [HuBMAP Help Desk](mailto:help@hubmapconsortium.org)
- For questions on Vitessce vignette preparation: [Mark Keller](mailto:mark_keller@hms.harvard.edu)
- For questions on Data Ingestion (ingestion portal, Globus, data provider groups): [Brendan Honick](mailto:help@hubmapconsortium.org,bhonick@andrew.cmu.edu)

## 1. Create Publication - Ingest Portal
&nbsp;&nbsp; a. Start at the [Ingest Portal](https://ingest.hubmapconsortium.org). <br />
&nbsp;&nbsp; b. Select “Publication” in the “Register New: Individual” menu. You can also follow this [link](https://ingest.hubmapconsortium.org/new/publication) to get to that page. 
 <img src="Publications1.png" alt="Selecting Publication upload" width="400"> <br />
&nbsp;&nbsp; The "Registering a Publication" dialog will display:
<details><summary><i>Click here to display &#x25BC; (or hide &#x25B6;) the image below...</i></summary>
 <img src="Publications2a.png" alt="Registering a Publication dialog" width="800"> <br />
</details>
&nbsp;&nbsp; c. Fill out all required fields and enter as much information as possible into the optional fields. <br />
&nbsp;&nbsp; <mark>Note:</mark> In particular, make sure to select _all_ HuBMAP datasets in the portal that were used in your publication. <br />
&nbsp;&nbsp;&nbsp;&nbsp; This information will be used to automatically infer donors and samples that are part of your publication <br />
&nbsp;&nbsp;&nbsp;&nbsp; and display them on the publication page in addition to the datasets. <br /> <br />
&nbsp;&nbsp; d. To add datasets to the Publication, click the "Add+" button under "Sources."
<img src="Publications2b.png" alt="Adding a dataset" width="500"> <br />
&nbsp;&nbsp; e. Search for the datasets you want to add, click on a dataset to select it.

- Important: For wild card searches, add "*" at the beginning and / or end of your keyword string
- You can also select a group (institution)
  
<img src="Publications2c-2.png" alt="Search for datasets" width="700"> <br />
&nbsp;&nbsp; f. The selected dataset is listed under sources. <br />
<img src="Publications2d.png" alt="Search for datasets" width="650"> <br />
&nbsp;&nbsp; g. Alternatively, selecting the BULK option allows you to upload multiple datasets. <br />
<img src="Publications2e.png" alt="Search for datasets"> <br />

  <details><summary><i>Click here to display &#x25BC; (or hide &#x25B6;) the image below...</i></summary>
   <img src="Publications2a-2.png" alt="Saving the Publication" width="800"> 
  </details>

 &nbsp;&nbsp; h. Once complete, click “Save” - The "Success" dialog should display: <br />
 
  <img src="Publications3-2.png" alt="Success dialog"> 

 - <mark>Note the HuBMAP ID - </mark> This will allow you to locate your Publication when the Success Dialog is not present. 
 - The steps above create...
   - A HuBMAP record of your Publication
   - A Globus directory where everything associated with the Publication will be stored
 - If no changes are needed, you can click DONE on the "Success" dialog.

## 2. Navigate to Your Publication
 - Click the link for the Publication's HuBMAP ID shown in the dialog above.
   - OR, in the main Ingest Portal search, enter the Publication's HuBMAP ID and click SEARCH
 - This will open the "Publication Information" dialog, where you can update the descripton or other information.
   
 <img src="Publications3-3.png" alt="Top of Publication information dialog" width="800"> <br />

 - From this dialog, click the link <img src="Link-icon1.png" alt="Link icon" width="17"> to the data repository to add or modify data files.

## 3. Prepare Your Files for Upload
Prepare the data for your publication. <br />
This should include any supplementary data files and other information that you want to share with the community. 

To prepare your data for upload, organize it according to the “publication” directory schema. 
Use the [ingest validation tools](https://github.com/hubmapconsortium/ingest-validation-tools#for-data-submitters-and-curators) to confirm that your _directory structure_ and _metadata files_ conform to the requirements of the publication assay type once you have assembled your dataset. 

### Directory structure:
- [**metadata.tsv**](https://gist.github.com/keller-mark/45535076f55bf06f8b22006b7dfe61bb#file-metadata-tsv) - Schema depends on the assay type, use the schema for the [“publication” assay](https://hubmapconsortium.github.io/ingest-validation-tools/publication/) type. 
- **extras/**
  - [**contributors.tsv**](https://hubmapconsortium.github.io/ingest-validation-tools/contributors/current/)
    - **Note:** The _contributors.tsv_ file may not accept certain special characters, such as _ö_.
    - ORCIDs may not be provided by all authors (and may not be required). One option - omit that author on the publication page. 
- **vignettes/** - Follow instructions in the [tutorial](https://github.com/vitessce/vitessce-python-tutorial) to construct your visualizations using Python and Jupyter notebooks.
- <mark>**Note:** </mark>Vignettes are not required!
  - **vignette_01/**
    - [**description.md**](https://gist.githubusercontent.com/keller-mark/45535076f55bf06f8b22006b7dfe61bb/raw/d0cf00b54d8c1d3332238629dbc1b4450ac1fe30/description.md) 
  - **vignette_02/**
    - **description.md**
    - **vitessce.json**
  - **vignette_03/**
    - **description.md** - Multiple Vitessce configurations can be added!
    - **vitessce.json**
- **data/** - All supplementary data for your paper and everything else that you want to share goes here.
  - Ensure that everything referenced by your Vitessce visualizations is in the data directory.

#### Directory Structure Minimum Requirements:
- A directory including **metadata.tsv, vignettes/, data/,** and **extras/** at the top level (no enclosing directory).
- These directories are _required_ but can be empty.

### 3.1 Vignettes
Vignettes are optional features specified using Markdown files named "description.md." <br />
You can share additional documentation, links to external resources, or one or more visualizations of key datasets in the form of “vignettes”. <br />
“Vignettes” will be automatically embedded in the page for your publication. 

Links to additional collections or other resources can be included in the "description.md" file, using standard markdown link formatting i.e. 
- "[link name in square brackets] (https://link-address-in-parentheses.example.com)".
- Please follow the above directory structure for "vignette_01/," and include a "description.md" file.
- The vitessce.json file is not required, as Vitessce visualizations are not required to display this markdown information.

You may also add externally-hosted iframes to the "description.md" to use an embeddable visualization that does not use Vitessce. 
- These iframes can be provided in the "description.md" file.
- Servers hosting the visualization must be configured to allow external embedding of the iframe via [Content Security Policy headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors).

One or more visualizations of key datasets will automatically be embedded in the page for your publication, <br />
if you follow the instructions in the [Vitessce tutorial](https://github.com/vitessce/vitessce-python-tutorial). 
- An example can be viewed for [this publication](https://portal.hubmapconsortium.org/browse/publication/2ced91fd6d543e79af90313e52ada57d). 
- The Globus directory for the above publication can be viewed [here](https://app.globus.org/file-manager?origin_id=af603d86-eab9-4eec-bb1d-9d26556741bb&origin_path=%2F2ced91fd6d543e79af90313e52ada57d%2F) (requires Globus login).

