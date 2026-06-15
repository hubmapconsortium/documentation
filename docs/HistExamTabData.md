---
layout: page
title: Histology Exam Tab
schema_fields:
  - field: parent_sample_id
    required: true
    type: Textfield
    description: |-
      Unique HuBMAP or SenNet identifier of the sample (i.e., block, section or suspension) used to perform this assay. For example, for a RNAseq assay, the parent would be the suspension, whereas, for one of the imaging assays, the parent would be the tissue section. If an assay comes from multiple parent samples then this should be a comma separated list. Example: HBM386.ZGKG.235, HBM672.MKPK.442 or SNT232.UBHJ.322, SNT329.ALSK.102
  - field: lab_id
    required: false
    type: Textfield
    description: |-
      A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1
  - field: preparation_protocol_doi
    required: true
    type: Textfield
    description: |-
      DOI for the protocols.io page that describes the assay or sample procurment and preparation. For example for an imaging assay, the protocol might include staining of a section through the creation of an OME-TIFF file. In this case the protocol would include any image processing steps required to create the OME-TIFF file. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1
  - field: dataset_type
    required: true
    type: Allowable Value
    description: |-
      The specific type of dataset being produced.
    allowable_values: |-
      ```10X Multiome``` ```2D Imaging Mass Cytometry``` ```ATACseq``` ```Auto-fluorescence``` ```Cell DIVE``` ```CODEX``` ```Confocal``` ```CosMx``` ```CyCIF``` ```DBiT``` ```DESI``` ```Enhanced Stimulated Raman Spectroscopy (SRS)``` ```GeoMx (nCounter)``` ```GeoMx (NGS)``` ```HiFi-Slide``` ```Histology``` ```LC-MS``` ```Light Sheet``` ```MALDI``` ```MERFISH``` ```MIBI``` ```Molecular Cartography``` ```MUSIC``` ```nanoSPLITS``` ```PhenoCycler``` ```Resolve``` ```RNAseq``` ```RNAseq (with probes)``` ```Second Harmonic Generation (SHG)``` ```SIMS``` ```SNARE-seq2``` ```Stereo-seq``` ```Thick section Multiphoton MxIF``` ```Visium (no probes)``` ```Visium (with probes)``` ```Xenium```
  - field: analyte_class
    required: true
    type: Allowable Value
    description: |-
      Analytes are the target molecules being measured with the assay.
    allowable_values: |-
      ```Chromatin``` ```DNA``` ```DNA + RNA``` ```Endogenous fluorophores``` ```Fluorochrome``` ```Lipid``` ```Metabolite``` ```Nucleic acid and protein``` ```Peptide``` ```Polysaccharide``` ```Protein``` ```RNA```
  - field: is_targeted
    required: true
    type: Radio
    description: |-
      Specifies whether or not a specific molecule(s) is/are targeted for detection/measurement by the assay ("Yes" or "No"). The CODEX analyte is protein.
  - field: acquisition_instrument_vendor
    required: true
    type: Allowable Value
    description: |-
      An acquisition instrument is the device that contains the signal detection hardware and signal processing software. Assays generate signals such as light of various intensities or color or signals representing the molecular mass.
    allowable_values: |-
      ```Akoya Biosciences``` ```Andor``` ```BGI Genomics``` ```Bruker``` ```Cytiva``` ```Evident Scientific (Olympus)``` ```GE Healthcare``` ```Hamamatsu``` ```Huron Digital Pathology``` ```Illumina``` ```In-House``` ```Ionpath``` ```Keyence``` ```Leica Biosystems``` ```Leica Microsystems``` ```Motic``` ```NanoString``` ```Resolve Biosciences``` ```Sciex``` ```Standard BioTools (Fluidigm)``` ```Thermo Fisher Scientific``` ```Zeiss Microscopy```
  - field: acquisition_instrument_model
    required: true
    type: Allowable Value
    description: |-
      Manufacturers of an acquisition instrument may offer various versions (models) of that instrument with different features or sensitivities. Differences in features or sensitivities may be relevant to processing or interpretation of the data.
    allowable_values: |-
      ```Aperio AT2``` ```Aperio CS2``` ```Axio Observer 3``` ```Axio Observer 5``` ```Axio Observer 7``` ```Axio Scan.Z1``` ```BZ-X710``` ```BZ-X800``` ```BZ-X810``` ```CosMx Spatial Molecular Imager``` ```Custom: Multiphoton``` ```Digital Spatial Profiler``` ```DM6 B``` ```DNBSEQ-T7``` ```EVOS M7000``` ```HiSeq 2500``` ```HiSeq 4000``` ```Hyperion Imaging System``` ```IN Cell Analyzer 2200``` ```Lightsheet 7``` ```MALDI timsTOF Flex Prototype``` ```MIBIscope``` ```MoticEasyScan One``` ```NanoZoomer 2.0-HT``` ```NanoZoomer S210``` ```NanoZoomer S360``` ```NanoZoomer S60``` ```NanoZoomer-SQ``` ```NextSeq 2000``` ```NextSeq 500``` ```NextSeq 550``` ```NovaSeq 6000``` ```NovaSeq X``` ```NovaSeq X Plus``` ```Orbitrap Eclipse Tribrid``` ```Orbitrap Fusion Lumos Tribrid``` ```Phenocycler-Fusion 1.0``` ```Phenocycler-Fusion 2.0``` ```PhenoImager Fusion``` ```Q Exactive``` ```Q Exactive HF``` ```Q Exactive UHMR``` ```QTRAP 5500``` ```Resolve Biosciences Molecular Cartography``` ```SCN400``` ```STELLARIS 5``` ```TissueScope LE Slide Scanner``` ```Unknown``` ```VS200 Slide Scanner``` ```Xenium Analyzer``` ```Zyla 4.2 sCMOS```
  - field: source_storage_duration_value
    required: true
    type: Numeric
    description: |-
      How long was the source material stored, prior to this sample being processed? For assays applied to tissue sections, this would be how long the tissue section (e.g., slide) was stored, prior to the assay beginning (e.g., imaging). For assays applied to suspensions such as sequencing, this would be how long the suspension was stored before library construction began.
  - field: source_storage_duration_unit
    required: true
    type: Allowable Value
    description: |-
      The time duration unit of measurement
    allowable_values: |-
      ```hour``` ```month``` ```day``` ```minute``` ```year```
  - field: time_since_acquisition_instrument_calibration_value
    required: false
    type: Numeric
    description: |-
      The amount of time since the acqusition instrument was last serviced by the vendor. This provides a metric for assessing drift in data capture.
  - field: time_since_acquisition_instrument_calibration_unit
    required: false
    type: Allowable Value
    description: |-
      The time unit of measurement
    allowable_values: |-
      ```Column-by-column``` ```Not applicable``` ```Row-by-row``` ```Snake-by-columns``` ```Snake-by-rows```
  - field: contributors_path
    required: true
    type: Textfield
    description: |-
      The path to the file with the ORCID IDs for all contributors of this dataset (e.g., "./extras/contributors.tsv" or "./contributors.tsv"). This is an internal metadata field that is just used for ingest.
  - field: data_path
    required: true
    type: Textfield
    description: |-
      The top level directory containing the raw and/or processed data. For a single dataset upload this might be "." where as for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For instance, if the data is within a directory called "TEST001-RK" use syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2" in which "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field that is just used for ingest.
  - field: is_image_preprocessing_required
    required: false
    type: Radio
    description: |-
      Indicates whether image preprocessing is necessary based on the type of acquisition instrument used, such as a microscope or slide scanner. This may involve steps like fusing image tiles to assemble the complete image. Example: Yes
  - field: stain_name
    required: true
    type: Allowable Value
    description: |-
      The name of the chemical stains (dyes) applied to histology samples to highlight important features of the tissue as well as to enhance the tissue contrast.
    allowable_values: |-
      ```AB-PAS``` ```H&E``` ```H-DAB``` ```LFB``` ```PAS``` ```Trichrome```
  - field: stain_technique
    required: false
    type: Allowable Value
    description: |-
      There are typically three types of stains: progressive, modified progressive, and regressive. Progressive staining occurs when the hematoxylin is added to the tissue without being followed by a differentiator to remove excess dye. With regressive and modified progressive staining, a differentiator is used.
    allowable_values: |-
      ```Modified progressive staining``` ```Not applicable``` ```Progressive staining``` ```Regressive staining```
  - field: is_batch_staining_done
    required: true
    type: Radio
    description: |-
      Are the slides stained using a linear batch method or individually?
  - field: is_staining_automated
    required: true
    type: Radio
    description: |-
      Is the slide staining automated with an instrument?
  - field: preparation_instrument_vendor
    required: false
    type: Allowable Value
    description: |-
      The manufacturer of the instrument used to prepare (staining/processing) the sample for the assay. If an automatic slide staining method was indicated this field should list the manufacturer of the instrument.
    allowable_values: |-
      ```10x Genomics``` ```Hamamatsu``` ```HTX Technologies``` ```In-House``` ```Leica Biosystems``` ```Not applicable``` ```Roche Diagnostics``` ```SunChrom``` ```Thermo Fisher Scientific```
  - field: preparation_instrument_model
    required: false
    type: Allowable Value
    description: |-
      Manufacturers of a staining system instrument may offer various versions (models) of that instrument with different features. Differences in features or sensitivities may be relevant to processing or interpretation of the data.
    allowable_values: |-
      ```AutoStainer XL``` ```Chromium Connect``` ```Chromium Controller``` ```Chromium iX``` ```Chromium X``` ```Discovery Ultra``` ```EVOS M7000``` ```M3+ Sprayer``` ```M5 Sprayer``` ```NanoZoomer S210``` ```NanoZoomer S360``` ```NanoZoomer S60``` ```Not applicable``` ```ST5020 Multistainer``` ```Sublimator``` ```SunCollect Sprayer``` ```TM-Sprayer``` ```Visium CytAssist```
  - field: slide_id
    required: false
    type: Textfield
    description: |-
      A unique ID denoting the slide used. This allows users the ability to determine which tissue sections were processed together on the same slide. It is recommended that data providers prefix the ID with the center name, to prevent values overlapping across centers.
  - field: tile_configuration
    required: false
    type: Allowable Value
    description: |-
      The configuration of tiles used for stitching in the assay process. If no tile configuration is applicable, enter "Not applicable". Example: Row-by-row
    allowable_values: |-
      ```Column-by-column``` ```Not applicable``` ```Snake-by-columns``` ```Row-by-row``` ```Snake-by-rows```
  - field: scan_direction
    required: false
    type: Allowable Value
    description: |-
      The direction of imaging, which is necessary for the stitching process. Example: Left-and-down
    allowable_values: |-
      ```Left-and-down``` ```Right-and-down``` ```Not applicable``` ```Right-and-up``` ```Left-and-up```
  - field: tiled_image_columns
    required: false
    type: Numeric
    description: |-
      The number of columns used in the stitching process of a tiled image, often referred to as the grid size in the x-dimension. Example: 5
  - field: tiled_image_count
    required: false
    type: Numeric
    description: |-
      The total number of raw tiled images captured, which are intended to be stitched together. Example: 75
  - field: intended_tile_overlap_percentage
    required: false
    type: Numeric
    description: |-
      The intended percentage of overlap between tiled images. This value serves as the set point, although slight variations may occur during image acquisition due to stage registration. Example: 5
  - field: non_global_files
    required: false
    type: Textfield
    description: |-
      A semicolon separated list of non-shared files to be included in the dataset. The path assumes the files are located in the "TOP/non-global/" directory. For example, for the file is TOP/non-global/lab_processed/images/1-tissue-boundary.geojson the value of this field would be "./lab_processed/images/1-tissue-boundary.geojson". After ingest, these files will be copied to the appropriate locations within the respective dataset directory tree. This field is used for internal HuBMAP processing. Examples for GeoMx and PhenoCycler are provided in the File Locations documentation: https://docs.google.com/document/d/1n2McSs9geA9Eli4QWQaB3c9R3wo5d5U1Xd57DWQfN5Q/edit#heading=h.1u82i4axggee
  - field: metadata_schema_id
    required: true
    type: Textfield
    description: |-
      The string that serves as the definitive identifier for the metadata schema version and is readily interpretable by computers for data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9
---
# Histology Exam Tab

<dl class="schema-definitions">
{% for item in page.schema_fields %}
  <dt>{{ item.field }}{% if item.required %} <span class="requiredMark">*</span>{% endif %}</dt>
  <dd>
    <strong>Type:</strong> {{ item.type }}<br />
    <strong>Description:</strong> {{ item.description }}{% if item.allowable_values %}<br />
    <strong>Allowable Values:</strong> {{ item.allowable_values }}{% endif %}
  </dd>
{% endfor %}
</dl>
