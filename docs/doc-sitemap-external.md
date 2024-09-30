---
layout: page
---

# HuBMAP Documentation

## HuBMAP Data

### Developers
Programmatic access to data / metadata via APIs or Tools

#### Search APIs
APIs to find metadata / data:
- <a href="https://smart-api.info/ui/7aaf02b838022d564da776b03f357158">Search API</a>: The HuBMAP Search API is a thin wrapper of the Elasticsearch API.
  - It handles data indexing and reindexing into the backend Elasticsearch.
  - It accepts the search query and passes through to the Elasticsearch with data access security check.
  - <a href="https://docs.hubmapconsortium.org/param-search/">HuBMAP Parameterized Search</a> - An option for a simpler programatic search mechanism.
     - Link to a <a href="https://github.com/hubmapconsortium/search-api/blob/main/examples/Parameter%20Search%20and%20Download%20Tutorial.ipynb">Parameterized Search tutorial</a> on GitHub.
       
 - <a href="https://smart-api.info/ui/0065e419668f3336a40d1f5ab89c6ba3">Entity API</a>: The Entity API returns information about HuBMAP data entities.
   - Generally, a donor and organ are _required_ in the provenance hierarchy where tissue samples (such as blocks and samples) can be organized based on several different tissue sample types.
     
#### Getting Data
Tools to get data without going to the Portal:
- <a href="https://docs.hubmapconsortium.org/assays/metadata/">Metadata Attributes by Dataset Type</a> - A list of available dataset types with links to the valid metadata attributes.
- Link to a <a href="https://github.com/hubmapconsortium/search-api/blob/main/examples/Parameter%20Search%20and%20Download%20Tutorial.ipynb">Parameterized Search tutorial</a> on GitHub.

### Other Stakeholders
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

## HuBMAP Tools
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
     </ul>
     </details>
     
- <a href="https://azimuth.hubmapconsortium.org/?_gl=1*w6lgc7*_ga*MjAwNDc0MTM0OC4xNzE0NzUzMTY4*_ga_N77K0HBGRV*MTcyMjQ4NDIwNi4zMzkuMC4xNzIyNDg0MjA2LjAuMC4w">Azimuth</a>: A web application that automates the processing, analysis, and interpretation of new single-cell sequencing experiments.
  - This page provides Query references, a general workflow, FAQ, and tips for Preprocessing, Mapping, and other topics.
- <a href="http://fusion.hubmapconsortium.org/">FUSION</a>: Functional Unit State Identification and Navigation with WSI - An interactive interface to view spatial transcriptomics data integrated with histopathology, driven by AI. This site contains multiple tutorials and other helpful features.
- <a href="https://snap.stanford.edu/stellar/">STELLAR</a>: A geometric deep learning method for cell type discovery and identification in single-cell datasets.
- <a href="https://vitessce.io/">Vitessce</a>: Visual integration tool for exploration of spatial single cell experiments.
  - <a href="https://vitessce.io/docs/">Vitessce Documentation</a>
  - <a href="https://vitessce.io/docs/tutorials/">Vitessce Tutorials</a>
- <a href="http://hubmap.scs.cmu.edu/documentation/">HuBMAP pipelines</a> and related documentation. Includes pipelines for CODEX, SPRM, Single-cell ATAC-seq, and Single-cell RNA-seq
- <mark>Reproducing HuBMAP workflows (Y3 effort)</mark>- Note, still in development, more details to follow. 
- <mark>Using APIs to get information about workflows</mark>
- <a href="https://portal.hubmapconsortium.org/workspaces">HuBMAP (Data Portal) Workspaces</a>: Explore public HuBMAP data and user-provided data using Python and R in a Jupyter Lab environment.
  - <a href="https://portal.hubmapconsortium.org/tutorials/workspaces">Workspaces Tutorials</a>: Learn how to interactively analyze HuBMAP datasets by uploading them in a JupyterLab environment.
