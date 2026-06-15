---
layout: doi-landing-page
title: Metadata Reporting Standards - Histology
spec_name: Histology
version_label: Version 1
doi: 10.35079/HBM788.QPBW.699
published: September 26, 2025
subjects: "AB-PAS, H&E, H-DAB, LFB, PAS, SBB, Trichrome"
summary: The microscopic study of tissue composition and structure, often referred to as microscopic anatomy. It involves examining tissue samples, typically after they've been sectioned, stained, and placed under a microscope.
schema_intro:
deprecated_intro:
schema_doc_href: "#"
validator_href: "#"
datasets_href: "#"
datasets_text: The HuBMAP Data Portal is an open platform to discover, visualize, and download standardized healthy single-cell and spatial tissue data.
citation_text: Fisher, Hardi, Morgan, Honick, O'Connor, Pillai, Blood, Silverstein, Musen. Histology Dataset Type. v1.0, HuBMAP, 26 Sept 2025. https://doi.org/10.35079/HBM788.QPBW.699
reuse_text: This standard may be reused, expanded, or referenced by external repositories.  [Include DCWG paper citation here]
contributors_intro: Below is the information for the primary contributors to the HuBMAP and SenNet metadata reporting standards. The full list of contributors can be found here [DCWG paper citation].
contributors_note: For questions about this standard, reach out to the individuals listed below, either via the email address listed in the table or via contact information provided on their ORCID profile page.
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
schema_items: |-
  | Attribute | Type | Description | Allowable Values |
  |------|------|-------------|-------------------|
  | parent_sample_id <span class="requiredMark">*</span>| <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | Unique HuBMAP or SenNet identifier of the sample (i.e., block, section or suspension) used to perform this assay. For example, for a RNAseq assay, the parent would be the suspension, whereas, for one of the imaging assays, the parent would be the tissue section. If an assay comes from multiple parent samples then this should be a comma separated list. Example: HBM386.ZGKG.235, HBM672.MKPK.442 or SNT232.UBHJ.322, SNT329.ALSK.102 |  |
  | lab_id | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1 |  |
  | preparation_protocol_doi <span class="requiredMark">*</span>| <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | DOI for the protocols.io page that describes the assay or sample procurment and preparation. For example for an imaging assay, the protocol might include staining of a section through the creation of an OME-TIFF file. In this case the protocol would include any image processing steps required to create the OME-TIFF file. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1 |  |
  | dataset_type <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific type of dataset being produced. | ```10X Multiome``` ```2D Imaging Mass Cytometry``` ```ATACseq``` ```Auto-fluorescence``` ```Cell DIVE``` ```CODEX``` ```Confocal``` ```CosMx``` ```CyCIF``` ```DBiT``` ```DESI``` ```Enhanced Stimulated Raman Spectroscopy (SRS)``` ```GeoMx (nCounter)``` ```GeoMx (NGS)``` ```HiFi-Slide``` ```Histology``` ```LC-MS``` ```Light Sheet``` ```MALDI``` ```MERFISH``` ```MIBI``` ```Molecular Cartography``` ```MUSIC``` ```nanoSPLITS``` ```PhenoCycler``` ```Resolve``` ```RNAseq``` ```RNAseq (with probes)``` ```Second Harmonic Generation (SHG)``` ```SIMS``` ```SNARE-seq2``` ```Stereo-seq``` ```Thick section Multiphoton MxIF``` ```Visium (no probes)``` ```Visium (with probes)``` ```Xenium``` |
  | analyte_class <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | Analytes are the target molecules being measured with the assay. | ```Chromatin``` ```DNA``` ```DNA + RNA``` ```Endogenous fluorophores``` ```Fluorochrome``` ```Lipid``` ```Metabolite``` ```Nucleic acid and protein``` ```Peptide``` ```Polysaccharide``` ```Protein``` ```RNA``` |
  | is_targeted <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Specifies whether or not a specific molecule(s) is/are targeted for detection/measurement by the assay ("Yes" or "No"). The CODEX analyte is protein. |  |
  | acquisition_instrument_vendor <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | An acquisition instrument is the device that contains the signal detection hardware and signal processing software. Assays generate signals such as light of various intensities or color or signals representing the molecular mass. | ```Akoya Biosciences``` ```Andor``` ```BGI Genomics``` ```Bruker``` ```Cytiva``` ```Evident Scientific (Olympus)``` ```GE Healthcare``` ```Hamamatsu``` ```Huron Digital Pathology``` ```Illumina``` ```In-House``` ```Ionpath``` ```Keyence``` ```Leica Biosystems``` ```Leica Microsystems``` ```Motic``` ```NanoString``` ```Resolve Biosciences``` ```Sciex``` ```Standard BioTools (Fluidigm)``` ```Thermo Fisher Scientific``` ```Zeiss Microscopy``` |
  | acquisition_instrument_model <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | Manufacturers of an acquisition instrument may offer various versions (models) of that instrument with different features or sensitivities. Differences in features or sensitivities may be relevant to processing or interpretation of the data. | ```Aperio AT2``` ```Aperio CS2``` ```Axio Observer 3``` ```Axio Observer 5``` ```Axio Observer 7``` ```Axio Scan.Z1``` ```BZ-X710``` ```BZ-X800``` ```BZ-X810``` ```CosMx Spatial Molecular Imager``` ```Custom: Multiphoton``` ```Digital Spatial Profiler``` ```DM6 B``` ```DNBSEQ-T7``` ```EVOS M7000``` ```HiSeq 2500``` ```HiSeq 4000``` ```Hyperion Imaging System``` ```IN Cell Analyzer 2200``` ```Lightsheet 7``` ```MALDI timsTOF Flex Prototype``` ```MIBIscope``` ```MoticEasyScan One``` ```NanoZoomer 2.0-HT``` ```NanoZoomer S210``` ```NanoZoomer S360``` ```NanoZoomer S60``` ```NanoZoomer-SQ``` ```NextSeq 2000``` ```NextSeq 500``` ```NextSeq 550``` ```NovaSeq 6000``` ```NovaSeq X``` ```NovaSeq X Plus``` ```Orbitrap Eclipse Tribrid``` ```Orbitrap Fusion Lumos Tribrid``` ```Phenocycler-Fusion 1.0``` ```Phenocycler-Fusion 2.0``` ```PhenoImager Fusion``` ```Q Exactive``` ```Q Exactive HF``` ```Q Exactive UHMR``` ```QTRAP 5500``` ```Resolve Biosciences Molecular Cartography``` ```SCN400``` ```STELLARIS 5``` ```TissueScope LE Slide Scanner``` ```Unknown``` ```VS200 Slide Scanner``` ```Xenium Analyzer``` ```Zyla 4.2 sCMOS``` |
  | source_storage_duration_value <span class="requiredMark">*</span>| <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | How long was the source material stored, prior to this sample being processed? For assays applied to tissue sections, this would be how long the tissue section (e.g., slide) was stored, prior to the assay beginning (e.g., imaging). For assays applied to suspensions such as sequencing, this would be how long the suspension was stored before library construction began. |  |
  | source_storage_duration_unit <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The time duration unit of measurement | ```hour``` ```month``` ```day``` ```minute``` ```year``` |
  | time_since_acquisition_instrument_calibration_value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The amount of time since the acqusition instrument was last serviced by the vendor. This provides a metric for assessing drift in data capture. |  |
  | time_since_acquisition_instrument_calibration_unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The time unit of measurement | ```Column-by-column``` ```Not applicable``` ```Row-by-row``` ```Snake-by-columns``` ```Snake-by-rows``` |
  | contributors_path <span class="requiredMark">*</span>| <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The path to the file with the ORCID IDs for all contributors of this dataset (e.g., "./extras/contributors.tsv" or "./contributors.tsv"). This is an internal metadata field that is just used for ingest. |  |
  | data_path <span class="requiredMark">*</span>| <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The top level directory containing the raw and/or processed data. For a single dataset upload this might be "." where as for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For instance, if the data is within a directory called "TEST001-RK" use syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2" in which "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field that is just used for ingest. |  |
  | is_image_preprocessing_required | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether image preprocessing is necessary based on the type of acquisition instrument used, such as a microscope or slide scanner. This may involve steps like fusing image tiles to assemble the complete image. Example: Yes |  |
  | stain_name <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The name of the chemical stains (dyes) applied to histology samples to highlight important features of the tissue as well as to enhance the tissue contrast. | ```AB-PAS``` ```H&E``` ```H-DAB``` ```LFB``` ```PAS``` ```Trichrome``` |
  | stain_technique | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | There are typically three types of stains: progressive, modified progressive, and regressive. Progressive staining occurs when the hematoxylin is added to the tissue without being followed by a differentiator to remove excess dye. With regressive and modified progressive staining, a differentiator is used. | ```Modified progressive staining``` ```Not applicable``` ```Progressive staining``` ```Regressive staining``` |
  | is_batch_staining_done <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Are the slides stained using a linear batch method or individually? |  |
  | is_staining_automated <span class="requiredMark">*</span>| <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Is the slide staining automated with an instrument? |  |
  | preparation_instrument_vendor | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The manufacturer of the instrument used to prepare (staining/processing) the sample for the assay. If an automatic slide staining method was indicated this field should list the manufacturer of the instrument. | ```10x Genomics``` ```Hamamatsu``` ```HTX Technologies``` ```In-House``` ```Leica Biosystems``` ```Not applicable``` ```Roche Diagnostics``` ```SunChrom``` ```Thermo Fisher Scientific``` |
  | preparation_instrument_model | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | Manufacturers of a staining system instrument may offer various versions (models) of that instrument with different features. Differences in features or sensitivities may be relevant to processing or interpretation of the data. | ```AutoStainer XL``` ```Chromium Connect``` ```Chromium Controller``` ```Chromium iX``` ```Chromium X``` ```Discovery Ultra``` ```EVOS M7000``` ```M3+ Sprayer``` ```M5 Sprayer``` ```NanoZoomer S210``` ```NanoZoomer S360``` ```NanoZoomer S60``` ```Not applicable``` ```ST5020 Multistainer``` ```Sublimator``` ```SunCollect Sprayer``` ```TM-Sprayer``` ```Visium CytAssist``` |
  | slide_id | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A unique ID denoting the slide used. This allows users the ability to determine which tissue sections were processed together on the same slide. It is recommended that data providers prefix the ID with the center name, to prevent values overlapping across centers. |  |
  | tile_configuration | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The configuration of tiles used for stitching in the assay process. If no tile configuration is applicable, enter "Not applicable". Example: Row-by-row | ```Column-by-column``` ```Not applicable``` ```Snake-by-columns``` ```Row-by-row``` ```Snake-by-rows``` |
  | scan_direction | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The direction of imaging, which is necessary for the stitching process. Example: Left-and-down | ```Left-and-down``` ```Right-and-down``` ```Not applicable``` ```Right-and-up``` ```Left-and-up``` |
  | tiled_image_columns | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The number of columns used in the stitching process of a tiled image, often referred to as the grid size in the x-dimension. Example: 5 |  |
  | tiled_image_count | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The total number of raw tiled images captured, which are intended to be stitched together. Example: 75 |  |
  | intended_tile_overlap_percentage | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The intended percentage of overlap between tiled images. This value serves as the set point, although slight variations may occur during image acquisition due to stage registration. Example: 5 |  |
  | non_global_files | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A semicolon separated list of non-shared files to be included in the dataset. The path assumes the files are located in the "TOP/non-global/" directory. For example, for the file is TOP/non-global/lab_processed/images/1-tissue-boundary.geojson the value of this field would be "./lab_processed/images/1-tissue-boundary.geojson". After ingest, these files will be copied to the appropriate locations within the respective dataset directory tree. This field is used for internal HuBMAP processing. Examples for GeoMx and PhenoCycler are provided in the File Locations documentation: https://docs.google.com/document/d/1n2McSs9geA9Eli4QWQaB3c9R3wo5d5U1Xd57DWQfN5Q/edit#heading=h.1u82i4axggee |  |
  | metadata_schema_id <span class="requiredMark">*</span>| <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The string that serves as the definitive identifier for the metadata schema version and is readily interpretable by computers for data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 |  |
deprecated_items: |-
  | Attribute | Type | Description | Allowable Values |
  |------|------|-------------|-------------------|
  | tiled_image_columns | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The number of columns used in the stitching process of a tiled image, often referred to as the grid size in the x-dimension. Example: 5 |  |
  | tiled_image_count | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The total number of raw tiled images captured, which are intended to be stitched together. Example: 75 |  |
definitions:
  - field: metadata.tsv
    description: The main metadata file for the submission.
    rules: Required
  - field: extras/
    description: Folder for supporting files associated with the dataset.
    rules: Directory
  - field: raw/
    description: Folder containing raw data files from the experiment.
    rules: Directory
  - field: raw/images/
    description: Folder containing raw image files.
    rules: Directory
  - field: lab_processed/images/
    description: Folder containing processed image outputs.
    rules: Directory
contributors:
  - name: Contributor One
    affiliation: HuBMAP
    contact: contributor.one@example.org
    orcid: https://orcid.org/0000-0000-0000-0001
  - name: Contributor Two
    affiliation: SenNet
    contact: contributor.two@example.org
    orcid: https://orcid.org/0000-0000-0000-0002
  - name: Contributor Three
    affiliation: HuBMAP
    contact: contributor.three@example.org
    orcid: https://orcid.org/0000-0000-0000-0003
---

{% include doi-template/page.html %}
