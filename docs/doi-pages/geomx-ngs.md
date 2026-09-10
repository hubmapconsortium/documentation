---
layout: doi-landing-page
title: Metadata Reporting Standards - GeoMx (NGS)
spec_name: GeoMx Digital Spatial Profiler (DSP) with next-generation sequencing (NGS)
version_label: Version 1
doi: 10.35079/HBM387.GWMM.369
download_href: "https://github.com/hubmapconsortium/ingest-validation-tools/raw/refs/heads/main/docs/geomx-ngs/current/doi-object.zip"
md5_hash: b91eae77a350987e939d4b68aa33204f
published: August 31, 2026
subjects: 
summary: A spatial biology platform that enables non-destructive, high-plex profiling of RNA and protein from user-selected regions of interest (ROIs) within intact tissue sections. For RNA, tiled in situ hybridization probe sets targeting the whole transcriptome are conjugated to photocleavable DNA indexing oligonucleotides; for protein, antibodies specific to 100s of protein targets are similarly conjugated to photocleavable oligo tags. Following ROI selection, UV illumination releases the oligo tags from the selected areas, which are collected and quantified by NGS, enabling whole-transcriptome-scale spatial profiling with higher target coverage and sensitivity than nCounter-based readout. This approach provides spatially resolved, multiplexed molecular profiles from defined tissue regions. <p class="multiAssay"><span class="requiredMark">*</span> This reporting standard requires the inclusion of <a href="https://dx.doi.org/10.35079/HBM674.XVGG.736"> RNAseq (with probes)</a> dataset metadata for completeness. </p>
schema_doc_href: "https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2F11687c2e-1fbe-4405-a73c-e7ce3294042f"
validator_href: "https://metadatavalidator.metadatacenter.org"
datasets_href: "https://portal.hubmapconsortium.org/search/datasets?dataset_type=GeoMx+(NGS)"
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
 │   ├── microscope_hardware.json
 │   └── microscope_settings.json
 ├── raw/
 │   ├── foobar_LabWorksheet.txt
 │   ├── foobar_config.ini
 │   ├── foobar_SeqCodeIndices.csv
 │   ├── foobar_SampleSheet.csv
 │   ├── foobar_whitelist.txt
 │   ├── markers.csv
 │   ├── foobar.pkc
 │   ├── additional_panels_used.csv
 │   ├── custom_probe_set.csv
 │   ├── fastq/
 │   │   └── oligo/
 │   │       └── foobar.fastq.gz
 │   └── images/
 │       └── overlay.{jpeg,tiff}
 └── lab_processed/
     ├── Initial\s{1}Dataset.xlsx
     ├── annotations.xlsx
     ├── dcc/
     │   └── foobar.dcc
     ├── images/
     │   ├── foobar.ome.tiff
     │   ├── foobar.ome-tiff.channels.csv
     │   └── foobar.tissue-boundary.geojson
     └── primary_analysis/
         └── foobar.xlsx

schema_items: 
|-
  | Attribute | Type | Description | Allowable Values |
  |--------|----|--------------|-------------|
  | Parent sample ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier from HuBMAP or SenNet for the sample (such as a block, section, or suspension) used to perform the assay. For instance, in an RNAseq assay, the parent sample would be the suspension, while in imaging assays, it would be the tissue section. If the assay is derived from multiple parent samples, this field should contain a comma-separated list of identifiers. Example: HBM386.ZGKG.235, HBM672.MKPK.442 |  |
  | Lab ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1 |  |
  | Preparation protocol DOI <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The DOI for the protocols.io page that details the assay or the procedures used for sample procurement and preparation. For example, in the case of an imaging assay, the protocol may start with tissue section staining and end with the generation of an OME-TIFF file. The documented protocol should also include any image processing steps involved in producing the final OME-TIFF. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1 |  |
  | Dataset type <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific type of dataset being produced. Example: RNAseq | ```HiFi-Slide``` ```SNARE-seq2``` ```COMET``` ```Visium (no probes)``` ```DESI``` ```Confocal``` ```Stereo-seq``` ```Visium (with probes)``` ```Molecular Cartography``` ```Virtual Histology``` ```DBiT-seq``` ```Seq-Scope``` ```CosMx Transcriptomics``` ```CyCIF``` ```Light Sheet``` ```seqFISH``` ```ATACseq``` ```CosMx Proteomics``` ```Singular Genomics G4X``` ```Visium HD``` ```MERFISH``` ```10X Multiome``` ```4i``` ```PhenoCycler``` ```Second Harmonic Generation (SHG)``` ```Thick section Multiphoton MxIF``` ```CyTOF``` ```Olink``` ```MIBI``` ```Auto-fluorescence``` ```FACS``` ```Xenium``` ```SIMS``` ```Cell DIVE``` ```CODEX``` ```GeoMx (NGS)``` ```MUSIC``` ```Pixel-seqV2``` ```MALDI``` ```2D Imaging Mass Cytometry``` ```Histology``` ```Enhanced Stimulated Raman Spectroscopy (SRS)``` ```DART-FISH``` ```Resolve``` ```RNAseq``` ```LC-MS``` ```nanoSPLITS``` ```GeoMx (nCounter)``` ```RNAseq (with probes)``` ```MS Lipidomics``` ```MPLEx``` |
  | Analyte class <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The analyte class which is the target molecule that the assay is measuring. Example: DNA | ```DNA + RNA``` ```Nucleic acid + protein``` ```Chromatin``` ```RNA + protein``` ```RNA``` ```Metabolite``` ```Unsaturated lipid``` ```Lipid + metabolite``` ```Saturated lipid``` ```Lipid``` ```Protein``` ```Fluorochrome``` ```Collagen``` ```DNA``` ```Peptide``` ```Polysaccharide``` ```Endogenous fluorophore``` |
  | Is targeted? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether a specific molecule or set of molecules is targeted for detection or measurement by the assay. Example: Yes | ```Yes``` ```No``` |
  | Acquisition instrument vendor <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The company that manufactures or supplies the acquisition instrument. An acquisition instrument is a device equipped with signal detection hardware and signal processing software. It captures signals produced by assays, such as variations in light intensity or color, or signals corresponding to molecular mass. If the instrument was custom-built or developed internally, enter "In-House". Example: Illumina | ```BGI Genomics``` ```Cytiva``` ```Thermo Fisher Scientific``` ```Zeiss Microscopy``` ```Complete Genomics``` ```3DHISTECH``` ```GE Healthcare``` ```Leica Microsystems``` ```Akoya Biosciences``` ```NanoString``` ```Element Biosciences``` ```Andor``` ```Huron Digital Pathology``` ```Illumina``` ```Ionpath``` ```In-House``` ```Resolve Biosciences``` ```Singular Genomics``` ```Vizgen``` ```Standard BioTools (Fluidigm)``` ```Sciex``` ```Bruker``` ```Evident Scientific (Olympus)``` ```Keyence``` ```Leica Biosystems``` ```Cytek Biosciences``` ```10x Genomics``` ```Microscopes International``` ```Hamamatsu``` ```Motic``` |
  | Acquisition instrument model <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific model of the acquisition instrument, as manufacturers often offer various versions with differing features or sensitivities. These differences may be relevant to the processing or interpretation of the data. If the instrument was custom-built or developed internally, enter "In-House". If the model is unknown, enter "Unknown". Example: HiSeq 4000 | ```SCN400``` ```STELLARIS 5``` ```BZ-X710``` ```Pannoramic MIDI II Digital Scanner``` ```Not applicable``` ```MoticEasyScan One``` ```EVOS M7000``` ```NovaSeq X``` ```NanoZoomer 2.0-HT``` ```timsTOF Ultra 2``` ```Lightsheet 7``` ```Phenocycler-Fusion 1.0``` ```DNBSEQ-T7``` ```timsTOF Pro``` ```Unknown``` ```AVITI``` ```timsTOF Pro 2``` ```Q Exactive UHMR``` ```Q Exactive``` ```timsTOF SCP``` ```Zyla 4.2 sCMOS``` ```Helios``` ```uScopeHXII-20``` ```Custom: Multiphoton``` ```QTRAP 5500``` ```timsTOF Ultra``` ```BZ-X800``` ```CyTOF 2``` ```G4X Spatial Sequencer``` ```NextSeq 500``` ```NanoZoomer S360``` ```Hyperion Imaging System``` ```NovaSeq X Plus``` ```CyTOF XT``` ```NanoZoomer-SQ``` ```NextSeq 550``` ```Axio Zoom.V16``` ```Digital Spatial Profiler``` ```timsTOF FleX``` ```timsTOF FleX MALDI-2``` ```NanoZoomer S210``` ```BZ-X810``` ```Axio Observer 7``` ```Cytek Northern Lights``` ```IN Cell Analyzer 2200``` ```timsTOF HT``` ```PhenoImager Fusion``` ```DM6 B``` ```Phenocycler-Fusion 2.0``` ```Aperio CS2``` ```Orbitrap Fusion Lumos Tribrid``` ```Resolve Biosciences Molecular Cartography``` ```MALDI timsTOF Flex Prototype``` ```TissueScope LE Slide Scanner``` ```VS200 Slide Scanner``` ```Axio Observer 5``` ```Axio Observer 3``` ```HiSeq 2500``` ```Orbitrap Eclipse Tribrid``` ```Cell DIVE``` ```MERSCOPE``` ```NextSeq 2000``` ```NovaSeq 6000``` ```In-House``` ```HiSeq 4000``` ```solariX``` ```Panoramic 150 Digital Scanner``` ```Aperio AT2``` ```MIBIscope``` ```Biomark HD``` ```NanoZoomer S60``` ```CosMx Spatial Molecular Imager``` ```MERSCOPE Ultra``` ```Axio Scan.Z1``` ```Juno System``` ```Q Exactive HF``` ```Xenium Analyzer``` |
  | Source storage duration value <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time the sample was stored prior to processing it. For assays performed on tissue sections, this refers to how long the tissue section (e.g., slide) was stored before the assay began (e.g., imaging). For assays performed on suspensions, such as sequencing, it refers to how long the suspension was stored before library construction started. Example: 12 |  |
  | Source storage duration unit <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the source storage duration value. Example: hour | ```hour``` ```month``` ```year``` ```day``` ```minute``` |
  | Time since acquisition instrument calibration value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time since the acquisition instrument was last serviced or calibrated. This provides a metric for assessing drift in data capture. Example: 10 |  |
  | Time since acquisition instrument calibration unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the time since acquisition instrument calibration value. Example: month | ```month``` ```year``` ```day``` |
  | Contributors path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The name of the file containing the ORCID IDs for all contributors to this dataset. Example: ./contributors.csv |  |
  | Data path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The top-level directory containing the raw and/or processed data. For a single dataset upload, this might be represented as ".", whereas for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For example, if the data is within a directory named "TEST001-RK", use the syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2", where "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field used solely for data ingestion. Example: ./TEST001-RK |  |
  | Mapped area value <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The mapped area value, which refers to the specific area covered or captured in various assays. For Visium, it is the area of spots covered by tissue within the captured area, excluding the total possible captured area. For GeoMx, it refers to the area of the AOI being captured. In HiFi, it is the summed area of the ROIs in a single flowcell lane. For CosMx and Resolve, it indicates the area of the FOV (also known as ROI) region being captured. For Xenium, it is the total area of the FOV regions (also known as ROI) being captured. For Stereo-Seq, this value represents the number of beads. Example: 42.25 |  |
  | Mapped area unit <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the mapped area value. If mapping area is not specified, this field may be left blank. Example: um^2 | ```mm^2``` ```um^2``` |
  | Slide ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier assigned to each slide, enabling users to determine which tissue sections were processed together on the same slide. It is recommended that data providers prefix the ID with the center name to prevent overlapping values across different centers. Example: VAN0071-PA-1-1_AF |  |
  | Number of fluorescent channels <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The number of distinct fluorescent channels present in the image. Example: 3 |  |
  | Target retrieval incubation temperature <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The incubation temperature required for target retrieval, which is typically 100 degrees Celsius for RNA assays and 80 degrees Celsius for protein assays. Example: 100 |  |
  | Target retrieval incubation time value <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The duration for which a sample is exposed to a target retrieval solution. Example: 15 |  |
  | Target retrieval incubation time unit <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the target retrieval incubation time value. If no incubation time is specified, this field may be left blank. Example: minute | ```minute``` |
  | ProteinaseK concentration | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The concentration of the enzyme Proteinase K within a sample, measured in micrograms per milliliter (ug/ml). Example: 10 |  |
  | ProteinaseK incubation time value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The duration for which a sample is incubated with Proteinase K. Example: 15 |  |
  | ProteinaseK incubation time unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the proteinaseK incubation time value. If no incubation time is specified, this field may be left blank. Example: minute | ```minute``` |
  | ROI label <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The label for the region of interest (ROI). For Resolve and CosMx, this corresponds to the field of view (FOV) label. In the case of Xenium, it refers to the ID of the region containing the analysis. For GeoMx, this information can be located in the "Initial Dataset" spreadsheet, which can be downloaded from within the Data Analysis Suite. Example: Decidua |  |
  | Is ROI segmentation performed? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether ROI (Region of Interest) segmentation was performed on the image. For GeoMx, this refers to the use of segmentation to divide ROIs into AOIs (Areas of Interest). Answer with "Yes" or "No" value. Example: Yes | ```Yes``` ```No``` |
  | ROI segmentation strategy | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The segmentation strategy employed in a GeoMx assay. If an overlay was utilized, ensure that the overlay image is included in the dataset upload. Example: Automated segmentation | ```Manual segmentation``` ```Automated segmentation``` |
  | Anatomical structure label | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The label for the overarching anatomical structure. If the anatomical structure is not applicable or not specified, this field may be left blank. Example: Kidney |  |
  | Anatomical structure ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The ontology ID associated with the anatomical structure, typically represented by an UBERON ID. Example: UBERON:0002113 |  |
  | Targeted entity label <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The label for the targeted entity, indicating the specific cell type(s) or functional tissue unit that was targeted within this Region of Interest (ROI) or Area of Interest (AOI). Example: ROI-001 |  |
  | Targeted entity ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The ontology ID associated with the targeted entity. If no specific entity is targeted, this field may be left blank. Example: CL:0000540 |  |
  | Segment ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier for the area of interest (AOI) within a GeoMx dataset. This ID can be found in the "Initial Dataset" spreadsheet, which can be downloaded from the Data Analysis Suite. Example: 9a828e39-43d8-4051-9bcc-581a520a85d4 |  |
  | Is technical replicate? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether the sequencing reaction was run in replicate. If "Yes," the corresponding FASTQ files in the dataset should be merged for analysis. Example: Yes | ```Yes``` ```No``` |
  | Non global files | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | Specifies a semicolon-separated list of non-global files that are to be included in the dataset. The file paths assume that the files are located in the "TOP/non-global/" directory. For instance, if the file is located at TOP/non-global/lab_processed/images/1-tissue-boundary.geojson, the value for this field would be "./lab_processed/images/1-tissue-boundary.geojson". Once ingested, these files will be copied to their appropriate locations within the respective dataset directory tree. This field is intended for internal HuBMAP processing. Examples for GeoMx and PhenoCycler are provided in the File Locations documentation: https://docs.google.com/document/d/1n2McSs9geA9Eli4QWQaB3c9R3wo5d5U1Xd57DWQfN5Q/edit#heading=h.1u82i4axggee Example: ./lab_processed/images/1-tissue-boundary.geojson |  |
  | Metadata schema ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique string identifier for the metadata specification version, which is easily interpretable by computers for purposes of data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 |  |

definitions: 
|-
  | Pattern | Required? | Description |
  |--|--|--|
  | extras/ | ✓ | Folder for general lab-specific files related to the dataset. |
  | extras/microscope_hardware.json$ | ✓ | [QA/QC] A file generated by the micro-meta app that contains a description of the hardware components of the microscope. Email HuBMAP Consortium Help Desk <help@hubmapconsortium.org> if help is required in generating this document. |
  | extras/microscope_settings.json$ |  | [QA/QC] A file generated by the micro-meta app that contains a description of the settings that were used to acquire the image data. Email HuBMAP Consortium Help Desk <help@hubmapconsortium.org> if help is required in generating this document. |
  | raw/ | ✓ | All raw data files for the experiment. |
  | raw/*_LabWorksheet.txt$ | ✓ | An Excel spreadsheet to refer to in setting up the library. This file documents all of the samples from a single collection plate. Generated by DSP run, prior to sequencing. |
  | raw/*_config.ini$ | ✓ | Needed to generate the DCC file from the fastq file. Contains pipeline processing parameters.  Generated by DSP run, prior to sequencing. |
  | raw/*_SeqCodeIndices.csv$ |  | A file with sample information needed by the Illumina software. Use the contents of the SeqCodeIndices.csv file to create a SampleSheet.csv for input to the Illumina sequencer. (NextSeq 1000/2000 users download a SampleSheet.csv and whitelist.txt instead of SeqCodeIndices.csv.)  Generated by DSP run. |
  | raw/*_SampleSheet.csv$ |  | Used by NextSeq 1000/2000 users, along with whitelist.txt, in place of SeqCodeIndices.csv |
  | raw/*_whitelist.txt$ |  | Used by NextSeq 1000/2000 users, along with SampleSheet.csv, in place of SeqCodeIndices.csv |
  | raw/markers.csv$ |  | A csv file describing any morphology markers used to guide ROI and/or AOI selection [this should be similar in structure to the antibodies file] |
  | raw/*.pkc$ | ✓ | The file listing probe barcode sequence and corresponding gene symbol and, if appropriate, proteins targeted by that probe. This should be consistent for the same probe panel. |
  | raw/additional_panels_used.csv$ |  | If multiple commercial probe panels were used, then the primary probe panel should be selected in the "oligo_probe_panel" metadata field. The additional panels must be included in this file. Each panel record should include: manufacturer, model/name, product code. |
  | raw/custom_probe_set.csv$ |  | This file should contain any custom probes used and must be included if the metadata field "is_custom_probes_used" is "Yes". The file should minimally include: target gene id, probe seq, probe id. The contents of this file are modeled after the 10x Genomics probe set file (see <https://support.10xgenomics.com/spatial-gene-expression-ffpe/probe-sets/probe-set-file-descriptions/probe-set-file-descriptions#probe_set_csv_file>). |
  | raw/fastq/ | ✓ | Raw sequencing files for the experiment |
  | raw/fastq/oligo/ | ✓ | Directory containing fastq files pertaining to oligo sequencing. |
  | raw/fastq/oligo/*.fastq.gz$ | ✓ | This is a gzip version of the fastq file. This file contains the cell barcode and unique molecular identifier (technical). |
  | raw/images/ |  | Directory containing raw image files. This directory should include at least one raw file. |
  | raw/images/overlay.{jpeg,tiff}$ |  | State whether an overlay image was used to guide ROI selection. If an overlay is used, then the overlay details will be provided in the protocols.io protocol. If used, this needs to be uploaded. It is not included in the OME TIFF. This can be a JPEG or TIFF file |
  | lab_processed/ | ✓ | Experiment files that were processed by the lab generating the data. |
  | lab_processed/Initial\s{1}Dataset.xlsx$ | ✓ | [QA/QC] An excel spreadsheet that is downloaded from the GeoMx DSP Data Analysis Suite containing QA/QC metrics based on raw, unprocessed target counts. This file contains one row per AOI/segment and no analyses span AOI. The AOIs included in this file can come from different GeoMx runs and hence span Globus uploads. So care must be taken to make sure the appropriate AOIs are included in the file. |
  | lab_processed/annotations.xlsx$ |  | AOI specific annotations. This might include cell type and anatomical information. |
  | lab_processed/dcc/ | ✓ | DCC files generated from fastq by the Nanostring GeoMx NGS Pipeline. |
  | lab_processed/dcc/*.dcc$ | ✓ | DCC files containing target probe counts, generated from fastq by the Nanostring GeoMx NGS Pipeline. |
  | lab_processed/images/ | ✓ | Processed image files |
  | lab_processed/images/*.ome.tiff$ | ✓ | OME-TIFF files (multichannel, multi-layered) produced by the microscopy experiment. If compressed, must use loss-less compression algorithm. For Visium this stitched file should only include the single capture area relevant to the current dataset. For GeoMx there will be one OME TIFF file per slide, with each slide including multiple AOIs. See the following link for the set of fields that are required in the OME TIFF file XML header. <https://docs.google.com/spreadsheets/d/1YnmdTAA0Z9MKN3OjR3Sca8pz-LNQll91wdQoRPSP6Q4/edit#gid=0> |
  | lab_processed/images/*ome-tiff.channels.csv$ | ✓ | This file provides essential documentation pertaining to each channel of the accommpanying OME TIFF. The file should contain one row per OME TIFF channel. The required fields are detailed <https://docs.google.com/spreadsheets/d/1xEJSb0xn5C5fB3k62pj1CyHNybpt4-YtvUs5SUMS44o/edit#gid=0> |
  | lab_processed/images/*.tissue-boundary.geojson$ |  | [QA/QC] If the boundaries of the tissue have been identified (e.g., by manual efforts), then the boundary geometry can be included as a GeoJSON file named “*.tissue-boundary.geojson”. |
  | lab_processed/primary_analysis/ | ✓ | Primary analysis results |
  | lab_processed/primary_analysis/*.xlsx$ |  | [QA/QC] File containing results from initial processing by GeoMx DSP Data Analysis Suite including optional removal of segments and targets based on QC flags and LOQ and normalization using Q3 normalization. This file will not be available for sites that do not use the GeoMx DSP Data Analysis Suite. |

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
  |Roy Lardenoije|Delft University of Technology, Delft, The Netherlands |  | 0000-0002-9026-7870 |
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
