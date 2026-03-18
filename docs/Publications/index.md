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

## 1. Create Publication in Ingest Portal
&nbsp;&nbsp; **a.** Start at the [Ingest Portal](https://ingest.hubmapconsortium.org). <br />
&nbsp;&nbsp; **b.** Select “Publication” in the “Register New: Individual” menu. You can also follow this [link](https://ingest.hubmapconsortium.org/new/publication) to get to that page. 
 ![Selecting Publication upload](Publications1.png) <br />
&nbsp;&nbsp; The "Registering a Publication" dialog will display:
 ![Registering a Publication dialog](Publications2a.png) <br />
&nbsp;&nbsp; **c.** Fill out all required fields and enter as much information as possible into the optional fields. <br />
&nbsp;&nbsp; **Note:** In particular, make sure to select _all_ HuBMAP datasets in the portal that were used in your publication. <br />
&nbsp;&nbsp;&nbsp;&nbsp; This information will be used to automatically infer donors and samples that are part of your publication <br />
&nbsp;&nbsp;&nbsp;&nbsp; and display them on the publication page in addition to the datasets.


