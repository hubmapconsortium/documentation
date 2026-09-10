---
layout: doi-landing-page
title: Metadata Reporting Standards - SNARE-seq2
spec_name: Single-Nucleus chromatin Accessibility and mRNA Expression sequencing, version 2 (SNARE-seq2) 
version_label: Version 1
doi: 10.35079/HBM346.DFPP.785
download_href: "https://github.com/hubmapconsortium/ingest-validation-tools/raw/refs/heads/main/docs/snareseq2/current/doi-object.zip"
md5_hash: edd039c25ed01c4e4697501a6cf16dc6
published: September 3, 2026
subjects: 
summary: SNARE-seq2 is a multimodal single-nucleus assay that simultaneously profiles chromatin accessibility and gene expression from the same individual nucleus. Permeabilized and fixed nuclei are subjected to in-nucleus tagmentation by Tn5 transposase to capture accessible chromatin regions, followed by capture and reverse transcription of nuclear RNA transcripts, with both libraries carrying the same per-nucleus barcode.  <p class="multiAssay"><span class="requiredMark">*</span> This reporting standard requires the inclusion of <a href="https://dx.doi.org/10.35079/HBM556.VHXG.898">RNAseq</a> and <a href="https://dx.doi.org/10.35079/HBM846.LZCV.363">ATACseq</a> dataset metadata for completeness.</p>
schema_doc_href: "https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fb76e54fe-5352-449b-9188-f250b51fbedc"
validator_href: "https://metadatavalidator.metadatacenter.org"
datasets_href: "https://portal.hubmapconsortium.org/search/datasets?dataset_type=SNARE-seq2"
help_href: /doi-pages-help/
datasets_text: The HuBMAP Data Portal is an open platform to discover, visualize, and download standardized healthy single-cell and spatial tissue data.
citation_text: Fisher SA, Hardi J, Morgan R, Nordgren E, Kant PM, Honick B, Rosario J, O'Connor MJ, Turner ML, DCWG Members, Gehlenborg N, Blood PD, Silverstein JC, Musen MA. 2026. The HuBMAP Framework for Advancing Data FAIRness. submitted. https://doi.org/10.64898/2026.06.01.728946
reuse_text: This standard may be reused, expanded, or referenced by external repositories.
contributors_intro: Below is the information for the individuals who contributed to the HuBMAP and SenNet metadata reporting standards.
contributors_note: For questions about this standard, email <a href="mailto:help@hubmapconsortium.org">HuBMAP Helpdesk</a>. You can alternatively reach out to the individuals listed below, either via the email address listed in the table or via contact information provided on their ORCID profile page.
example_tree: 
|- 
  .
  ├── extras/
  │   └── expected_cell_count.txt
  ├── raw/
  │   └── fastq/
  │       ├── RNA/
  │       │   └── foobar_snareseq2_R.fastq.gz
  │       └── ATAC/
  │           └── foobar_snareseq2_R.fastq.gz
  └── lab_processed/

schema_items: |-
  | Attribute | Type | Description | Allowable Values |
  |------|------|-------------|-------------------|
  | Parent sample ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier from HuBMAP or SenNet for the sample (such as a block, section, or suspension) used to perform the assay. For instance, in an RNAseq assay, the parent sample would be the suspension, while in imaging assays, it would be the tissue section. If the assay is derived from multiple parent samples, this field should contain a comma-separated list of identifiers. Example: HBM386.ZGKG.235, HBM672.MKPK.442 |  |
  | Lab ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1 |  |
  | Preparation protocol DOI <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The DOI for the protocols.io page that details the assay or the procedures used for sample procurement and preparation. For example, in the case of an imaging assay, the protocol may start with tissue section staining and end with the generation of an OME-TIFF file. The documented protocol should also include any image processing steps involved in producing the final OME-TIFF. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1 |  |
  | Dataset type <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific type of dataset being produced. Example: RNAseq | ```HiFi-Slide``` ```SNARE-seq2``` ```COMET``` ```Visium (no probes)``` ```DESI``` ```Confocal``` ```Stereo-seq``` ```Visium (with probes)``` ```Molecular Cartography``` ```DBiT-seq``` ```Seq-Scope``` ```CosMx Transcriptomics``` ```CyCIF``` ```Light Sheet``` ```seqFISH``` ```ATACseq``` ```CosMx Proteomics``` ```Singular Genomics G4X``` ```Visium HD``` ```MERFISH``` ```10X Multiome``` ```4i``` ```PhenoCycler``` ```Second Harmonic Generation (SHG)``` ```Thick section Multiphoton MxIF``` ```CyTOF``` ```Olink``` ```MIBI``` ```Auto-fluorescence``` ```FACS``` ```Xenium``` ```SIMS``` ```Cell DIVE``` ```CODEX``` ```GeoMx (NGS)``` ```MUSIC``` ```Pixel-seqV2``` ```MALDI``` ```2D Imaging Mass Cytometry``` ```Histology``` ```Enhanced Stimulated Raman Spectroscopy (SRS)``` ```DART-FISH``` ```Resolve``` ```RNAseq``` ```LC-MS``` ```nanoSPLITS``` ```GeoMx (nCounter)``` ```RNAseq (with probes)``` ```MS Lipidomics``` ```MPLEx``` |
  | Contributors path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The name of the file containing the ORCID IDs for all contributors to this dataset. Example: ./contributors.csv |  |
  | Data path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The top-level directory containing the raw and/or processed data. For a single dataset upload, this might be represented as ".", whereas for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For example, if the data is within a directory named "TEST001-RK", use the syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2", where "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field used solely for data ingestion. Example: ./TEST001-RK |  |
  | Number of pre-amplification PCR cycles | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The number of PCR cycles performed following the Chromium Controller step and before the suspension is separated and library construction begins. Example: 7 |  |
  | Metadata schema ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique string identifier for the metadata specification version, which is easily interpretable by computers for purposes of data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 |  |

definitions: 
|-
  | Pattern | Required? | Description |
  |--|--|--|
  | extras/ | ✓ | Folder for general lab-specific files related to the dataset. |
  | extras/expected_cell_count.txt$ |  | The expected cell count for the RNA sequencing dataset. This is an optional file that, if present, will be used by the HIVE's RNA sequencing analysis pipeline. With some datasets, knowing the expected cell count has improved the output of the HIVE analysis pipeline. |
  | raw/ | ✓ | All raw data files for the experiment. |
  | raw/fastq/ | ✓ | Raw sequencing files for the experiment. |
  | raw/fastq/RNA/ | ✓ | Directory containing fastq files pertaining to RNAseq sequencing. |
  | raw/fastq/RNA/\*_R\*.fastq.gz$ | ✓ | This is a GZip'd version of the forward and reverse fastq files from RNAseq sequencing (R1 and R2). |
  | raw/fastq/ATAC/ | ✓ | Directory containing fastq files pertaining to ATACseq sequencing. |
  | raw/fastq/ATAC/\*_R\*.fastq.gz$ | ✓ | This is a GZip'd version of the fastq files containing the forward, reverse and barcode reads from ATACseq sequencing (R1, R2 and R3). Further, if the barcodes are in R3 (as with 10X) then the metadata field "barcode reads" would be set to "Read 2 (R2)" and the fastq file named "\*_R2\*.fastq.gz" would be expected. |
  lab_processed/ |  | Experiment files that were processed by the lab generating the data. |

contributors:
 |-
  | Name | Affiliation | Contact | ORCID |
  |------|-------------|---------|--------|
  | Stephen A Fisher | University of Pennsylvania, Philadelphia PA, USA | safisher@upenn.edu | 0000-0001-8034-7685 |
  | Josef Hardi | Stanford University, Stanford, CA, USA | johardi@stanford.edu | 0000-0002-2533-6681 |
  | Richard Morgan | University of Pittsburgh, Pittsburgh, PA, USA | rsm66@pitt.edu | 0009-0003-1800-8545 |
  | Mark A Musen | Stanford University, Stanford, CA, USA | musen@stanford.edu | 0000-0003-3325-793X |
  | Jonathan C Silverstein | University of Pittsburgh, Pittsburgh, PA, USA | j.c.s@pitt.edu | 0000-0002-9252-6039 |
  |Erik Nordgren|University of Pennsylvania, Philadelphia PA, USA||0000-0002-5024-0278 |
  |Peter M Kant|University of Pittsburgh, Pittsburgh, PA, USA; Currently - Otsuka Precision Health, Princeton, NJ, USA||0009-0002-6510-5041 |
  |Brendan John Honick|Pittsburgh Supercomputing Center, Carnegie Mellon University, Pittsburgh, PA, USA||0000-0001-6128-9854 |
  |Martin J O'Connor|Stanford University, Stanford, CA, USA||0000-0002-2256-2421 |
  |Jean G Rosario|University of Pennsylvania, Philadelphia PA, USA||0000-0002-6116-5058 |
  |Nils Gehlenborg|Harvard Medical School, Boston, MA, USA||0000-0003-0327-8297 |
  |Philip D Blood|Pittsburgh Supercomputing Center, Carnegie Mellon University, Pittsburgh, PA, USA||0000-0002-9129-1223 |
  |Kyung Jin Ahn|Children's Hospital of Philadelphia, Philadelphia, PA, USA||0000-0002-4184-482X |
  |Christopher R Anderton|Pacific Northwest National Laboratory, Richland, WA, USA||0000-0002-6170-1033 |
  |Shovik Bandyopadhyay|Children's Hospital of Philadelphia, Philadelphia, PA, USA; Brigham and Women's Hospital, Boston, MA, USA||0000-0003-3919-3914 |
  |Kenneth C Bedi|University of Pennsylvania, Philadelphia PA, USA||0000-0003-3588-9324 |
  |Maigan Brusko|University of Florida, Gainesville, FL, USA||0000-0002-4331-2202 |
  |Martha Campbell-Thompson|University of Florida, Gainesville, FL, USA||0000-0001-6878-1235 |
  |James Carson|The University of Texas at Austin, Austin, TX, USA||0000-0001-9009-5645 |
  |Chase M Carver|Mayo Clinic, Rochester, MN, USA||0000-0003-4002-2418 |
  |Jing Chen|University of Florida, Gainesville, FL, USA||0000-0001-8008-8062 |
  |Anthony M Corbett|University of Rochester Medical Center, Rochester, NY, USA||0000-0001-9545-0853 |
  |Alexandra E Cuaycal|University of Florida, Gainesville, FL, USA||0000-0002-9060-6326 |
  |Penny Cuda|Carnegie Mellon University, Pittsburgh, PA, USA||0009-0002-6547-2650 |
  |Dinh Diep|University of California, San Diego, CA, USA; Currently - Altos Labs, San Diego, CA, USA||0000-0001-6057-4119 |
  |Sergii Domanskyi|The Jackson Laboratory for Genomic Medicine, Farmington, CT, USA||0000-0002-6847-6019 |
  |Sean Donahue|Carnegie Mellon University, Pittsburgh, PA, USA||0000-0002-4072-2046 |
  |Michael P Duffy|University of Pennsylvania, Philadelphia PA, USA||0000-0001-5325-3683 |
  |Michael T Eadon|Indiana University School of Medicine, Indianapolis, IN, USA||0000-0003-3066-2876 |
  |Jean Fan|Johns Hopkins University, Baltimore, MD, USA||0000-0002-0212-5451 |
  |Melissa A Farrow|Vanderbilt University, Nashville, TN, USA||0000-0002-1602-2082 |
  |Kathleen M Fisch|University of California San Diego, La Jolla, CA, USA||0000-0002-0117-7444 |
  |William F Flynn|The Jackson Laboratory for Genomic Medicine, Farmington, CT, USA||0000-0001-6533-0340 |
  |James M Fulcher|Pacific Northwest National Laboratory, Richland, WA, USA||0000-0001-9033-3623 |
  |Soumya Ghose|GE HealthCare, Niskayuna, NY, USA||0000-0002-2730-1482 |
  |Fiona Ginty|GE HealthCare, Niskayuna, NY, USA                    ||0000-0001-6638-683X |
  |Joana P Gonçalves|Delft University of Technology, Delft, The Netherlands||0000-0001-6072-9627 |
  |Yongqun He|University of Michigan, Ann Arbor, MI, USA||0000-0001-9189-9661 |
  |Po Hu|Children's Hospital of Philadelphia, Philadelphia, PA, USA; University of Pennsylvania, Philadelphia, PA, USA||0000-0003-2422-1652 |
  |Sanjay Jain|Washington University School of Medicine, St. Louis, MO, USA||0000-0003-2804-127X |
  |Thomas V Karathanos|Stanford University, Stanford, CA, USA||0000-0003-1754-3872 |
  |Madhurima Kaushal|Washington University School of Medicine||0000-0003-2760-0586 |
  |Angela RS Kruse|Vanderbilt University, Nashville, TN, USA; Currently - The Ohio State University, Columbus, OH, USA||0000-0001-8776-2769 |
  |Yumi Kwon|Pacific Northwest National Laboratory, Richland, WA, USA||0000-0003-0523-6197 |
  |Blue B Lake|University of California San Diego, La Jolla, CA, USA; Currently - Altos Labs, San Diego, CA, USA||0000-0002-8637-9044 |
  |Roy Lardenoije|Delft University of Technology, Delft, The Netherlands | | 0000-0002-9026-7870 |
  |Shin Lin|Emory University, Atlanta, GA, USA||0000-0003-0118-0413 |
  |Yiing Lin|Washington University, St. Louis, MO, USA||0000-0002-0317-7608 |
  |Scott A Lindsay|University of California, San Diego, CA, USA||0000-0002-2929-7755 |
  |Peiran  Lu|Children's Hospital of Philadelphia, Philadelphia, PA, USA; University of Pennsylvania, Philadelphia, PA, USA||0009-0001-5096-3046 |
  |Clayton Mathews|University of Florida, Gainesville, FL, USA||0000-0002-8817-6355 |
  |Elizabeth McDonough|GE HealthCare, Niskayuna, NY, USA||0000-0001-7524-8260 |
  |Ricardo Melo Ferreira|Indiana University School of Medicine, Indianapolis, IN, USA||0000-0003-2063-9744 |
  |Emma M Monte|Stanford University, Stanford, CA, USA||0000-0003-2566-1967 |
  |Kathleen O'Neill|University of Pennsylvania, Philadelphia PA, USA||0000-0003-1980-6840 |
  |Minxing Pang|University of Pennsylvania, Philadelphia PA, USA||0000-0001-5208-5972 |
  |Mana Parast|University of California San Diego, La Jolla, CA, USA||0000-0001-5963-2246 |
  |Liming Pei|Children's Hospital of Philadelphia, Philadelphia, PA, USA; University of Pennsylvania, Philadelphia, PA, USA||0000-0002-1924-0333 |
  |Samuel Peters|University of Minnesota, Minneapolis, MN, USA||0000-0003-1479-8087 |
  |Ajay Pillai|National Institute of Health, Bethesda, MD, USA||0000-0002-9789-7189 |
  |Gloria Pryhuber|University of Rochester Medical Center, Rochester, NY, USA||0000-0002-9185-3994 |
  |Ling Qin|University of Pennsylvania, Philadelphia PA, USA||0000-0002-2582-0078 |
  |Presha Rajbhandari|Columbia University, NYC, NY, USA||0000-0003-2184-7238 |
  |Matthew M Ruffalo|Carnegie Mellon University, Pittsburgh, PA, USA||0000-0003-2222-6169 |
  |Pinaki Sarder|University of Florida, Gainesville, FL, USA||0000-0003-2450-5233 |
  |Diane C Saunders|Ann & Robert H. Lurie Children’s Hospital of Chicago, Chicago, IL, USA; Northwestern University, Chicago, IL, USA||0000-0002-8849-6746 |
  |Kevin Schneider|Buck Institute, Novato, CA, USA||0009-0001-8046-0167 |
  |Lingyan Shi|University of California San Diego, La Jolla, CA, USA||0000-0003-1373-3206 |
  |Santhosh Sivajothi|The Jackson Laboratory for Genomic Medicine, Farmington, CT, USA||0000-0002-8854-4517 |
  |David Smith|Children's Hospital of Philadelphia, Philadelphia, PA, USA||0000-0001-7858-3785 |
  |Jeff M Spraggins|Vanderbilt University, Nashville, TN, USA||0000-0001-9198-5498 |
  |Valentina Stanley|University of California, San Diego, CA, USA||0000-0002-2212-7796 |
  |Kai Tan|Children's Hospital of Philadelphia, Philadelphia, PA, USA; University of Pennsylvania, Philadelphia, PA, USA||0000-0002-9104-5567 |
  |Anusha Thadi|Children's Hospital of Philadelphia, Philadelphia, PA, USA||0000-0002-1271-0398 |
  |Hua Tian|Columbia University Medical Center, NYC, NY, USA||0000-0002-3598-0219 |
  |Morgan L Turner|Harvard Medical School, Boston, MA, USA||0000-0002-1512-9742 |
  |Ioannis S Vlachos|Beth Israel Deaconess Medical Center, Boston, MA, USA; Harvard Cancer Center, Boston, MA, USA; Broad Institute of MIT and Harvard, Boston, MA, USA||0000-0002-8849-808X |
  |Seth Winfree|University of Nebraska Medical Center, Omaha, NE, USA; Currently - QCDx Inc, Farmington, CT, USA|| |
  |Pei-Hsun Wu|Johns Hopkins University, Baltimore, MD, USA||0000-0002-7371-2960 |
  |Kevin J Zemaitis|Pacific Northwest National Laboratory, Richland, WA, USA||0000-0002-3524-9776 |
  |Mowei Zhou|Pacific Northwest National Laboratory, Richland, WA, USA; Currently - Zhejiang University, Hangzhou, Zhejiang 310058, China||0000-0003-3575-3224 |
  |Chenchen Zhu|Department of Genetics, Stanford University, Stanford, CA, USA||0000-0003-2165-9456 |
---

{% include doi-template/page.html %}
