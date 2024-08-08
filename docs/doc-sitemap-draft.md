## External viewers
### HuBMAP Data
- Developers:
  - Programmatic access to data / metadata via APIs or Tools
    - APIs to find metadata / data:
      - <a href="https://smart-api.info/ui/7aaf02b838022d564da776b03f357158">Search API</a>: The HuBMAP Search API is a thin wrapper of the Elasticsearch API.
        - It handles data indexing and reindexing into the backend Elasticsearch.
        - It accepts the search query and passes through to the Elasticsearch with data access security check.
      - <a href="https://smart-api.info/ui/0065e419668f3336a40d1f5ab89c6ba3">Entity API</a>: The Entity API returns information about HuBMAP data entities.
        - Generally, a donor and organ are _required_ in the provenance hierarchy where tissue samples (such as blocks and samples) can be organized based on several different tissue sample types.
    - Tools to get data without going to the Portal
      - Data and metadata structures (Link to Jes W.’s Cohesive [Metadata] Doc stuff?)
      - Examples: docs, commands, (Jupyter notebooks) 
- Other Stakeholders:
  - View / Access / Download data (via the Portal)
  - <a href="https://docs.hubmapconsortium.org/faq">HuBMAP FAQ</a>: Frequently Asked Questions about HuBMAP Data, Tools, and related topics.
  - <a href="https://docs.hubmapconsortium.org/about">About HuBMAP</a>: Policies & Procedures, DUA, Protected Data & Access, Citing HuBMAP Data, Funding & Contact info.
  - **Training Materials:** Biomedical technologies such as single-cell and spatial approaches are not common at all institutions of higher education. Significant barriers towards making effective use of such data include the lack of available training.
    - HuBMAP has created several self-paced training modules to fill this gap. These modules...
    - Focus on introducing HuBMAP, including technologies & assays used by HuBMAP, HuBMAP metadata, and example use cases.
    - Demonstrate how to include HuBMAP data in research projects, graduate student theses, and classroom teaching.
      <details>
      <summary>See <b>Self-paced Training Modules</b></summary>
      <ul>
          <li> <a href="https://expand.iu.edu/browse/sice/cns/courses/hubmap-visible-human-mooc">Visible Human MOOC</a>: An overview of HuBMAP and introduction to data acquisition, analysis, and visualization.</li>
          <li> <a href="https://github.com/hubmapconsortium/hubmap-data-exploration-workshop/blob/main/HuBMAP_scRNAseq_HBM538_PHSC_677_Bridges2_Jupyter_Notebook_version_02.ipynb">Intro to Single-Cell RNA-Seq Data Analysis</a>: Become proficient in single cell RNA-seq data analysis from HuBMAP.</li>
          <li><a href="https://github.com/hubmapconsortium/hubmap-data-exploration-workshop/blob/main/HuBMAP_Gene_Ontology_Enrichment_Analysis_(GOEA)_with_goatools_HBM538_PHSC_677.ipynb">Venn Diagrams for Comparing Marker Genes </a>: Generate Venn & Super Venn Diagrams to compare marker genes.</li>
          <li><a href="https://github.com/hubmapconsortium/hubmap-data-exploration-workshop/blob/main/HuBMAP_String_Database_protein_protein_interaction_networks_version_03_HBM538_PHSC_677.ipynb">Protein-Protein Interaction Networks</a>: Generate these networks from a list of marker genes with Python's stringdb library.</li>
          <li><a href="https://github.com/hubmapconsortium/hubmap-data-exploration-workshop/blob/main/HuBMAP_Gene_Ontology_Enrichment_Analysis_(GOEA)_with_goatools_HBM538_PHSC_677.ipynb">Gene Ontology Enrichment Analysis</a>: Use the Python goatools library for gene ontology enrichment analysis.</li>
    </ul>
   </details>
   
  - <a href="https://hubmapconsortium.org/featured-publications/">HuBMAP Publications</a>: See more than 330 featured publications to learn how HuBMAP tools and data are advancing discovery.

### HuBMAP Tools and documentation links
- HRA Tools:
  - <a href="https://humanatlas.io">Human Reference Atlas (HRA)</a>: a comprehensive, high-resolution, three-dimensional atlas of all the cells in a healthy human body.
    - Watch a short <a href="https://www.youtube.com/watch?v=DDmP_7vDy-o">video introduction</a> or check out the <a href="https://humanatlas.io/release-notes/v2.1">latest release notes</a> for the HRA.
      <details>
      <summary>See additional Tools available from the HRA... </summary>
      <ul>
        <li><a href="https://humanatlas.io/asctb-reporter">(ASCT+B) Reporter</a>: Compare Anatomical Structures, Cell Types, and Biomarker Tables with this visualization tool. Watch a <a href="https://youtu.be/pzUFmDhQEO8">tutorial video</a> for the ASCT+B Reporter.</li>
        <li><a href="https://humanatlas.io/cell-population-graphs">Cell Population Graphs</a>: An interactive tool for exploring and comparing cell populations.</li>
        <li><a href="https://humanatlas.io/registration-user-interface">Registration User Interface (RUI)</a>: Register and annotate organs. Includes an overview of the interface, basic steps for using the RUI, a short video tutorial, and a link to the RUI. Link to the <a href="https://zenodo.org/records/6628366"> RUI SOP</a>.</li>
        <li><a href="https://humanatlas.io/exploration-user-interface">Exploration User Interface (EUI)</a>: Interact with registered organs. Includes an overview of the interface, basic steps for using the EUI, short video tutorials, and a link to the EUI.</li>
        <li><a href="https://humanatlas.io/organ-gallery-in-vr">VR Organ Gallery</a>: Immersive experience for exploring organs. Includes an overview of the Organ Gallery, an opportunity to provide feedback, and documentation. See also the <a href="https://github.com/cns-iu/hra-organ-gallery-in-vr/blob/main/README.md">README</a> for the VR Organ Gallery.</li>
        <li><a href="https://humanatlas.io/millitome">Millitome</a>: 3D-printed tool for organ sectioning. Read an overview of millitomes, see images of 3-D printed millitomes, and browse the latest millitome gallery.</li>
        <li><a href="https://humanatlas.io/api">APIs</a> for querying and interacting with the HRA.</li>
     </ul></details>
- <a href="https://azimuth.hubmapconsortium.org/?_gl=1*w6lgc7*_ga*MjAwNDc0MTM0OC4xNzE0NzUzMTY4*_ga_N77K0HBGRV*MTcyMjQ4NDIwNi4zMzkuMC4xNzIyNDg0MjA2LjAuMC4w">Azimuth</a>: A web application that uses an annotated reference dataset to automate the processing, analysis, and interpretation of new single-cell sequencing experiments.
  - This page provides Query references, a general workflow, FAQ, and tips for Preprocessing, Mapping, and other topics.
- <a href="http://fusion.hubmapconsortium.org/">FUSION</a>: Functional Unit State Identification and Navigation with WSI - An interactive interface to view spatial transcriptomics data integrated with histopathology, driven by AI. This site contains multiple tutorials and other helpful features.
- <a href="https://vitessce.io/">Vitessce</a>: Visual integration tool for exploration of spatial single cell experiments.
  - <a href="https://vitessce.io/docs/">Vitessce Documentation</a>
  - <a href="https://vitessce.io/docs/tutorials/">Vitessce Tutorials</a>
- Intro/primer to using HuBMAP data analysis tools
  - examples
- Reproducing HuBMAP workflows (Y3 effort)
  - Using APIs to get information about workflows
- <a href="https://portal.hubmapconsortium.org/workspaces">HuBMAP (Data Portal) Workspaces</a>: Explore public HuBMAP data and user-provided data using Python and R in a Jupyter Lab environment.
  - <a href="https://portal.hubmapconsortium.org/tutorials/workspaces">Workspaces Tutorials</a>: Learn how to interactively analyze HuBMAP datasets by uploading them in a JupyterLab environment.

### HuBMAP APIs 
- <a href="https://docs.hubmapconsortium.org/apis.html">HuBMAP APIs</a>: Available as RESTful web services, these APIs support data ingest, querying, and delivery of metadata.
- <a href="https://smart-api.info/registry?q=hubmap">Documentation for HuBMAP APIs</a> at Smart APIs. Click the Details button for more information and documentation.
- Links to use-case-specific API usage (e.g. using data and tools) linked to Data and Tools pages.

## Internal viewers
- Internal developers 
  - HuBMAP Application-specific APIs (**Not intended for use by external developers or other external users**):
    - <a href="https://smart-api.info/ui/5a6bea1158d2652743c7a201fdb1c44d">Ingest API</a>: Supports writing data and metadata to HuBMAP, used by both TMCs and the HIVE. Links to the SmartAPI site where this API is registered as well as documentation for the API.
    - <a href="https://github.com/hubmapconsortium/uuid-api">UUID API</a>: Supports donor and tissue sample registration, data submission, and collection of provenance information via the Ingest UI. Links to GitHub documentation for this API.
    - <a href="https://smart-api.info/ui/96e5b5c0b0efeef5b93ea98ac2794837">Ontology (UBKG) API</a>: Accesses an instance of a [neo4j] Unified Biomedical Knowledge Graph (UBKG).
      - This UBKG links infomation from a variety of biomedical vocabulary systems.
      - The HuBMAP UBKG instance includes HuBMAP’s application ontology that represents the HuBMAP operational model.
      - Links to the SmartAPI site where this API is registered as well as documentation for the API.
- Data submitters
  - <a href="https://docs.hubmapconsortium.org/data-submission/">Data Submission Guide</a>: Documents the key steps for TMCs, Assay teams, and others who upload data to the HuBMAP.
  - <a href="https://docs.hubmapconsortium.org/metadata">Metadata/data schemas</a>: HuBMAP metadata documentation and submission specifications.
    -  See the <a href="https://hubmapconsortium.github.io/ingest-validation-tools/">HuBMAP Data Upload Guidelines</a> for the latest assay metadata options and specifications.
  - <a href="https://metadatavalidator.metadatacenter.org/">Metadata Spreadsheet Validator</a>: Use this tool to validate your metadata spreadsheet (template).
    - <a href="https://metadatacenter.github.io/spreadsheet-validator-docs/">Help documentation</a> for the Metadata Spreadsheet Validator.
  - <a href="https://docs.google.com/forms/d/14tBFAfMy82qQGAR1ECIljCJDaHxQUS-o6z0526jpUuQ/edit?ts=662feb8b">HuBMAP Microscope Metadata entry form</a>: Submit Microscopy Metadata in compliance with the NBO-Q metadata model.
    - <a href="https://docs.google.com/spreadsheets/d/1Ju1_mvqTk1B8I8Ot6EKFKZuQbwkJy4NwzVgwoITWWYw/edit?gid=0#gid=0">HuBMAP Microscope Hardware Collection</a>: List of Microscopy Metadata collected to date.
- General Consortium members 
  - <a href="https://hubmapconsortium.org/member-portal/">HuBMAP Member Portal</a>: Find information about how to navigate the consortium, including the calendar, member directory, etc. 
    - SOPs
    - <a href="https://hubmapconsortium.org/working-groups/">Governance</a>: The HuBMAP Steering Committee and Working Groups.
    - <a href="https://drive.google.com/drive/folders/1jbgzo_MpA7lVv9rmmgxP1Zfuegwis31E">HuBMAP Consortium Google Drive</a>: A shared resource.
      - <a href="https://hubmapconsortium.org/guide-doc-management">Document Management Guide</a>: For the HuBMAP Consortium Google Drive.
    - <a href="https://hubmapconsortium.org/hubmap-calendar/">HuBMAP Calendar</a>: A web calendar that combines all shared, internal Consortium events.
      - <a href="https://docs.google.com/document/d/e/2PACX-1vRyir3ozru4TB3SU79b-_psN3BFxr6BsWORnUFP53_jU1vQAAQe1feRSgXTWqHfrLfqo1NgOHNvgS78/pub">Using Google Groups with Google Calendar</a>
    - other Resources
