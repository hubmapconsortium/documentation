# MERFISH

## Current Metadata Attributes

| Attribute | Type      | Description              | Allowable Values |
| ----------- | ----------- | -------------------------- | ------------------ |
|Parent sample ID | type |Unique HuBMAP or SenNet identifier of the sample (i.e., block, section or suspension) used to perform this assay. For example, for a RNAseq assay, the parent would be the suspension, whereas, for one of the imaging assays, the parent would be the tissue section. If an assay comes from multiple parent samples then this should be a comma separated list. Example: HBM386.ZGKG.235, HBM672.MKPK.442 or SNT232.UBHJ.322, SNT329.ALSK.102| value |
|Lab ID | type |An internal field labs can use it to add whatever ID(s) they want or need for dataset validation and tracking. This could be a single ID (e.g., "Visium_9OLC_A4_S1") or a delimited list of IDs (e.g., “9OL; 9OLC.A2; Visium_9OLC_A4_S1”). This field will not be accessible to anyone outside of the consortium and no effort will be made to check if IDs provided by one data provider are also used by another.| value |
|Preparation protocol DOI | type |DOI for the protocols.io page that describes the assay or sample procurment and preparation. For example for an imaging assay, the protocol might include staining of a section through the creation of an OME-TIFF file. In this case the protocol would include any image processing steps required to create the OME-TIFF file. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1| value |
|Dataset type | type |The specific type of dataset being produced.| value |
|Analyte class | type |Analytes are the target molecules being measured with the assay.| value |
|Is targeted? | type |Specifies whether or not a specific molecule(s) is/are targeted for detection/measurement by the assay ("Yes" or "No"). The CODEX analyte is protein.| value |
|Acquisition instrument vendor | type |An acquisition instrument is the device that contains the signal detection hardware and signal processing software. Assays generate signals such as light of various intensities or color or signals representing the molecular mass.| value |
|Acquisition instrument model | type |Manufacturers of an acquisition instrument may offer various versions (models) of that instrument with different features or sensitivities. Differences in features or sensitivities may be relevant to processing or interpretation of the data.| value |
|Source storage duration value | type |How long was the source material stored, prior to this sample being processed? For assays applied to tissue sections, this would be how long the tissue section (e.g., slide) was stored, prior to the assay beginning (e.g., imaging). For assays applied to suspensions such as sequencing, this would be how long the suspension was stored before library construction began.| value |
|Source storage duration unit | type |The time duration unit of measurement| value |
|Time since acquisition instrument calibration value | type |The amount of time since the acqusition instrument was last serviced by the vendor. This provides a metric for assessing drift in data capture.| value |
|Time since acquisition instrument calibration unit | type |The time unit of measurement| value |
|Contributors path | type |The path to the file with the ORCID IDs for all contributors of this dataset (e.g., "./extras/contributors.tsv" or "./contributors.tsv"). This is an internal metadata field that is just used for ingest.| value |
|Data path | type |The top level directory containing the raw and/or processed data. For a single dataset upload this might be "." where as for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For instance, if the data is within a directory called "TEST001-RK" use syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2" in which "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field that is just used for ingest.| value |
|Mapped area value | type |For Visium, this is the area of spots that was covered by tissue within the captured area, not the total possible captured area which is fixed. For GeoMx this would be the area of the AOI being captured. For HiFi this is the summed area of the ROIs in a single flowcell lane. For CosMx, Xenium and Resolve, this is the area of the FOV (aka ROI) region being captured.| value |
|Mapped area unit | type |The unit of measurement for the mapping area. For Visium and GeoMx this is typically um^2.| value |
|Permeabilization time value | type |Permeabilization time used for this tissue section.| value |
|Permeabilization time unit | type |The unit for the permeabilization time.| value |
|Slide ID | type |A unique ID denoting the slide used. This allows users the ability to determine which tissue sections were processed together on the same slide. It is recommended that data providers prefix the ID with the center name, to prevent values overlapping across centers.| value |
|Target retrieval incubation temperature | type |Will normally be 100 degrees Celsius for RNA assays, and 80 degrees Celsius for protein assays.| value |
|Target retrieval incubation time value | type |The duration for which a sample is exposed to a target retrieval solution.| value |
|Target retrieval incubation time unit | type |The units for target retrieval incubation time value.| value |
|ProteinaseK concentration | type |The amount or concentration of the enzyme Proteinase K within a sample (in ug/ml).| value |
|ProteinaseK incubation time value | type |The duration for which a sample is exposed to Proteinase K.| value |
|ProteinaseK incubation time unit | type |The units for proteinaseK incubation time value.| value |
|Probe hybridization time value | type |How long was the oligo-conjugated RNA or oligo-conjugated antibody probes hybridized with the sample?| value |
|Probe hybridization time unit | type |The units for probe hybridization time value.| value |
|Oligo probe panel | type |This is the probe panel used to target genes and/or proteins. In cases where there is a core panel and add-on modules, the core panel should be selected here. If additional panels are used, then they must be included in the "additional_panels_used.csv" file that's uploaded with the dataset.| value |
|Is custom probes used? | type |State ("Yes" or "No") whether custom RNA or antibody probes were used. If custom probes were used, they must be listed in the "custom_probe_set.csv" file.| value |
|Number of panel targets | type |How many genes, RNA isoforms or RNA regions are targeted by probes.| value |
|ROI label | type |A label for the region of interest (ROI). For Xenium, Resolve and CosMx, this is the field of view (FOV) label. For GeoMx this can be found in the "Initial Dataset" spreadsheet (download from within Data Analysis Suite).| value |
|Anatomical structure label | type |The overarching anatomical structure.| value |
|Anatomical structure ID | type |The ontology ID for the parent structure. Typically this would be an UBERON ID.| value |
|Non global files | type |A semicolon separated list of non-shared files to be included in the dataset. The path assumes the files are located in the "TOP/non-global/" directory. For example, for the file is TOP/non-global/lab_processed/images/1-tissue-boundary.geojson the value of this field would be "./lab_processed/images/1-tissue-boundary.geojson". After ingest, these files will be copied to the appropriate locations within the respective dataset directory tree. This field is used for internal HuBMAP processing. Examples for GeoMx and PhenoCycler are provided in the File Locations documentation: https://docs.google.com/document/d/1n2McSs9geA9Eli4QWQaB3c9R3wo5d5U1Xd57DWQfN5Q/edit#heading=h.1u82i4axggee| value |
|Number of additional stains | type |This would be minimally 2 (always include DAPI and polyT) and can include 6 more.| value |
|Metadata schema ID | type |The string that serves as the definitive identifier for the metadata schema version and is readily interpretable by computers for data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 | value | | value |
