---
layout: default
---

## EPIC Example Type 1
### Segmentation Mask: <mark>Published</mark>

<mark>This is a published specification, which has been tested, is stable, and can be used to submit relevant EPIC datasets.</mark>
Segmentation of images is performed manually or by an algorithm that predicts edges of structures. Structures may be nuclear membrane, cell membranes, or larger structures such as tubules. Segmentation mask EPICs work with 2D and 3D images (see Fig 2). 

A 3D EPIC will include:
- 3D OME-TIFF
- Z coordinates for the object centroids
- 3D mesh file (optional)

If a 3D segmentation mask is based on a 3D image that’s been constructed from 2D serial sections, the “parent dataset” must be a 3D Reconstruction EPIC (see 3D Reconstruction below).

- [Published specification](https://hubmapconsortium.github.io/ingest-validation-tools/segmentation-mask/current/)
- [Documentation](https://docs.google.com/document/d/1LgQ509UOoZsY-sZO1cBFtqxWbo3jLGyCVy-_mssBVMw/edit?tab=t.0#heading=h.1u82i4axggee)

![EPICs Figure 2](EPICs-Fig2.png)

**Figure 2:** Segmentation mask EPICs can be derived from 2D or 3D images.
