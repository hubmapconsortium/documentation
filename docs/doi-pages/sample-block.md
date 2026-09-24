---
layout: doi-landing-page
title: Metadata Reporting Standards - Block
spec_name: Sample Block
descriptive_version: 2.1
structural_version: 
doi: 10.35079/HBM447.MXVB.286
download_href: "https://github.com/hubmapconsortium/ingest-validation-tools/raw/refs/heads/main/docs/sample-block/current/doi-object.zip"
md5_hash: 8448e5e15ae0d12747bd3c2b5fb469d1
published: September 15, 2026
subjects: 
summary: A block is a piece of tissue typically sized to fit into a tissue cassette or freezer mold, prepared for long-term storage or downstream sectioning. Tissue blocking is generally performed by hand with a scalpel, producing a relatively thick specimen with a typical Z-plane depth of 0.5–1 cm; organ pieces and biopsies are both classified as blocks. A block serves as the starting material from which thinner sections are cut for downstream assays.
latest_href: "https://hubmapconsortium.github.io/ingest-validation-tools/sample-block/current"
harmonized_href: "https://docs.hubmapconsortium.org/metadata/sample/sample-block"
schema_doc_href: "https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2F3e98cee6-d3fb-467b-8d4e-9ba7ee49eeff"
validator_href: "https://metadatavalidator.metadatacenter.org"
datasets_href: "https://portal.hubmapconsortium.org/search/samples"
help_href: /doi-pages-help/
datasets_text: The HuBMAP Data Portal is an open platform to discover, visualize, and download standardized healthy single-cell and spatial tissue data.
citation_text: Fisher SA, Hardi J, Morgan R, Nordgren E, Kant PM, Honick B, Rosario J, O'Connor MJ, Turner ML, DCWG Members, Gehlenborg N, Blood PD, Silverstein JC, Musen MA. 2026. The HuBMAP Framework for Advancing Data FAIRness. submitted. https://doi.org/10.64898/2026.06.01.728946
contributors_intro: Below is the information for the individuals who contributed to the HuBMAP and SenNet metadata reporting standards.
contributors_note: For questions about this standard, email <a href="mailto:help@hubmapconsortium.org">HuBMAP Helpdesk</a>. You can alternatively reach out to the individuals listed below, either via the email address listed in the table or via contact information provided on their ORCID profile page.

example_tree: 

schema_items: 
|-
  | Attribute | Type | Description | Allowable Values |
  |--------|----|--------------|-------------|
  | Source ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique identifier from HuBMAP or SenNet for the source (parent data) from which the sample was derived. Example: HBM122.EFGH.789 |  |
  | Sample ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique HuBMAP or SenNet identifier assigned to the sample by the ingest portal. Example: HBM743.CKJW.876 |  |
  | Lab ID | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | A locally assigned identifier provided by the data provider for the dataset. It is used to reference an external metadata record that may be maintained independently, enabling traceability and supporting provenance tracking. Example: Visium_9OLC_A4_S1 |  |
  | Preparation protocol DOI <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The DOI for the protocols.io page that details the assay or the procedures used for sample procurement and preparation. For example, in the case of an imaging assay, the protocol may start with tissue section staining and end with the generation of an OME-TIFF file. The documented protocol should also include any image processing steps involved in producing the final OME-TIFF. Example: https://dx.doi.org/10.17504/protocols.io.eq2lyno9qvx9/v1 |  |
  | Source storage duration value <span class="requiredMark">*</span> | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The length of time the sample was stored prior to processing it. For assays performed on tissue sections, this refers to how long the tissue section (e.g., slide) was stored before the assay began (e.g., imaging). For assays performed on suspensions, such as sequencing, it refers to how long the suspension was stored before library construction started. Example: 12 |  |
  | Source storage duration unit <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement used to specify the source storage duration value. Example: hour | ```hour``` ```month``` ```year``` ```day``` ```minute``` |
  | Tissue weight value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The weight of a tissue block or the piece of tissue used in a suspension. This information is crucial for calculating the percentage of the parent block that was utilized in the suspension preparation. If the weight is not applicable or unknown, this field may be left blank. Example: 100 |  |
  | Tissue weight unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the tissue weight value. If no tissue weight is specified, this field may be left blank. Example: g | ```ug``` ```g``` ```mg``` ```kg``` |
  | Volume value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The volume of the object in question. Example: 102 |  |
  | Volume unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the volume value. If no volume measurement is specified, this field may be left blank. Example: mm^3 | ```cm^3``` ```mm^3``` ```um^3``` ```ml``` |
  | Pathology distance value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The distance from which the surgical sample was obtained relative to the pathology site. If this information is not applicable, this field may be left blank. Example: 100 |  |
  | Pathology distance unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the pathology distance value. If no distance measurement is applicable, this field may be left blank. Example: mm | ```mm``` ```cm``` |
  | Preparation medium <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The medium used during the sample preparation process. If no specific medium was utilized, enter "None". If medium was not recorded, enter "Unknown". Example: Fresh frozen CMC | ```HTK Solution``` ```NBF (Neutral Buffered Formalin)``` ```Allprotect tissue reagent (ALL)``` ```CLARITY hydrogel``` ```Trumps fixative``` ```1X fixation & permeabilization buffer``` ```Inflated (OCT)``` ```DMEM``` ```Perfadex Plus``` ```PFA (Paraformaldehyde)``` ```Fixed frozen OCT (Formalin, sucrose protected)``` ```Unknown``` ```Fresh frozen OCT``` ```Alpha-MEM``` ```2% PFA/2.5% Glutaraldehyde``` ```Bouin's``` ```Methanol``` ```PAXgene tissue kit (PXT)``` ```PBS``` ```Ethanol``` ```Modified Davidson's Fixative``` ```HPMC-PVP``` ```Inflated (Agarose)``` ```PLP (Periodate-Lysine-Paraformaldehyde)``` ```UW Solution``` ```MACS tissue storage solution``` ```Fresh frozen CMC``` ```Fresh frozen gelatin``` ```Growth media``` ```RNAlater``` ```Biops buffer``` ```Fixed frozen OCT (Cytofix/Cytoperm)``` ```None``` ```Fixed frozen OCT (PFA, sucrose protected)``` ```Lysis buffer``` |
  | Preparation condition <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The condition under which the sample preparation took place, such as whether the sample was placed on dry ice during the process. If preparation condition was not recorded, enter "Unknown". Example: Frozen on dry ice | ```Frozen in liquid nitrogen vapor``` ```Stored in ambient temperature``` ```Frozen on ice``` ```Frozen in liquid nitrogen``` ```Unknown``` ```Frozen at -20 degrees celsius``` ```Frozen on dry ice``` ```Stored in refrigerator``` ```Stored on wet ice``` |
  | Processing time value | <i class="fa-solid fa-hashtag" title="Numeric" aria-label="Numeric"></i> | The duration for which the tissue was handled prior to its initial preservation. Example: 120 |  |
  | Processing time unit | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The unit of measurement for the processing time value. If processing time is not specified, this field may be left blank. Example: minute | ```hour``` ```day``` ```minute``` |
  | Storage medium <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The medium used to preserve the sample. If no specific medium was utilized, enter "None". If medium was not recorded, enter "Unknown". Example: FFPE (Paraffin embedded) | ```Water``` ```OCT``` ```NBF (Neutral Buffered Formalin)``` ```Allprotect tissue reagent (ALL)``` ```DMSO (no serum)``` ```PFA (Paraformaldehyde)``` ```Unknown``` ```Gelatin``` ```DMSO (serum)``` ```CMC``` ```2% PFA/2.5% Glutaraldehyde``` ```Methanol``` ```PAXgene tissue kit (PXT)``` ```PBS``` ```1X quench buffer``` ```Ethanol``` ```Formic acid in water``` ```HPMC-PVP``` ```MACS tissue storage solution``` ```Tris-EDTA``` ```Concentrated quench buffer``` ```Cryo-EM``` ```RNAlater``` ```FFPE (Paraffin embedded)``` ```None``` |
  | Storage method <span class="requiredMark">*</span> | <i class="fa-solid fa-circle-nodes" title="Allowable Value" aria-label="Allowable Value"></i> | The method used to store the sample after preparation and prior to performing the assay. If no specific storage method was utilized, enter "None". If storage method was not recorded, enter "Unknown". Example: Frozen in dry ice | ```Frozen in liquid nitrogen vapor``` ```Stored in ambient temperature``` ```Frozen on ice``` ```Frozen in liquid nitrogen``` ```Unknown``` ```Stored in desiccator``` ```Incubated at 37 degrees celsius``` ```Frozen at -80 degrees celsius``` ```Frozen at -20 degrees celsius``` ```Frozen on dry ice``` ```Stored in refrigerator``` ```None``` |
  | Quality criteria | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The quality criteria used to assess the sample, which may include metrics such as RIN (e.g., RIN: 8.7) or visual inspection parameters for suspensions prior to cell lysis. These criteria can be captured at a high level with general terms like "OK" or "not OK" or with more specific descriptors such as "debris" "clump" or "low clump". Example: RIN: 8.7, low clump, no visible debris |  |
  | Histological report | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The key variables in the histopathological report that are crucial for assessing the tissue, including the absence of necrosis, comments on tissue composition, descriptions of significant pathology, and high-level assessments of inflammation or fibrosis. Example: No necrosis observed; tissue composed predominantly of hepatocytes with mild portal inflammation and minimal fibrosis |  |
  | Notes | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | Miscellaneous details about the sample that are not captured in the existing metadata fields. Example: Sample was stored at 4°C for 48 hours prior to processing due to equipment maintenance delay |  |
  | Metadata schema ID <span class="requiredMark">*</span> | <i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i> | The unique string identifier for the metadata specification version, which is easily interpretable by computers for purposes of data validation and processing. Example: 22bc762a-5020-419d-b170-24253ed9e8d9 |  |

definitions: 
    
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
