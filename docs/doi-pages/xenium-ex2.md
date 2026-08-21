---
layout: doi-landing-page
title: Metadata Reporting Standards - Xenium
spec_name: Xenium
version_label: Version 1
doi: 10.35079/HBM788.QPBW.699
published: August 18, 2026
subjects: <a href="https://github.com/hubmapconsortium/ingest-validation-tools/blob/main/docs/xenium/current/doi-object.zip"> Download</a>
summary: Xenium (10x Genomics) is a high-resolution, imaging-based in situ spatial transcriptomics platform that maps the expression of targeted RNA panels within intact tissue sections at single-cell and subcellular resolution. This assay can identify the location of target transcripts within the tissue, providing a single cell resolution map of expression patterns of all genes that are included in the selected probe panel and generating a single-cell-resolution expression map of all profiled genes.
schema_doc_href: "https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2F907d89c7-6cf4-4ec6-9edd-63cf0441d689"
validator_href: "https://metadatavalidator.metadatacenter.org"
datasets_href: "https://portal.hubmapconsortium.org/search/datasets?dataset_type=Xenium"
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
  │   ├── microscope_hardware.json$
  │   └── microscope_settings.json$
  ├── raw/
  │   ├── markers.csv$
  │   ├── additional_panels_used.csv$
  │   ├── custom_probe_set.csv$
  │   ├── custom_probe_set.bed$
  │   ├── transcript_locations.csv$
  │   ├── custom_gene_list.csv$
  │   ├── probes.csv$
  │   ├── gene_panel.json$
  │   ├── protein_panel.json$
  │   └── images/
  │       └── overlay.{jpeg,tif,tiff}$
  └── lab_processed/
      ├── images/
      │   ├── *.ome.tiff$
      │   ├── *ome-tiff.channels.csv$
      │   └── *tissue-boundary.geojson$
      └── xenium_bundle/
          ├── cell_feature_matrix.h5$
          ├── experiment.xenium$
          ├── nucleus_boundaries.parquet$
          ├── cell_boundaries.parquet$
          ├── transcripts.parquet$
          ├── cells.parquet$
          ├── morphology_mip.ome.tif$
          ├── morphology_focus.ome.tif$
          ├── transcripts.zarr.zip$
          ├── cells.zarr.zip$
          ├── cell_feature_matrix.zarr.zip$
          └── morphology_focus/
              ├── morphology_focus_0000.ome.tif$
              ├── morphology_focus_0001.ome.tif$
              ├── morphology_focus_0002.ome.tif$
              └── morphology_focus_0003.ome.tif$
          
schema_items: 
|-
  | Attribute | Type | Description | Allowable Values |
  |--------|----|--------------|-------------|
  | Parent sample ID<span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier from HuBMAP or SenNet for the sample (such as a block, section, or suspension) used to perform the assay. For instance, in an RNAseq assay, the parent sample would be the suspension, while in imaging assays, it would be the tissue section. If the assay is derived from multiple parent samples, this field should contain a comma-separated list of identifiers. Example: HBM386.ZGKG.235, HBM672.MKPK.442 |  |
  | Lab ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1 |  |
  | Preparation protocol DOI<span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The DOI for the protocols.io page that details the assay or the procedures used for sample procurement and preparation. For example, in the case of an imaging assay, the protocol may start with tissue section staining and end with the generation of an OME-TIFF file. The documented protocol should also include any image processing steps involved in producing the final OME-TIFF. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1 |  |
  | Dataset type<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific type of dataset being produced. Example: RNAseq | HiFi-Slide, SNARE-seq2, COMET, Visium (no probes), DESI, Confocal, Stereo-seq, Visium (with probes), Molecular Cartography, Virtual Histology, DBiT-seq, Seq-Scope, CosMx Transcriptomics, CyCIF, Light Sheet, iCLAP, seqFISH, ATACseq, CosMx Proteomics, Singular Genomics G4X, Visium HD, MERFISH, 10X Multiome, 4i, PhenoCycler, Second Harmonic Generation (SHG), Thick section Multiphoton MxIF, MACSima, CyTOF, Olink, MIBI, Auto-fluorescence, FACS, Xenium, DNA Methylation, SIMS, Cell DIVE, CODEX, GeoMx (NGS), MUSIC, Pixel-seqV2, MALDI, 2D Imaging Mass Cytometry, Histology, Enhanced Stimulated Raman Spectroscopy (SRS), Illumina Spatial ver0, DART-FISH, Resolve, RNAseq, LC-MS, nanoSPLITS, GeoMx (nCounter), Raman Imaging, RNAseq (with probes), MS Lipidomics, STARmap, MPLEx |
  | Analyte class<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The analyte class which is the target molecule that the assay is measuring. Example: DNA | DNA + RNA, Nucleic acid + protein, Chromatin, Lipid + metabolite + protein, RNA + protein, RNA, Metabolite, Unsaturated lipid, Lipid + metabolite, Saturated lipid, Lipid, Protein, Fluorochrome, Collagen, DNA, Peptide, Polysaccharide, Endogenous fluorophore |
  | Is targeted?<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether a specific molecule or set of molecules is targeted for detection or measurement by the assay. Example: Yes |  ```Yes ```,  ```No ``` |
  | Acquisition instrument vendor<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The company that manufactures or supplies the acquisition instrument. An acquisition instrument is a device equipped with signal detection hardware and signal processing software. It captures signals produced by assays, such as variations in light intensity or color, or signals corresponding to molecular mass. If the instrument was custom-built or developed internally, enter "In-House". Example: Illumina | BGI Genomics, Cytiva, Thermo Fisher Scientific, Zeiss Microscopy, Complete Genomics, 3DHISTECH, GE Healthcare, Leica Microsystems, Akoya Biosciences, NanoString, Element Biosciences, Andor, Huron Digital Pathology, Illumina, Ionpath, Waters, In-House, Resolve Biosciences, Singular Genomics, Vizgen, Standard BioTools (Fluidigm), Sciex, Bruker, Evident Scientific (Olympus), Keyence, Miltenyi Biotec, Leica Biosystems, Revvity, Cytek Biosciences, 10x Genomics, Microscopes International, Hamamatsu, Motic |
  | Acquisition instrument model<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific model of the acquisition instrument, as manufacturers often offer various versions with differing features or sensitivities. These differences may be relevant to the processing or interpretation of the data. If the instrument was custom-built or developed internally, enter "In-House". If the model is unknown, enter "Unknown". Example: HiSeq 4000 | SCN400, STELLARIS 5, BZ-X710, Pannoramic MIDI II Digital Scanner, Not applicable, MoticEasyScan One, EVOS M7000, NovaSeq X, LSM 710 Confocal Microscope, NanoZoomer 2.0-HT, timsTOF Ultra 2, Lightsheet 7, Phenocycler-Fusion 1.0, DNBSEQ-T7, timsTOF Pro, Unknown, AVITI, DMi8, Opera Phenix Plus HCS, timsTOF Pro 2, Q Exactive UHMR, Q Exactive, timsTOF SCP, Zyla 4.2 sCMOS, Helios, uScopeHXII-20, Orbitrap Fusion Tribrid, Custom: Multiphoton, QTRAP 5500, timsTOF Ultra, BZ-X800, CyTOF 2, G4X Spatial Sequencer, NextSeq 500, NanoZoomer S360, Hyperion Imaging System, NovaSeq X Plus, CyTOF XT, NanoZoomer-SQ, NextSeq 550, Axio Zoom.V16, Digital Spatial Profiler, timsTOF FleX, timsTOF FleX MALDI-2, NanoZoomer S210, BZ-X810, Axio Observer 7, Cytek Northern Lights, Opera Phenix HCS, Zeiss LightSheet Z.1, IN Cell Analyzer 2200, timsTOF HT, PhenoImager Fusion, DM6 B, Phenocycler-Fusion 2.0, Aperio CS2, Orbitrap Fusion Lumos Tribrid, Resolve Biosciences Molecular Cartography, MALDI timsTOF Flex Prototype, TissueScope LE Slide Scanner, VS200 Slide Scanner, Axio Observer 5, NanoZoomer 2.0-RS, Axio Observer 3, HiSeq 2500, Orbitrap Eclipse Tribrid, Cell DIVE, MERSCOPE, NextSeq 2000, NovaSeq 6000, In-House, HiSeq 4000, Q Exactive HF-X, solariX, Panoramic 150 Digital Scanner, Aperio AT2, MIBIscope, SYNAPT G2-Si, MACSima System, Biomark HD, NanoZoomer S60, CosMx Spatial Molecular Imager, MERSCOPE Ultra, Axio Scan.Z1, Juno System, Q Exactive HF, Xenium Analyzer |
  | Source storage duration value<span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time the sample was stored prior to processing it. For assays performed on tissue sections, this refers to how long the tissue section (e.g., slide) was stored before the assay began (e.g., imaging). For assays performed on suspensions, such as sequencing, it refers to how long the suspension was stored before library construction started. Example: 12 |  |
  | Source storage duration unit<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the source storage duration value. Example: hour | hour, month, year, day, minute |
  | Time since acquisition instrument calibration value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time since the acquisition instrument was last serviced or calibrated. This provides a metric for assessing drift in data capture. Example: 10 |  |
  | Time since acquisition instrument calibration unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the time since acquisition instrument calibration value. Example: month | month, year, day |
  | Contributors path<span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The name of the file containing the ORCID IDs for all contributors to this dataset. Example: ./contributors.csv |  |
  | Data path<span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The top-level directory containing the raw and/or processed data. For a single dataset upload, this might be represented as ".", whereas for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For example, if the data is within a directory named "TEST001-RK", use the syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2", where "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field used solely for data ingestion. Example: ./TEST001-RK |  |
  | Mapped area value<span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The mapped area value, which refers to the specific area covered or captured in various assays. For Visium, it is the area of spots covered by tissue within the captured area, excluding the total possible captured area. For GeoMx, it refers to the area of the AOI being captured. In HiFi, it is the summed area of the ROIs in a single flowcell lane. For CosMx and Resolve, it indicates the area of the FOV (also known as ROI) region being captured. For Xenium, it is the total area of the FOV regions (also known as ROI) being captured. For Stereo-Seq, this value represents the number of beads. Example: 42.25 |  |
  | Mapped area unit<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the mapped area value. If mapping area is not specified, this field may be left blank. Example: um^2 | mm^2, um^2 |
  | Slide ID<span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier assigned to each slide, enabling users to determine which tissue sections were processed together on the same slide. It is recommended that data providers prefix the ID with the center name to prevent overlapping values across different centers. Example: VAN0071-PA-1-1_AF |  |
  | Target retrieval incubation temperature | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The incubation temperature required for target retrieval, which is typically 100 degrees Celsius for RNA assays and 80 degrees Celsius for protein assays. Example: 100 |  |
  | Target retrieval incubation time value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The duration for which a sample is exposed to a target retrieval solution. Example: 15 |  |
  | Target retrieval incubation time unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the target retrieval incubation time value. If no incubation time is specified, this field may be left blank. Example: minute | minute |
  | ProteinaseK concentration | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The concentration of the enzyme Proteinase K within a sample, measured in micrograms per milliliter (ug/ml). Example: 10 |  |
  | ProteinaseK incubation time value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The duration for which a sample is incubated with Proteinase K. Example: 15 |  |
  | ProteinaseK incubation time unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the proteinaseK incubation time value. If no incubation time is specified, this field may be left blank. Example: minute | minute |
  | Probe hybridization time value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The duration for which the oligo-conjugated RNA or oligo-conjugated antibody probes were hybridized with the sample. Example: 30 |  |
  | Probe hybridization time unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the probe hybridization time value. If the hybridization time is not specified, this field may be left blank. Example: minute | hour, minute |
  | Oligo probe panel<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The oligo probe panel used to target genes and/or proteins. If there is a core panel along with add-on modules, the core panel should be selected in this field. Any additional panels utilized should be documented in the "additional_panels_used.csv" file, which must be uploaded alongside the dataset. Example: 10x Genomics; Visium Human Transcriptome Probe Kit-Small; PN 1000363 | 10x Genomics; Chromium Next GEM Single Cell Fixed RNA Mouse Transcriptome Probe Kit, 64 rxns; PN 1000492, 10x Genomics; Xenium Prime 5K Human Pan Tissue & Pathways Panel; PN 1000724, 10x Genomics; Visium Human Transcriptome Probe Kit-Large; PN 1000364, 10x Genomics; Xenium Mouse Multi-Tissue Atlassing Panel; PN 1000627, 10x Genomics; GEM-X Flex Human Transcriptome Probe Kit, 16 samples; PN 1000785, 10x Genomics; Visium Human Transcriptome Probe Kit-Small; PN 1000363, 10x Genomics; Visium Mouse Transcriptome Probe Kit v2.0 - Small; PN 1000667, NanoString Technologies; GeoMx Human IO Proteome Atlas, 4 slides; PN 121300160, 10x Genomics; Visium Human Transcriptome Probe Kit v2 - Small; PN 1000466, NanoString Technologies; CosMx Human 6K Discovery Panel (RNA, 6175 Plex); PN 121500041, NanoString Technologies; CosMx Mouse Universal Cell Characterization Panel (RNA, 1000 Plex); PN CMX-M-USCP-1KP-R, 10x Genomics; Xenium Custom Gene Expression Panel (51-100 genes); PN 1000561, 10X Genomics; Chromium Next GEM Single Cell Fixed RNA Human Transcriptome Probe Kit, 64 rxns; PN 1000456, 10x Genomics; Xenium Human Colon Gene Expression Panel; PN 1000642, NanoString Technologies; CosMx Human Immuno-Oncology Panel (Protein, 64 Plex); PN CMX-H-IOP-64P-P, 10x Genomics; Chromium Fixed RNA Kit, Human Transcriptome 16 rxns x 16 BC; PN 1000547, 10x Genomics; Visium Mouse Transcriptome Probe Kit - Small; PN 1000365, NanoString Technologies; CosMx Hs WTX RNA Panel Kit, 2 slides: PN 121500047, 10x Genomics; Xenium Human Lung Gene Expression Panel; PN 1000601, NanoString Technologies; CosMx Mouse Neuroscience Panel (Protein, 64 Plex); PN CMX-M-Neuro-64P-P, NanoString Technologies; GeoMx Mouse Whole Transcriptome Atlas, 4 slides; PN GMX-RNA-NGS-MsWTA-4, NanoString Technologies; CosMx Mouse Neuroscience Panel (RNA, 1000 Plex); PN CMX-M-NEUP-R, Custom, NanoString Technologies; GeoMx Human Whole Transcriptome Atlas, 4 slides; PN GMX-RNA-NGS-HuWTA-4, 10x Genomics; Xenium Human Multi-Tissue and Cancer Panel v1; PN 1000626, 10x Genomics; Xenium Custom Gene Expression Panel (up to 50 genes); PN 1000464, 10x Genomics; Chromium Fixed RNA Kit, Human Transcriptome, 4 rxns x 1 BC; PN 1000474, 10x Genomics; Xenium Human Skin Gene Expression Panel; PN 1000643, NanoString Technologies; CosMx Human Universal Cell Characterization Panel (RNA, 1000 Plex); PN CMX-H-USCP-1KP-R, 10X Genomics; Chromium Next GEM Single Cell Fixed RNA Human Transcriptome Probe Kit, 16 rxns; PN 1000420, NanoString Technologies; CosMx Hs Univ Cell (RNA, 1000 Plex); PN 121500002 |
  | Is custom probes used?<span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether custom RNA or antibody probes were utilized in the assay. If custom probes were employed, they should be documented in the "custom_probe_set.csv" file. Example: No | Yes, No |
  | Number of panel targets<span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The number of panel targets, which refers to the total count of genes, RNA isoforms, or RNA regions that are targeted by probes. Example: 1000 |  |
  | ROI label<span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The label for the region of interest (ROI). For Resolve and CosMx, this corresponds to the field of view (FOV) label. In the case of Xenium, it refers to the ID of the region containing the analysis. For GeoMx, this information can be located in the "Initial Dataset" spreadsheet, which can be downloaded from within the Data Analysis Suite. Example: Decidua |  |
  | Anatomical structure label | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The label for the overarching anatomical structure. If the anatomical structure is not applicable or not specified, this field may be left blank. Example: Kidney |  |
  | Anatomical structure ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The ontology ID associated with the anatomical structure, typically represented by an UBERON ID. Example: UBERON:0002113 |  |
  | Non global files | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | Specifies a semicolon-separated list of non-global files that are to be included in the dataset. The file paths assume that the files are located in the "TOP/non-global/" directory. For instance, if the file is located at TOP/non-global/lab_processed/images/1-tissue-boundary.geojson, the value for this field would be "./lab_processed/images/1-tissue-boundary.geojson". Once ingested, these files will be copied to their appropriate locations within the respective dataset directory tree. This field is intended for internal HuBMAP processing. Examples for GeoMx and PhenoCycler are provided in the File Locations documentation: https://hubmapconsortium.github.io/ingest-validation-tools/xenium/current/ Example: ./lab_processed/images/1-tissue-boundary.geojson |  |
  | Metadata schema ID<span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique string identifier for the metadata specification version, which is easily interpretable by computers for purposes of data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 |  |
  
definitions: 
|-
  | Pattern | Required? | Description |
  |--|--|--|
  | extras/ | ✓ | Folder for general lab-specific files related to the dataset. |
  | extras/microscope_hardware.json$ | ✓ | [QA/QC] A file generated by the micro-meta app that contains a description of the hardware components of the microscope. Email HuBMAP Consortium Help Desk <help@hubmapconsortium.org> if help is required in generating this document. |
  | extras/microscope_settings.json$ |  | [QA/QC] A file generated by the micro-meta app that contains a description of the settings that were used to acquire the image data. Email HuBMAP Consortium Help Desk <help@hubmapconsortium.org> if help is required in generating this document. |
  | raw/ | ✓ | All raw data files for the experiment. |
  | raw/markers.csv$ |  | A csv file describing any morphology markers used to guide ROI and/or AOI selection. This should minimally contain name of fluorophor, vendor, channel. |
  | raw/additional_panels_used.csv$ |  | If multiple commercial probe panels were used, then the primary probe panel should be selected in the "oligo_probe_panel" metadata field. The additional panels must be included in this file. Each panel record should include:manufacturer, model/name, product code. |
  | raw/custom_probe_set.csv$ |  | This file should contain any custom probes used and must be included if the metadata field "is_custom_probes_used" is "Yes". The file should minimally include:target gene id, probe seq, probe id. The contents of this file are modeled after the 10x Genomics probe set file (see <https://support.10xgenomics.com/spatial-gene-expression-ffpe/probe-sets/probe-set-file-descriptions/probe-set-file-descriptions#probe_set_csv_file>). |
  | raw/custom_probe_set.bed$ |  | This is a BED file version of the custom probe set file. |
  | raw/transcript_locations.csv$ | ✓ | Contains decription of the location of all decoded transcripts. The origin of the coordinate is 0,0 at the top left corner of the image. The file should include: gene name, x, y, z (optional), quality score (optional). It is expected that the first row in the file contains the column header. |
  | raw/custom_gene_list.csv$ |  | This describes the target genes profiled by the assay. For advanced design, this can be probes sequences for splicing or other analysis for any target of interest. The format should minimally contain: gene name, ensemble ID |
  | raw/probes.csv$ |  | A CSV file describing the probe panel used. This is tyipcally what's used to specific the probe set when ordering a probe panel for a Xenium run. |
  | raw/gene_panel.json$ | ✓ | This is the JSON file describing the probes, as output from the xenium-ranger pipeline. |
  | raw/protein_panel.json$ |  | This is the JSON file describing the protein targets, as output from the xenium-ranger pipeline. |
  | raw/images/overlay.{jpeg,tif,tiff}$ |  | State whether an overlay image was used to guide ROI selection. If an overlay is used, then the overlay details will be provided in the protocols.io protocol. If used, this needs to be uploaded. It is not included in the OME TIFF. This can be a JPEG or TIFF file |
  | lab_processed/ | ✓ | Experiment files that were processed by the lab generating the data. |
  | lab_processed/images/ | ✓ | Processed image files |
  | lab_processed/images/*.ome.tiff$ | ✓ | OME-TIFF files (multichannel, multi-layered) produced by the microscopy experiment. If compressed, must use loss-less compression algorithm. For Visium this stitched file should only include the single capture area relevant to the current dataset. For GeoMx there will be one OME TIFF file per slide, with each slide including multiple AOIs. See the following link for the set of fields that are required in the OME TIFF file XML header. <https://docs.google.com/spreadsheets/d/1YnmdTAA0Z9MKN3OjR3Sca8pz-LNQll91wdQoRPSP6Q4/edit#gid=0> |
  | lab_processed/images/*ome-tiff.channels.csv$ | ✓ | This file provides essential documentation pertaining to each channel of the accommpanying OME TIFF. The file should contain one row per OME TIFF channel. The required fields are detailed <https://docs.google.com/spreadsheets/d/1xEJSb0xn5C5fB3k62pj1CyHNybpt4-YtvUs5SUMS44o/edit#gid=0> |
  | lab_processed/images/*tissue-boundary.geojson$ |  | [QA/QC] If the boundaries of the tissue have been identified (e.g., by manual efforts), then the boundary geometry can be included as a GeoJSON file named “*.tissue-boundary.geojson”. |
  | lab_processed/xenium_bundle/ | ✓ | The Xenium bundle includes *.zarr, *.parquet, *.tiff and *.gz files et al. Zarr files are required to view and explore data in Xenium Explorer. Parquet files are faster than CSV files and used extensively by 10X Genomics in Xenium and Visium HD. Sites are free to include in this subdirectory as many Xenium bundle files as possible: <https://www.10xgenomics.com/support/software/xenium-onboard-analysis/latest/analysis/xoa-output-understanding-outputs> |
  | lab_processed/xenium_bundle/cell_feature_matrix.h5$ | ✓ | Contains cell feature matrix |
  | lab_processed/xenium_bundle/experiment.xenium$ | ✓ | Contains specifications |
  | lab_processed/xenium_bundle/nucleus_boundaries.parquet$ | ✓ | Contains polygons of nucleus boundaries |
  | lab_processed/xenium_bundle/cell_boundaries.parquet$ | ✓ | Contains polygons of cell boundaries |
  | lab_processed/xenium_bundle/transcripts.parquet$ | ✓ | Contains transcripts |
  | lab_processed/xenium_bundle/cells.parquet$ | ✓ | Contains cell metadata |
  | lab_processed/xenium_bundle/morphology_mip.ome.tif$ |  | Contains morphology mip |
  | lab_processed/xenium_bundle/morphology_focus.ome.tif$ |  | Morphology focus file for Xenium datasets with a single morphology focus file |
  | lab_processed/xenium_bundle/transcripts.zarr.zip$ |  | The transcripts file made by the Xenium onboard analysis pipeline containing transcript quality and localization based on the image coordinate system of the morphology images. |
  | lab_processed/xenium_bundle/cells.zarr.zip$ | ✓ | Contains segmentation masks and boundaries for nuclei and cells made by the Xenium onboard analysis pipeline, used for assigning transcripts to cells. If using an earlier version of Xenium that doesn't generate this file, a placeholder file should be included to allow for consortial analysis. |
  | lab_processed/xenium_bundle/cell_feature_matrix.zarr.zip$ |  | Cell-feature matrix made by the Xenium onboard analysis pipeline. |
  | lab_processed/xenium_bundle/morphology_focus/ |  | The morphology_focus/ subdirectory should include all morphology_focus.ome.tif files for Xenium datasets with multiple morphology focus files. |
  | lab_processed/xenium_bundle/morphology_focus/morphology_focus_0000.ome.tif$ |  | Morphology focus file - DAPI image |
  | lab_processed/xenium_bundle/morphology_focus/morphology_focus_0001.ome.tif$ |  | Morphology focus file - boundary (ATP1A1/E-Cadherin/CD45) image |
  | lab_processed/xenium_bundle/morphology_focus/morphology_focus_0002.ome.tif$ |  | Morphology focus file - interior - RNA (18S) image |
  | lab_processed/xenium_bundle/morphology_focus/morphology_focus_0003.ome.tif$ |  | Morphology focus file - interior - protein (alphaSMA/Vimentin) image |
    
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
