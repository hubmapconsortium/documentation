---
layout: page
---
## Overview
This document details data levels, metadata fields, file structure, QA/QC thresholds, and data processing for bulk and single-cell ATAC sequencing assays.

| Assay | Attributes | Description |
|-------|------------|-------------|
| [AF (Autofluorescence)](https://docs.hubmapconsortium.org/assays/af) | [attributes](AutoFluorescence)  |   Exploits endogenous fluorescence in a biological tissue to capture an image. The image can then be used to integrate other images from multiple modalities and to align tissues within a 3D experiment. |
| [ATACseq](https://docs.hubmapconsortium.org/assays/atacseq) | [attributes](ATACseq)  |  Identifies accessible DNA regions by probing open chromatin with hyperactive mutant Tn5 Transposase that inserts sequencing adapters into open regions of the genome. |
| [scATACseq](https://docs.hubmapconsortium.org/assays/atacseq) | [attributes](ATACseq)  | |
| [bulkATACseq](https://docs.hubmapconsortium.org/assays/atacseq) | [attributes](ATACseq) |  Bulk ATAC-Seq |
| Body CT | [attributes*](https://docs.google.com/spreadsheets/d/114DmeiACGQzA8C5ZY3mWh-338XNe7Zy7/edit)  | |
| [bulkRNAseq](https://docs.hubmapconsortium.org/assays/rnaseq) | [attributes](RNAseq)  |  Bulk RNA sequencing |
| [CODEX (Not PhenoCycler)](https://docs.hubmapconsortium.org/assays/codex) | [attributes](CODEX)  |  Strategy for generating highly multiplexed images of fluorescently-labeled antigens. |
| Confocal | [attributes](Confocal)  | |
| DESI | [attributes](DESI)  | |
| Enhanced SRS | [attributes](EnhancedSRS)  | |
| HiFi | [attributes](HiFi-Slide)  | |
| Histology | [attributes](Histology)  | |
| [2D IMC (Imaging Mass Cytometry)](https://docs.hubmapconsortium.org/assays/imc) | [attributes](IMC-2D)  |Combines standard immunohistochemistry with CyTOF mass cytometry to resolve the cellular localization of up to 40 proteins in a tissue sample. |
| [3D IMC  (Imaging Mass Cytometry)](https://docs.hubmapconsortium.org/assays/imc)| attributes*  |Combines standard immunohistochemistry with CyTOF mass cytometry to resolve the cellular localization of up to 40 proteins in a tissue sample. |
| [LC-MS](https://docs.hubmapconsortium.org/assays/lcms) | [attributes](LC-MS)  |  Coupling of liquid chromatography (LC) to mass spectrometry (MS) |
| Light Sheet | [attributes](LightSheet)  | |
| [MALDI-IMS (neg and pos modes - Matrix Assisted Laser Desorption Ionization Imaging Mass Spectrometry)](https://docs.hubmapconsortium.org/metadata/Assay_Types.html#MALDI-Imaging) | [attributes](MALDI)  |  Matrix-assisted laser desorption/ionization (MALDI) imaging mass spectrometry (IMS) combines the sensitivity and molecular specificity of MS with the spatial fidelity of classical microscopy. |
| MIBI | [attributes](MIBI)  |  |
| MERFISH | [attributes](MERFISH)  |  |
| Micro CT | [attributes*](https://docs.google.com/spreadsheets/d/114DmeiACGQzA8C5ZY3mWh-338XNe7Zy7/edit?gid=1304455053#gid=1304455053)  | |
| Molecular Cartography | [attributes*](https://docs.google.com/spreadsheets/d/1kd1UQ2il-eW-MTM4iEotyAxa8M_hcwn8yQJTU_II-F8/edit?gid=1856663792#gid=1856663792)  | |
| MRI | [attributes*](https://docs.google.com/spreadsheets/d/114DmeiACGQzA8C5ZY3mWh-338XNe7Zy7/edit?gid=1304455053#gid=1304455053)  | |
| MUSIC | [attributes](MUSIC)  | |
| NanoDESI | [attributes**](DESI)  | |
| OCT | [attributes*](https://docs.google.com/spreadsheets/d/114DmeiACGQzA8C5ZY3mWh-338XNe7Zy7/edit?gid=1304455053#gid=1304455053)  | |
| PhenoCycler | [attributes](PhenoCycler)  | |
| [RNAseq](https://docs.hubmapconsortium.org/assays/rnaseq) | [attributes](RNAseq)  | While bulk RNAseq elucidates the average gene expression profile in cells comprising a tissue sample, single-cell RNAseq, employs per-cell and per-molecule barcoding to enable single-cell resolution of the gene expression profile.|
| RNAseq With Probes | [attributes](RNAseqWithProbes)  | |
| scRNAseq | attributes  | |
| Second Harmonic Generation | [attributes](SecondHarmonicGeneration)  | |
| [SeqFISH](https://docs.hubmapconsortium.org/assays/seqfish) | attributes  |  seqFISH technology allows in situ imaging of multiple mRNAs using barcoding and fluorophore-labelled barcode readout-probes.  |
| SIMS | [attributes](SIMS)  | |
| Slide-seq | attributes  | |
| SnareSeq2 | [attributes](SnareSeq2)  | |
| Thick Section Multiphoton MxIF | [attributes](ThickSectionMultiphotonMxIF)  | |
| Ultrasound | [attributes*](https://docs.google.com/spreadsheets/d/114DmeiACGQzA8C5ZY3mWh-338XNe7Zy7/edit?gid=1304455053#gid=1304455053)  | |
| Visium No Probes | [attributes](VisiumNoProbes)  | |
| Visium With Probes | [attributes](VisiumWithProbes)  | |