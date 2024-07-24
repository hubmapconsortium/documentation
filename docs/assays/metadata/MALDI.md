---
layout: page
---

# MALDI

## Current Metadata Attributes

| Attribute | Type      | Description              | Allowable Values |
| ----------- | ----------- | -------------------------- | ------------------ |
|Parent sample ID | textfield | Unique HuBMAP or SenNet identifier of the sample (i.e., block, section or suspension) used to perform this assay. For example, for a RNAseq assay, the parent would be the suspension, whereas, for one of the imaging assays, the parent would be the tissue section. If an assay comes from multiple parent samples then this should be a comma separated list. Example: HBM386.ZGKG.235, HBM672.MKPK.442 or SNT232.UBHJ.322, SNT329.ALSK.102| value |
|Lab ID | textfield | An internal field labs can use it to add whatever ID(s) they want or need for dataset validation and tracking. This could be a single ID (e.g., "Visium_9OLC_A4_S1") or a delimited list of IDs (e.g., “9OL; 9OLC.A2; Visium_9OLC_A4_S1”). This field will not be accessible to anyone outside of the consortium and no effort will be made to check if IDs provided by one data provider are also used by another.| value |
|Preparation protocol DOI | textfield | DOI for the protocols.io page that describes the assay or sample procurment and preparation. For example for an imaging assay, the protocol might include staining of a section through the creation of an OME-TIFF file. In this case the protocol would include any image processing steps required to create the OME-TIFF file. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1| value |
|Dataset type | textfield | The specific type of dataset being produced.| value |
|Analyte class | textfield | Analytes are the target molecules being measured with the assay.| value |
|Is targeted? | numeric | Specifies whether or not a specific molecule(s) is/are targeted for detection/measurement by the assay ("Yes" or "No"). The CODEX analyte is protein.| value |
|Acquisition instrument vendor | textfield | An acquisition instrument is the device that contains the signal detection hardware and signal processing software. Assays generate signals such as light of various intensities or color or signals representing the molecular mass.| value |
|Acquisition instrument model | numeric | Manufacturers of an acquisition instrument may offer various versions (models) of that instrument with different features or sensitivities. Differences in features or sensitivities may be relevant to processing or interpretation of the data.| value |
|Source storage duration value | textfield | How long was the source material (parent) stored, prior to this sample being processed.| value |
|Source storage duration unit | link | The time duration unit of measurement| value |
|Time since acquisition instrument calibration value | radio | The amount of time since the acqusition instrument was last serviced by the vendor. This provides a metric for assessing drift in data capture.| value |
|Time since acquisition instrument calibration unit | textfield | The time unit of measurement| value |
|Contributors path | textfield | The path to the file with the ORCID IDs for all contributors of this dataset (e.g., "./extras/contributors.tsv" or "./contributors.tsv"). This is an internal metadata field that is just used for ingest.| value |
|Data path | textfield | The top level directory containing the raw and/or processed data. For a single dataset upload this might be "." where as for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For instance, if the data is within a directory called "TEST001-RK" use syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2" in which "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field that is just used for ingest.| value |
|MS ionization technique | numeric | The ionization approach (i.e., sample probing method) for performing imaging mass spectrometry.| value |
|MS scan mode | numeric | MS (mass spectrometry) scan mode refers to the number of steps in the separation of fragments.| value |
|Mass analysis polarity | textfield | The polarity of the mass analysis (positive or negative ion modes).| value |
|Mass-to-charge range low value | textfield | The low value of the scanned mass-to-charge range, for MS1. (unitless)| value |
|Mass-to-charge range high value | textfield | The high value of the scanned mass-to-charge range, for MS1. (unitless)| value |
|Mass resolving power | textfield | The mass resolving power m/∆m, where ∆m is defined as the full width at half-maximum (FWHM) for a given peak with a specified mass-to-charge (m/z). (unitless)| value |
|Mass-to-charge resolving power | textfield | The peak (m/z) used to calculate the resolving power.| value |
|Ion mobility | textfield | Specifies which technology was used for ion mobility spectrometry. Technologies for measuring ion mobility: Traveling Wave Ion Mobility Spectrometry (TWIMS), Trapped Ion Mobility Spectrometry (TIMS), High Field Asymmetric waveform ion Mobility Spectrometry (FAIMS), Drift Tube Ion Mobility Spectrometry (DTIMS), Structures for Lossless Ion Manipulations (SLIM), and cyclic Ion Mobility Spectrometry (cIMS).| value |
|Matrix deposition method | numeric | Common methods of depositing matrix for assisting in desorption and ionization in imaging mass spectrometry include robotic spotting, electrospray deposition, and sublimation.| value |
|Preparation instrument vendor | numeric | The manufacturer of the instrument used to prepare (staining/processing) the sample for the assay. If an automatic slide staining method was indicated this field should list the manufacturer of the instrument.| value |
|Preparation instrument model | link | Manufacturers of a staining system instrument may offer various versions (models) of that instrument with different features. Differences in features or sensitivities may be relevant to processing or interpretation of the data.| value |
|Preparation matrix | textfield | The matrix is a compound of crystallized molecules that acts like a buffer between the sample and the ionizing probe. It also helps ionize the sample, carrying it along the flight tube so it can be detected.| value |
|Analysis protocol DOI | textfield | A DOI to a protocols.io protocol describing the software and database(s) used to process the raw data. Example: https://dx.doi.org/10.17504/protocols.io.bsu5ney6| value |
|Metadata schema ID | textfield | The string that serves as the definitive identifier for the metadata schema version and is readily interpretable by computers for data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 | value | 
