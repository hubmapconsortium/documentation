---
layout: doi-landing-page
title: Metadata Reporting Standards - Histology
spec_name: Histology
version_label: Version 1
doi: 10.35079/HBM788.QPBW.699
download_href: "https://github.com/hubmapconsortium/ingest-validation-tools/blob/main/docs/histology/current/doi-object.zip"
md5_hash: 02f137a986fe53263587ed4b8101cd2b
published: August 21, 2026
subjects: "AB-PAS, H&E, H-DAB, LFB, PAS, SBB, Trichrome"
summary: The microscopic study of tissue composition and structure, often referred to as microscopic anatomy. It involves examining tissue samples, typically after they've been sectioned, stained, and placed under a microscope.
schema_doc_href: "https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2F907d89c7-6cf4-4ec6-9edd-63cf0441d689"
validator_href: "https://metadatavalidator.metadatacenter.org"
datasets_href: "https://portal.hubmapconsortium.org/search/datasets?dataset_type=Histology"
help_href: /doi-pages-help/
datasets_text: The HuBMAP Data Portal is an open platform to discover, visualize, and download standardized healthy single-cell and spatial tissue data.
citation_text: Fisher SA, Hardi J, Morgan R, Nordgren E, Kant PM, Honick B, Rosario J, O'Connor MJ, Turner ML, DCWG Members, Gehlenborg N, Blood PD, Silverstein JC, Musen MA. 2026. The HuBMAP Framework for Advancing Data FAIRness. submitted. https://doi.org/10.64898/2026.06.01.728946
reuse_text: This standard may be reused, expanded, or referenced by external repositories.
contributors_intro: Below is the information for the individuals who contributed to the HuBMAP and SenNet metadata reporting standards.
contributors_note: For questions about this standard, email <a href="mailto:help@hubmapconsortium.org">HuBMAP Helpdesk</a>. You can alternatively reach out to the individuals listed below, either via the email address listed in the table or via contact information provided on their ORCID profile page.

example_tree: 
|-
  .
  ├── metadata.tsv
  ├── extras/
  │   ├── some_file.tsv
  │   ├── some_file1.tsv
  │   ├── some_file2.tsv
  │   ├── some_file3.tsv
  │   ├── some_file4.tsv
  │   ├── contributors.tsv
  │   └── microscope_hardware.json
  ├── raw/
  │   └── images/
  │       ├── Brightfield_HE_10msec_image_0001.tiff
  │       ├── Brightfield_HE_10msec_image_0002.tiff
  │       ├── Brightfield_HE_10msec_image_0003.tiff
  │       ├── Brightfield_HE_10msec_image_0004.tiff
  │       ├── Brightfield_HE_10msec_image_0005.tiff
  │       ├── Brightfield_HE_10msec_image_0006.tiff
  │       ├── Brightfield_HE_10msec_image_0007.tiff
  │       ├── Brightfield_HE_10msec_image_0008.tiff
  │       ├── Brightfield_HE_10msec_image_0009.tiff
  │       ├── Brightfield_HE_10msec_image_0010.tiff
  │       ├── Brightfield_HE_10msec_image_0010.tiff
  │       ├── Brightfield_HE_10msec_image_0011.tiff
  │       ├── Brightfield_HE_10msec_image_0012.tiff
  │       ├── Brightfield_HE_10msec_image_0013.tiff
  │       ├── Brightfield_HE_10msec_image_0014.tiff
  │       └── Brightfield_HE_10msec_image_0110.tiff
  └── lab_processed/
      └── images/
          ├── Histology_13_95.ome.tiff
          ├── Histology_13_95.channels.csv
          └── tissue-boundary.geojson
          
schema_items: 
|-
  | Attribute | Type | Description | Allowable Values |
  |--------|----|--------------|-------------|
  | Parent sample ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier from HuBMAP or SenNet for the sample (such as a block, section, or suspension) used to perform the assay. For instance, in an RNAseq assay, the parent sample would be the suspension, while in imaging assays, it would be the tissue section. If the assay is derived from multiple parent samples, this field should contain a comma-separated list of identifiers. Example: HBM386.ZGKG.235, HBM672.MKPK.442 |  |
  | Lab ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1 |  |
  | Preparation protocol DOI <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The DOI for the protocols.io page that details the assay or the procedures used for sample procurement and preparation. For example, in the case of an imaging assay, the protocol may start with tissue section staining and end with the generation of an OME-TIFF file. The documented protocol should also include any image processing steps involved in producing the final OME-TIFF. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1 |  |
  | Dataset type <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific type of dataset being produced. Example: RNAseq | ```HiFi-Slide``` ```SNARE-seq2``` ```COMET``` ```Visium (no probes)``` ```DESI``` ```Confocal``` ```Stereo-seq``` ```Visium (with probes)``` ```Molecular Cartography``` ```Virtual Histology``` ```DBiT-seq``` ```Seq-Scope``` ```CosMx Transcriptomics``` ```CyCIF``` ```Light Sheet``` ```iCLAP``` ```seqFISH``` ```ATACseq``` ```CosMx Proteomics``` ```Singular Genomics G4X``` ```Visium HD``` ```MERFISH``` ```10X Multiome``` ```4i``` ```PhenoCycler``` ```Second Harmonic Generation (SHG)``` ```Thick section Multiphoton MxIF``` ```MACSima``` ```CyTOF``` ```Illumina Spatial v0``` ```Olink``` ```MIBI``` ```Auto-fluorescence``` ```FACS``` ```Xenium``` ```SIMS``` ```Cell DIVE``` ```CODEX``` ```GeoMx (NGS)``` ```MUSIC``` ```Pixel-seqV2``` ```MALDI``` ```2D Imaging Mass Cytometry``` ```Histology``` ```Enhanced Stimulated Raman Spectroscopy (SRS)``` ```DART-FISH``` ```Resolve``` ```RNAseq``` ```LC-MS``` ```nanoSPLITS``` ```GeoMx (nCounter)``` ```Raman Imaging``` ```RNAseq (with probes)``` ```MS Lipidomics``` ```STARmap``` ```MPLEx``` |
  | Analyte class <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The analyte class which is the target molecule that the assay is measuring. Example: DNA | ```DNA + RNA``` ```Nucleic acid + protein``` ```Chromatin``` ```Lipid + metabolite + protein``` ```RNA + protein``` ```RNA``` ```Metabolite``` ```Unsaturated lipid``` ```Lipid + metabolite``` ```Saturated lipid``` ```Lipid``` ```Protein``` ```Fluorochrome``` ```Collagen``` ```DNA``` ```Peptide``` ```Polysaccharide``` ```Endogenous fluorophore``` |
  | Is targeted? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether a specific molecule or set of molecules is targeted for detection or measurement by the assay. Example: Yes | ```Yes``` ```No``` |
  | Acquisition instrument vendor <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The company that manufactures or supplies the acquisition instrument. An acquisition instrument is a device equipped with signal detection hardware and signal processing software. It captures signals produced by assays, such as variations in light intensity or color, or signals corresponding to molecular mass. If the instrument was custom-built or developed internally, enter "In-House". Example: Illumina | ```BGI Genomics``` ```Cytiva``` ```Thermo Fisher Scientific``` ```Zeiss Microscopy``` ```Complete Genomics``` ```3DHISTECH``` ```GE Healthcare``` ```Leica Microsystems``` ```Akoya Biosciences``` ```NanoString``` ```Element Biosciences``` ```Andor``` ```Huron Digital Pathology``` ```Illumina``` ```Ionpath``` ```Waters``` ```In-House``` ```Resolve Biosciences``` ```Singular Genomics``` ```Vizgen``` ```Standard BioTools (Fluidigm)``` ```Sciex``` ```Bruker``` ```Evident Scientific (Olympus)``` ```Keyence``` ```Miltenyi Biotec``` ```Leica Biosystems``` ```Revvity``` ```Cytek Biosciences``` ```10x Genomics``` ```Microscopes International``` ```Hamamatsu``` ```Motic``` |
  | Acquisition instrument model <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific model of the acquisition instrument, as manufacturers often offer various versions with differing features or sensitivities. These differences may be relevant to the processing or interpretation of the data. If the instrument was custom-built or developed internally, enter "In-House". If the model is unknown, enter "Unknown". Example: HiSeq 4000 | ```SCN400``` ```STELLARIS 5``` ```BZ-X710``` ```Pannoramic MIDI II Digital Scanner``` ```Not applicable``` ```MoticEasyScan One``` ```EVOS M7000``` ```NovaSeq X``` ```LSM 710 Confocal Microscope``` ```NanoZoomer 2.0-HT``` ```timsTOF Ultra 2``` ```Lightsheet 7``` ```Phenocycler-Fusion 1.0``` ```DNBSEQ-T7``` ```timsTOF Pro``` ```Unknown``` ```AVITI``` ```DMi8``` ```Opera Phenix Plus HCS``` ```timsTOF Pro 2``` ```Q Exactive UHMR``` ```Q Exactive``` ```timsTOF SCP``` ```Zyla 4.2 sCMOS``` ```Helios``` ```uScopeHXII-20``` ```Orbitrap Fusion Tribrid``` ```Custom: Multiphoton``` ```QTRAP 5500``` ```timsTOF Ultra``` ```BZ-X800``` ```CyTOF 2``` ```G4X Spatial Sequencer``` ```NextSeq 500``` ```NanoZoomer S360``` ```Hyperion Imaging System``` ```NovaSeq X Plus``` ```CyTOF XT``` ```NanoZoomer-SQ``` ```NextSeq 550``` ```Axio Zoom.V16``` ```Digital Spatial Profiler``` ```timsTOF FleX``` ```timsTOF FleX MALDI-2``` ```NanoZoomer S210``` ```BZ-X810``` ```Axio Observer 7``` ```Cytek Northern Lights``` ```Opera Phenix HCS``` ```Zeiss LightSheet Z.1``` ```IN Cell Analyzer 2200``` ```timsTOF HT``` ```PhenoImager Fusion``` ```DM6 B``` ```Phenocycler-Fusion 2.0``` ```Aperio CS2``` ```Orbitrap Fusion Lumos Tribrid``` ```Resolve Biosciences Molecular Cartography``` ```MALDI timsTOF Flex Prototype``` ```TissueScope LE Slide Scanner``` ```VS200 Slide Scanner``` ```Axio Observer 5``` ```NanoZoomer 2.0-RS``` ```Axio Observer 3``` ```HiSeq 2500``` ```Orbitrap Eclipse Tribrid``` ```Cell DIVE``` ```MERSCOPE``` ```NextSeq 2000``` ```NovaSeq 6000``` ```In-House``` ```HiSeq 4000``` ```Q Exactive HF-X``` ```solariX``` ```Panoramic 150 Digital Scanner``` ```Aperio AT2``` ```MIBIscope``` ```SYNAPT G2-Si``` ```MACSima System``` ```Biomark HD``` ```NanoZoomer S60``` ```CosMx Spatial Molecular Imager``` ```MERSCOPE Ultra``` ```Axio Scan.Z1``` ```Juno System``` ```Q Exactive HF``` ```Xenium Analyzer``` |
  | Source storage duration value <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time the sample was stored prior to processing it. For assays performed on tissue sections, this refers to how long the tissue section (e.g., slide) was stored before the assay began (e.g., imaging). For assays performed on suspensions, such as sequencing, it refers to how long the suspension was stored before library construction started. Example: 12 |  |
  | Source storage duration unit <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the source storage duration value. Example: hour | ```hour``` ```month``` ```year``` ```day``` ```minute``` |
  | Time since acquisition instrument calibration value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time since the acquisition instrument was last serviced or calibrated. This provides a metric for assessing drift in data capture. Example: 10 |  |
  | Time since acquisition instrument calibration unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the time since acquisition instrument calibration value. Example: month | ```month``` ```year``` ```day``` |
  | Contributors path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The name of the file containing the ORCID IDs for all contributors to this dataset. Example: ./contributors.csv |  |
  | Data path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The top-level directory containing the raw and/or processed data. For a single dataset upload, this might be represented as ".", whereas for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For example, if the data is within a directory named "TEST001-RK", use the syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2", where "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field used solely for data ingestion. Example: ./TEST001-RK |  |
  | Is image preprocessing required? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether image preprocessing is necessary based on the type of acquisition instrument used, such as a microscope or slide scanner. This may involve steps like fusing image tiles to assemble the complete image. Example: Yes | ```Yes``` ```No``` |
  | Stain name <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The name of the chemical stains or dyes used on histology samples to emphasize key features of the tissue and enhance contrast. Example: H&E | ```SBB``` ```Trichrome``` ```PAS``` ```AB-PAS``` ```H&E``` ```Fluorophores``` ```LFB``` ```H-DAB``` |
  | Stain technique | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The staining technique used, which can be categorized into three types: progressive, modified progressive, and regressive. In progressive staining, hematoxylin is applied to the tissue without the use of a differentiator to remove excess dye. In contrast, regressive and modified progressive staining techniques involve the use of a differentiator. Example: Progressive staining | ```Modified progressive staining``` ```Not applicable``` ```Progressive staining``` ```Regressive staining``` |
  | Is batch staining done? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether the slides are stained using a linear batch method or individually. Example: No | ```Yes``` ```No``` |
  | Is staining automated? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether the slide staining process is automated using an instrument. Example: Yes | ```Yes``` ```No``` |
  | Preparation instrument vendor | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The company that manufactures the instrument used to prepare the sample (e.g., for staining or other processing steps) prior to the assay. If the instrument was custom-built or developed internally, enter "In-House". If no sample preparation occurred, enter "Not applicable". Example: 10X Genomics | ```In-House``` ```Leica Biosystems``` ```Not applicable``` ```Thermo Fisher Scientific``` ```Roche Diagnostics``` ```HTX Technologies``` ```10x Genomics``` ```Hamamatsu``` ```Ionpath``` ```Akoya Biosciences``` ```SunChrom``` |
  | Preparation instrument model | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific model of the instrument used for sample preparation, such as staining. Manufacturers may offer multiple models with varying features or sensitivities, which can influence how the sample is processed and how the resulting data is interpreted. If no sample preparation occurred, enter "Not applicable". Example: Chromium X | ```NanoZoomer S210``` ```Not applicable``` ```Sublimator``` ```EVOS M7000``` ```Chromium Controller``` ```Custom``` ```NanoZoomer S360``` ```NanoZoomer S60``` ```Chromium X``` ```AutoStainer XL``` ```Visium CytAssist``` ```SunCollect Sprayer``` ```M3+ Sprayer``` ```Discovery Ultra``` ```ST5020 Multistainer``` ```Chromium iX``` ```Chromium Connect``` ```M5 Sprayer``` ```TM-Sprayer``` |
  | Slide ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier assigned to each slide, enabling users to determine which tissue sections were processed together on the same slide. It is recommended that data providers prefix the ID with the center name to prevent overlapping values across different centers. Example: VAN0071-PA-1-1_AF |  |
  | Tile configuration | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The configuration of tiles used for stitching in the assay process. If no tile configuration is applicable, enter "Not applicable". Example: Row-by-row | ```Not applicable``` ```Row-by-row``` ```Column-by-column``` ```Snake-by-rows``` ```Snake-by-columns``` |
  | Scan direction | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The direction of imaging, which is necessary for the stitching process. Example: Left-and-down | ```Left-and-up``` ```Right-and-up``` ```Not applicable``` ```Left-and-down``` ```Right-and-down``` |
  | Tiled image columns | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The number of columns used in the stitching process of a tiled image, often referred to as the grid size in the x-dimension. Example: 5 |  |
  | Tiled image count | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The total number of raw tiled images captured, which are intended to be stitched together. Example: 75 |  |
  | Intended tile overlap percentage | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The intended percentage of overlap between tiled images. This value serves as the set point, although slight variations may occur during image acquisition due to stage registration. Example: 5 |  |
  | Non global files | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | Specifies a semicolon-separated list of non-global files that are to be included in the dataset. The file paths assume that the files are located in the "TOP/non-global/" directory. For instance, if the file is located at TOP/non-global/lab_processed/images/1-tissue-boundary.geojson, the value for this field would be "./lab_processed/images/1-tissue-boundary.geojson". Once ingested, these files will be copied to their appropriate locations within the respective dataset directory tree. This field is intended for internal HuBMAP processing. Examples for GeoMx and PhenoCycler are provided in the [File Locations documentation](https://docs.google.com/document/d/1n2McSs9geA9Eli4QWQaB3c9R3wo5d5U1Xd57DWQfN5Q/edit#heading=h.1u82i4axggee). Example: ./lab_processed/images/1-tissue-boundary.geojson |  |
  | Metadata schema ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique string identifier for the metadata specification version, which is easily interpretable by computers for purposes of data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 |  |

definitions: 
|-
  | Pattern | Required? | Description |
  |--|--|--|
  | extras/ | ✓ | Folder for general lab-specific files related to the dataset. |
  | extras/microscope_hardware.json | ✓ | [QA/QC] A file generated by the micro-meta app that contains a description of the hardware components of the microscope. Email <a href="mailto:help@hubmapconsortium.org">HuBMAP Consortium Helpdesk</a> if help is required in generating this document. |
  | extras/microscope_settings.json | | [QA/QC] A file generated by the micro-meta app that contains a description of the settings used to acquire the image data. Email <a href="mailto:help@hubmapconsortium.org">HuBMAP Consortium Helpdesk</a> if help is required in generating this document. |
  | raw/ | ✓ | Raw data files for the experiment. |
  | raw/images/ | ✓ | Raw image files. This subdirectory harmonizes with other assays like Visium that include both raw imaging and sequencing data. This directory should include at least one raw file. |
  | raw/images/*.{xml,scn,vsi,ndpi,svs,czi,tiff,qptiff} | ✓ | Raw microscope file for the experiment. |
  | lab_processed/ | ✓ | Experiment files that were processed by the lab generating the data. |
  | lab_processed/images/ | ✓ | Processed image files. |
  | lab_processed/images/*.ome.tiff | ✓ | OME-TIFF files (multichannel, multi-layered) produced by the microscopy experiment. If compressed, must use loss-less compression. Required fields -<https://docs.google.com/spreadsheets/d/1YnmdTAA0Z9MKN3OjR3Sca8pz-LNQll91wdQoRPSP6Q4/edit#gid=0> |
  | lab_processed/images/*ome-tiff.channels.csv | ✓ | Documentation for each channel of the OME-TIFF. One row per channel. Required fields -<https://docs.google.com/spreadsheets/d/1xEJSb0xn5C5fB3k62pj1CyHNybpt4-YtvUs5SUMS44o/edit#gid=0> |
  | lab_processed/images/*.tissue-boundary.geojson | | [QA/QC] GeoJSON file describing manually identified (or otherwise) tissue boundaries. |
  | lab_processed/transformations/ | | Directory containing transformation matrices used to align modalities for multimodal overlays (e.g., MALDI, autofluorescence microscopy, MxIF, histology). |
  | lab_processed/transformations/*.txt | | Transformation matrices for overlaying images from the same tissue section. |
  | lab_processed/probabilities/ | | Directory containing probabilities related to lab-processed data (e.g., Ilastik pixel classification). |
  | lab_processed/probabilities/*.tiff | | [QA/QC] A TIFF file containing pixel probabilities. |
    
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
  |Roy Lardenoije|Delft University of Technology, Delft, The Netherlands |  
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
