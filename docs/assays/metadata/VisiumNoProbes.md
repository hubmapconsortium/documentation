--- 
layout: page 
---
# Visium (no probes) 

## Current Metadata Attributes 


| Attribute                     | Label                         | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Value   | Required   |
|-------------------------------|-------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|------------|
| lab_id                        | Lab ID                        | textfield | An internal field labs can use it to add whatever ID(s) they want or need for dataset validation and tracking. This could be a single ID (e.g., "Visium_9OLC_A4_S1") or a delimited list of IDs (e.g., “9OL; 9OLC.A2; Visium_9OLC_A4_S1”). This field will not be accessible to anyone outside of the consortium and no effort will be made to check if IDs provided by one data provider are also used by another.                                                                                                                                                                   |         | False      |
| preparation_protocol_doi      | Preparation protocol DOI      | link      | DOI for the protocols.io page that describes the assay or sample procurment and preparation. For example for an imaging assay, the protocol might include staining of a section through the creation of an OME-TIFF file. In this case the protocol would include any image processing steps required to create the OME-TIFF file. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1                                                                                                                                                                                  |         | True       |
| dataset_type                  | Dataset type                  | textfield | The specific type of dataset being produced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |         | True       |
| contributors_path             | Contributors path             | textfield | The path to the file with the ORCID IDs for all contributors of this dataset (e.g., "./extras/contributors.tsv" or "./contributors.tsv"). This is an internal metadata field that is just used for ingest.                                                                                                                                                                                                                                                                                                                                                                            |         | True       |
| data_path                     | Data path                     | textfield | The top level directory containing the raw and/or processed data. For a single dataset upload this might be "." where as for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For instance, if the data is within a directory called "TEST001-RK" use syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2" in which "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field that is just used for ingest. |         | True       |
| mapped_area_value             | Mapped area value             | numeric   | For Visium, this is the area of spots that was covered by tissue within the captured area, not the total possible captured area which is fixed. For GeoMx this would be the area of the AOI being captured. For HiFi this is the summed area of the ROIs in a single flowcell lane. For CosMx, Xenium and Resolve, this is the area of the FOV (aka ROI) region being captured.                                                                                                                                                                                                       |         | True       |
| mapped_area_unit              | Mapped area unit              | textfield | The unit of measurement for the mapping area. For Visium and GeoMx this is typically um^2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |         | True       |
| spot_size_value               | Spot size value               | numeric   | For assays where spots are used to define discrete capture areas, this is the area of a spot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |         | True       |
| spot_size_unit                | Spot size unit                | textfield | The unit for spot size value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |         | True       |
| number_of_spots               | Number of spots               | numeric   | Number of capture spots within the mapped area. For Visium this would be the number of spots covered by tissue, while it's the number of spots within ROIs for HiFi.                                                                                                                                                                                                                                                                                                                                                                                                                  |         | True       |
| spot_spacing_value            | Spot spacing value            | numeric   | Approximate center-to-center distance between capture spots.  Synonyms: Inter-Spot distance, Spot resolution, Pit size                                                                                                                                                                                                                                                                                                                                                                                                                                                                |         | True       |
| spot_spacing_unit             | Spot spacing unit             | textfield | Units corresponding to inter-spot distance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |         | True       |
| capture_area_id               | Capture area ID               | ENUM      | Which capture area on the slide was used. For Visium this would be [A1, B1, C1, D1]. For HiFi this would be the lane on the flowcell.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ENUM    | True       |
| permeabilization_time_value   | Permeabilization time value   | numeric   | Permeabilization time used for this tissue section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         | False      |
| permeabilization_time_unit    | Permeabilization time unit    | textfield | The unit for the permeabilization time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         | False      |
| metadata_schema_id            | Metadata schema ID            | textfield | The string that serves as the definitive identifier for the metadata schema version and is readily interpretable by computers for data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9                                                                                                                                                                                                                                                                                                                                                                       |         | True       |
| parent_sample_id              | Parent sample ID              | textfield | Unique HuBMAP or SenNet identifier of the sample (i.e., block, section or suspension) used to perform this assay. For example, for a RNAseq assay, the parent would be the suspension, whereas, for one of the imaging assays, the parent would be the tissue section. If an assay comes from multiple parent samples then this should be a comma separated list. Example: HBM386.ZGKG.235, HBM672.MKPK.442 or SNT232.UBHJ.322, SNT329.ALSK.102                                                                                                                                       |         | True       |
| preparation_instrument_vendor | Preparation instrument vendor | textfield | The manufacturer of the instrument used to prepare (staining/processing) the sample for the assay. If an automatic slide staining method was indicated this field should list the manufacturer of the instrument.                                                                                                                                                                                                                                                                                                                                                                     |         | False      |
| preparation_instrument_model  | Preparation instrument model  | textfield | Manufacturers of a staining system instrument may offer various versions (models) of that instrument with different features. Differences in features or sensitivities may be relevant to processing or interpretation of the data.                                                                                                                                                                                                                                                                                                                                                   |         | False      |