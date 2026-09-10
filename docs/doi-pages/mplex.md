---
layout: doi-landing-page
title: Metadata Reporting Standards - MPLeX
spec_name: Multi-Phase Liquid Extraction (MPLeX)
version_label: Version 1
doi: 10.35079/HBM765.TCFP.373
download_href: "https://github.com/hubmapconsortium/ingest-validation-tools/raw/refs/heads/main/docs/mplex/current/doi-object.zip"
md5_hash: c60316e366093b12bbc26795105753a1
published: September 2, 2026 
subjects: 
summary: MPLEx is a simple, rapid, and robust sample preparation protocol for integrated multi-omics analysis from diverse biological sample types, including environmental, in vitro, and clinical specimens. Based on a modified Bligh-Dyer solvent extraction, MPLEx simultaneously partitions lipids, metabolites, and proteins into distinct phases in a single step, enabling individual downstream analysis of each fraction by mass spectrometry-based lipidomics, metabolomics, and proteomics. 
schema_doc_href: "https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2F2015a1c3-fcf8-458c-8572-0f65e89f2405"
validator_href: "https://metadatavalidator.metadatacenter.org"
datasets_href: "https://portal.hubmapconsortium.org/search/datasets"
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
  ├── raw/
  │   └── mplex/
  └── lab_processed/
      └── mplex/

schema_items: 
|-
  | Attribute | Type | Description | Allowable Values |
  |--------|----|--------------|-------------|
  | Parent sample ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier from HuBMAP or SenNet for the sample (such as a block, section, or suspension) used to perform the assay. For instance, in an RNAseq assay, the parent sample would be the suspension, while in imaging assays, it would be the tissue section. If the assay is derived from multiple parent samples, this field should contain a comma-separated list of identifiers. Example: HBM386.ZGKG.235, HBM672.MKPK.442 |  |
  | Lab ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1 |  |
  | Preparation protocol DOI <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The DOI for the protocols.io page that details the assay or the procedures used for sample procurement and preparation. For example, in the case of an imaging assay, the protocol may start with tissue section staining and end with the generation of an OME-TIFF file. The documented protocol should also include any image processing steps involved in producing the final OME-TIFF. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1 |  |
  | Dataset type <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific type of dataset being produced. Example: RNAseq | ```HiFi-Slide``` ```SNARE-seq2``` ```COMET``` ```Visium (no probes)``` ```DESI``` ```Confocal``` ```Stereo-seq``` ```Visium (with probes)``` ```Molecular Cartography``` ```Virtual Histology``` ```DBiT-seq``` ```Seq-Scope``` ```CosMx Transcriptomics``` ```CyCIF``` ```Light Sheet``` ```iCLAP``` ```seqFISH``` ```ATACseq``` ```CosMx Proteomics``` ```Singular Genomics G4X``` ```Visium HD``` ```MERFISH``` ```10X Multiome``` ```4i``` ```PhenoCycler``` ```Second Harmonic Generation (SHG)``` ```Thick section Multiphoton MxIF``` ```CyTOF``` ```Olink``` ```MIBI``` ```Auto-fluorescence``` ```FACS``` ```Xenium``` ```SIMS``` ```Cell DIVE``` ```CODEX``` ```GeoMx (NGS)``` ```MUSIC``` ```Pixel-seqV2``` ```MALDI``` ```2D Imaging Mass Cytometry``` ```Histology``` ```Enhanced Stimulated Raman Spectroscopy (SRS)``` ```DART-FISH``` ```Resolve``` ```RNAseq``` ```LC-MS``` ```nanoSPLITS``` ```GeoMx (nCounter)``` ```Raman Imaging``` ```RNAseq (with probes)``` ```MS Lipidomics``` ```STARmap``` ```MPLEx``` |
  | Analyte class <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The analyte class which is the target molecule that the assay is measuring. Example: DNA | ```DNA + RNA``` ```Nucleic acid + protein``` ```Chromatin``` ```Lipid + metabolite + protein``` ```RNA + protein``` ```RNA``` ```Metabolite``` ```Unsaturated lipid``` ```Lipid + metabolite``` ```Saturated lipid``` ```Lipid``` ```Protein``` ```Fluorochrome``` ```Collagen``` ```DNA``` ```Peptide``` ```Polysaccharide``` ```Endogenous fluorophore``` |
  | Is targeted? <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i> | Indicates whether a specific molecule or set of molecules is targeted for detection or measurement by the assay. Example: Yes | ```Yes``` ```No``` |
  | Acquisition instrument vendor <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The company that manufactures or supplies the acquisition instrument. An acquisition instrument is a device equipped with signal detection hardware and signal processing software. It captures signals produced by assays, such as variations in light intensity or color, or signals corresponding to molecular mass. If the instrument was custom-built or developed internally, enter "In-House". Example: Illumina | ```BGI Genomics``` ```Cytiva``` ```Thermo Fisher Scientific``` ```Zeiss Microscopy``` ```Complete Genomics``` ```3DHISTECH``` ```GE Healthcare``` ```Leica Microsystems``` ```Akoya Biosciences``` ```NanoString``` ```Element Biosciences``` ```Andor``` ```Huron Digital Pathology``` ```Illumina``` ```Ionpath``` ```Waters``` ```In-House``` ```Resolve Biosciences``` ```Singular Genomics``` ```Vizgen``` ```Standard BioTools (Fluidigm)``` ```Sciex``` ```Bruker``` ```Evident Scientific (Olympus)``` ```Keyence``` ```Leica Biosystems``` ```Revvity``` ```Cytek Biosciences``` ```10x Genomics``` ```Microscopes International``` ```Hamamatsu``` ```Motic``` |
  | Acquisition instrument model <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific model of the acquisition instrument, as manufacturers often offer various versions with differing features or sensitivities. These differences may be relevant to the processing or interpretation of the data. If the instrument was custom-built or developed internally, enter "In-House". If the model is unknown, enter "Unknown". Example: HiSeq 4000 | ```SCN400``` ```STELLARIS 5``` ```BZ-X710``` ```Pannoramic MIDI II Digital Scanner``` ```Not applicable``` ```MoticEasyScan One``` ```EVOS M7000``` ```NovaSeq X``` ```NanoZoomer 2.0-HT``` ```timsTOF Ultra 2``` ```Lightsheet 7``` ```Phenocycler-Fusion 1.0``` ```DNBSEQ-T7``` ```timsTOF Pro``` ```Unknown``` ```AVITI``` ```DMi8``` ```Opera Phenix Plus HCS``` ```timsTOF Pro 2``` ```Q Exactive UHMR``` ```Q Exactive``` ```timsTOF SCP``` ```Zyla 4.2 sCMOS``` ```Helios``` ```uScopeHXII-20``` ```Orbitrap Fusion Tribrid``` ```Custom: Multiphoton``` ```QTRAP 5500``` ```timsTOF Ultra``` ```BZ-X800``` ```CyTOF 2``` ```G4X Spatial Sequencer``` ```NextSeq 500``` ```NanoZoomer S360``` ```Hyperion Imaging System``` ```NovaSeq X Plus``` ```CyTOF XT``` ```NanoZoomer-SQ``` ```NextSeq 550``` ```Axio Zoom.V16``` ```Digital Spatial Profiler``` ```timsTOF FleX``` ```timsTOF FleX MALDI-2``` ```NanoZoomer S210``` ```BZ-X810``` ```Axio Observer 7``` ```Cytek Northern Lights``` ```Opera Phenix HCS``` ```Zeiss LightSheet Z.1``` ```IN Cell Analyzer 2200``` ```timsTOF HT``` ```PhenoImager Fusion``` ```DM6 B``` ```Phenocycler-Fusion 2.0``` ```Aperio CS2``` ```Orbitrap Fusion Lumos Tribrid``` ```Resolve Biosciences Molecular Cartography``` ```MALDI timsTOF Flex Prototype``` ```TissueScope LE Slide Scanner``` ```VS200 Slide Scanner``` ```Axio Observer 5``` ```Axio Observer 3``` ```HiSeq 2500``` ```Orbitrap Eclipse Tribrid``` ```Cell DIVE``` ```MERSCOPE``` ```NextSeq 2000``` ```NovaSeq 6000``` ```In-House``` ```HiSeq 4000``` ```solariX``` ```Panoramic 150 Digital Scanner``` ```Aperio AT2``` ```MIBIscope``` ```SYNAPT G2-Si``` ```Biomark HD``` ```NanoZoomer S60``` ```CosMx Spatial Molecular Imager``` ```MERSCOPE Ultra``` ```Axio Scan.Z1``` ```Juno System``` ```Q Exactive HF``` ```Xenium Analyzer``` |
  | Source storage duration value <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time the sample was stored prior to processing it. For assays performed on tissue sections, this refers to how long the tissue section (e.g., slide) was stored before the assay began (e.g., imaging). For assays performed on suspensions, such as sequencing, it refers to how long the suspension was stored before library construction started. Example: 12 |  |
  | Source storage duration unit <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the source storage duration value. Example: hour | ```hour``` ```month``` ```year``` ```day``` ```minute``` |
  | Time since acquisition instrument calibration value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time since the acquisition instrument was last serviced or calibrated. This provides a metric for assessing drift in data capture. Example: 10 |  |
  | Time since acquisition instrument calibration unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the time since acquisition instrument calibration value. Example: month | ```month``` ```year``` ```day``` |
  | Contributors path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The name of the file containing the ORCID IDs for all contributors to this dataset. Example: ./contributors.csv |  |
  | Data path <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The top-level directory containing the raw and/or processed data. For a single dataset upload, this might be represented as ".", whereas for a data upload containing multiple datasets, this would be the directory name for the respective dataset. For example, if the data is within a directory named "TEST001-RK", use the syntax "./TEST001-RK" for this field. If there are multiple directory levels, use the format "./TEST001-RK/Run1/Pass2", where "Pass2" is the subdirectory where the single dataset's data is stored. This is an internal metadata field used solely for data ingestion. Example: ./TEST001-RK |  |
  | MS ionization technique <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The ionization technique used in imaging mass spectrometry, which refers to the method employed to probe the sample. Example: MALDI | ```LDI``` ```SIMS-H20``` ```HESI``` ```LA``` ```nanoDESI``` ```MALDI``` ```DESI``` ```SIMS-C60``` ```ESI``` ```MALDI-2``` ```nESI``` |
  | MS scan mode <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The mode of mass spectrometry (MS) scanning, which refers to the number of steps involved in the separation of fragments during the analysis. Example: MS1 | ```MS1``` ```MS3``` ```MS2``` |
  | Mass analysis polarity <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The polarity mode used in mass analysis, indicating whether positive or negative ion modes are employed. Example: Positive ion mode | ```Negative ion mode``` ```Positive ion mode``` ```Negative and positive ion mode``` |
  | Mass-to-charge range low value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The low value of the scanned mass-to-charge range for MS1. This value is unitless. Example: 100 |  |
  | Mass-to-charge range high value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The high value of the scanned mass-to-charge range, for MS1. (unitless) |  |
  | Mass resolving power | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The mass resolving power, denoted as m/∆m, where ∆m is defined as the full width at half-maximum (FWHM) for a given peak with a specified mass-to-charge ratio (m/z). This measurement is unitless. Example: 60000 |  |
  | Mass-to-charge resolving power | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The peak mass-to-charge ratio (m/z) used to calculate the resolving power. Example: 400.2 |  |
  | Ion mobility | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The specific technology employed for ion mobility spectrometry. Available technologies include Traveling Wave Ion Mobility Spectrometry (TWIMS), Trapped Ion Mobility Spectrometry (TIMS), High Field Asymmetric Waveform Ion Mobility Spectrometry (FAIMS), Drift Tube Ion Mobility Spectrometry (DTIMS), Structures for Lossless Ion Manipulations (SLIM), and cyclic Ion Mobility Spectrometry (cIMS). Example: TIMS | ```cIMS``` ```TWIMS``` ```DTIMS``` ```SLIM``` ```TIMS``` ```FAIMS``` |
  | Data collection mode | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The mode of data collection used in tandem MS assays, which can include options such as Data-dependent acquisition (DDA), Data-independent acquisition (DIA), multiple reaction monitoring (SRM), or parallel reaction monitoring (PRM). Example: PRM | ```DDA``` ```PRM``` ```DIA``` ```SRM``` |
  | Label name | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The name or identifier of the chemical label used on this sample if labeling was applied. This is typically required for multiplexed experiments using techniques like Tandem Mass Tag (TMT). If sample was not labeled, this field may be left blank. Example: TMT126 |  |
  | LC instrument vendor | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The company that manufactures the instrument used for liquid chromatography. If the instrument was custom-built or developed internally, enter "In-House". Example: Bruker | ```In-House``` ```Evosep``` ```Shimadzu``` ```Thermo Fisher Scientific``` ```Agilent Technologies``` ```Sciex``` ```Bruker``` ```Waters``` |
  | LC instrument model | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The model number or name of the instrument used for liquid chromatography. Example: Bruker Elute LC-MS |  |
  | LC column vendor | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The manufacturer of the liquid chromatography column used, unless a self-packed or pulled tip capillary is employed. If the column was custom-made or developed internally, enter "In-House". Example: Bruker | ```In-House``` ```IonOpticks``` ```Evosep``` ```Thermo Fisher Scientific``` ```Agilent Technologies``` ```Millipore``` ```Bruker``` ```Waters``` |
  | LC column model | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The model number or name of the liquid chromatography column used. If a custom self-packed, pulled tip capillary is utilized, enter "Pulled tip capillary". Example: Thermo Scientific Vanquish UHPLC |  |
  | LC resin | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The details of the resin used in liquid chromatography, including information about the vendor, particle size, and pore size. Example: Thermo Fisher Scientific, Acclaim PepMap 100 C18, 3 µm, 100 Å |  |
  | LC column length value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | Liquid chromatography column length. |  |
  | LC column length unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | Units for liquid chromatography column length (typically cm). | ```mm``` ```um``` ```cm``` |
  | LC temperature value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The temperature at which the liquid chromatography (LC) process is conducted. Example: 40 |  |
  | LC temperature unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> |  | ```celsius``` |
  | LC inner diameter value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | Liquid chromatography column inner diameter. |  |
  | LC inner diameter unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurment for the LC inner diameter value. If the diameter is not specified, this field may be left blank. Example: um | ```mm``` ```um``` ```cm``` |
  | LC flow rate value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | Value of flow rate. |  |
  | LC flow rate unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | Units of flow rate. | ```mL/min``` ```nL/min``` |
  | LC gradient value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The liquid chromatography (LC) gradient used in the assay. Example: 120 |  |
  | LC gradient unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | Unit for liquid chromatography gradient | ```minute``` |
  | LC mobile phase A | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | Composition of mobile phase A. |  |
  | LC mobile phase B | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> |  |  |
  | Spatial sampling technique | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> |  | ```microPOTS``` ```nanoSPLITS``` ```LESA``` ```microLESA``` ```nanoPOTS``` ```LCM``` |
  | Spatial sampling target | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The cell type or functional tissue unit (FTU) that is the focus of the spatial profiling experiment. If the data are generated in imaging mode without targeting a specific structure, this field may be left blank. Example: Proximal tubule epithelial cell |  |
  | Spatial sampling type | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The type of spatial targeting used in the analysis. Spatial profiling focuses on selected tissue regions without necessarily producing images, while spatial imaging captures data across a regular grid of pixels, enabling visualization as ion intensity heat maps—also referred to as molecular images. Leave this field blank if the data originate from bulk (non-spatial) analysis. Example: Imaging | ```Profiling``` ```Imaging``` |
  | Analysis protocol DOI <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A DOI to a protocols.io protocol describing the software and database(s) used to process the raw data. Example: https://dx.doi.org/10.17504/protocols.io.bsu5ney6 |  |
  | Metadata schema ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique string identifier for the metadata specification version, which is easily interpretable by computers for purposes of data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 |  |
  
definitions: 
|-
  | Pattern | Required? | Description |
  |--|--|--|
  | extras/ | ✓ | Folder for general lab-specific files related to the dataset. |
  | raw/ | ✓ | This is a directory containing raw data. |
  | raw/mplex/ |  | All relevant raw files for MPLeX. |
  | lab_processed/ | ✓ | Experiment files that were processed by the lab generating the data. |
  | lab_processed/mplex/ |  | Experiment files that were processed by the lab generating the data exclusive to MPLeX. |

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
