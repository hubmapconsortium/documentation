---
layout: page
---
# HuBMAP Antibody Validation Report TSV Structure
With each submission of AVR documents associated header/metadata information must be include for each AVR document. This information is provided as a .tsv file.  It is recommended to start with the blank (header only) [template tsv file](/avr/avr-template-v2.tsv), use Excel or other spreadsheet to enter the data, then export as a comma separated value (tsv) file.  An example [example AVR tsv file](/avr/example-avrs-v2.tsv) is also available. All columns in the tsv file are required, with the definitions of the columns here:


| tsv column               | description                                                                    |
|--------------------------|--------------------------------------------------------------------------------|
| uniprot_accession_number | This can typically be found on the vendor’s website, but can also be found by searching <a href="https://www.uniprot.org" target="_blank">UniProt.org</a> directly. Please note that different species have different UniProt accession numbers for the same protein. If your data was acquired using human tissue, be sure you are choosing the UniProt accession for the human protein. |
|hgnc_id                   | Gene identification number from Human Gene Ontology Nomenclature Committee (HGNC) https://www.genenames.org/ encoding the target protein. HGNC:####|
|target_symbol               | This is the symbol of the protein that the antibody is targeting. Please list the UniProt protein name. This may be different from the common name for the protein. |
|isotype                   | Describes the antibody isotype. Please write out any symbols. (e.g. IgG, IgG1, IgG1 kappa)|
| host                     | This is the species that was used to generate the antibody (e.g. mouse, rabbit, etc). |
|clonality| This will be either Monoclonal or Polyclonal.|
|clone_id   | A unique identifier for a laboratory-generated antibody produced either by hybridoma cells or through recombinant DNA technology.|
|vendor                   | This is the company that sells the antibody. |
|catalog_number           | Provides catalog number from vendor for the source of the antibody.|
|lot_number               | This is the lot number for the antibody that was validated. |
|recombinant              | Simple Yes or No if the antibody was recombinant. Recombinant antibodies (rAbs) are monoclonal antibodies which are generated in vitro using synthetic genes.|
|concentration_value      | Provides a recommended usage in standardized units (μg/mL). Numeric only (units standardized) If providing dilution instead, leave this field blank. Required field if AVR is part of an Organ Mapping Antibody Panel (OMAP). |
|dilution_factor                 | Provides a recommended dilution factor. If providing a concentration instead, leave this field blank. (e.g. for 1:100 dilution put "100" for the dilution factor): Required field if AVR is part of an Organ Mapping Antibody Panel (OMAP).|
|conjugate                | Specifies addition to the antibody (e.g., fluorophore, heavy metal, oligonucleotide) enabling detection, if applicable. If no conjugate, leave blank.|
|rrid                     | This can usually be found on the vendor’s website, but can also be found by searching at <a href="https://scicrunch.org/resources/Antibodies/search" target="_blank">https://scicrunch.org/resources/Antibodies/search</a> or <a href="https://antibodyregistry.org" target="_blank">htps://antibodyregistry.org</a>. If there is no RRID, you can create one here: <a href="https://scicrunch.org/resources/about/resource" target="_blank">https://scicrunch.org/resources/about/resource</a>. |
|method                   | This is the downstream assay that was used (e.g. CODEX, MIBI, etc). |
|tissue_preservation      | Preservation technique used. If fixative other than formalin, indicate the percentage of fixative indicated (e.g., 1% or 4%). Use a common abbreviation format (e.g., FFPE for formalin fixed paraffin embedded).| 
|protocol_doi            | All validation pipelines need an accompanying protocol on protocols.io. or another open protocol repository. Details the protocol used to validate the antibody, including positive and negative controls and example images. If the validation procedure is the same for all antibodies your which lab tests, then a single protocol can be used. If validation procedures differ, then different methods will need different validation protocols. |
|manuscript_doi | DOI for the published manuscript that details the use of the antibody and the associated OMAP.|
| author_orcids            | This is needed for whomever is submitting the validation data. This will be used to differentiate the same antibodies being tested across different groups. Identifies the individuals who validated the antibody used in the assay; Format ####-####-####-#### (the last digit may be X) See https://info.orcid.org/researchers/ |
| vendor_affiliation      | Identities whether the antibody validation was done by commercial entity (antibody vendor or multiplexed technology provider). Vendor name. If not applicable, please leave this field blank. (e.g. Cell Signaling Technology, Bio-Techne, Abcam, Biolegend,  Akoya Biosciences, Leica Microsystems)|
| organ          | This is the tissue that was used to acquire the validation data. This should be the same tissue that was used in the downstream assay. |
|organ_uberon_id              | Uberon multi-species anatomy ontology ID for organ (e.g. for kidney UBERON:0002113). Accessible via the Ontology look-up service (OLS): https://www.ebi.ac.uk/ols/search?ontology=uberon |
| antigen_retrieval        | If applicable, indicate general conditions under which  antigen retrieval was performed. Additional details should be available in the referenced protocol (see protocol_doi field).Required format: pH values; if multiple, separate by commas. |
| avr_pdf_filename         | The name of the corresponding AVR document in PDF format that this row of metadata is associated with.  This name must match the file uploaded in the Antibody PDF section of the AVR upload screen during submission. An example AVR document can be found <a href="/avr/example-avr-v2.pdf" target="_blank">here</a>.|
| omap_id                  | Unique identifier assigned to Organ Mapping Antibody Panel (OMAP) at time of publication. OMAP with number based on date created (e.g. OMAP-1, OMAP-2) (optional field)|
| cycle_number             | Identifies the cycle number in which an antibody was either applied to the tissue or, in the case of CODEX,visualized with a fluorescent reporter. For non-cyclic methods use 1 for all cycles. Required field if AVR is part of an Organ Mapping Antibody Panel (OMAP).|
|fluorescent_reporter      | For indirect visualization (e.g., oligo-conjugated antibodies), define the fluorescent reporter utilized in the corresponding cycle. For metal or fluorophore-conjugated antibodies, please leave blank. Required field if AVR is part of an Organ Mapping Antibody Panel (OMAP).|