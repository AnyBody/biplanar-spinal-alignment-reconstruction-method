<div align="center">
  <h1>Biplanar Spinal Alignment Reconstruction Method</h1>
  <p>
    AnyBody plugin for high fidelity reconstructing of 3D spinal alignment from biplanar radiographs.
    <br />
    <!-- Optional: link to preprint/paper -->
    <a href="https://doi.org/XX.XXXX/your-doi-here"><strong>Caimi et Rieger et al. (202X)</strong></a>
  </p>
</div>


<p align="center">
  <img src="docs/images/Scenario overview GitHub.jpg" width="90%">
</p>



---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Methods Overview](#methods-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Input Data](#input-data)
- [Outputs](#outputs)
- [Validation & Limitations](#validation--limitations)
- [How to Cite](#how-to-cite)
- [Contributions](#contributions)
- [Contact](#contact)

---

## About

This repository provides an AnyBody-based implementation of a spinal alignment reconstruction method. Using vertebral landmark annotations extracted from single- or biplanar radiographs, the model reconstructs the 3D spinal alignment, including vertebral centroid positions and segmental orientations.

The implementation provides an improved posture-reconstruction approach for researchers evaluating spine biomechanics through Musculoskeletal Modeling (MSK) based on single- or biplanar radiographs. It serves as a supplementary module to the AnyBody Modeling System and enables users to:
- Calibrate 3D spinal alignment models in AnyBody from sagittal or coronal radiographic projections
- Integrate subject-specific spinal alignments into downstream musculoskeletal simulations

<p align="center">
  <img src="docs/images/Figure 01 V2.jpg" width="60%">
</p>

---

## Features

- AnyBody Modeling System implementation (version 8.0+)
- Biplanar (coronal + sagittal) landmark-based posture reconstruction
- Automatic computation of global and segmental alignment parameters
- Example datasets and scripts for running the full pipeline

---

## Methods Overview

High-level pipeline:

1. **Input**: Extracted landmarks of biplanar radiographs in sagittal and (optionally) coronal planes  
2. **Anatomical Landmark definition**: 2D coordinates of vertebral corner nodes (T1-L5), sacral endolate and bi-femoral head axis, as well as spinopelvic parameters Pelvic Incidence (PI), Pelvic Tilt (PT), Sacral Slope (SS) and Pelvic Obliquity (PO)
3. **Inputs**: Vertebral inclinations and vertebral centroids coordinates, derrived from Anatomical Landmarks in the sagittal and coronal plane
4. **3D reconstruction**: Posture reconstruction drivers that integrate the degrees of freedom in the model setup
5. **Alignment metrics**: Computation of sagittal and coronal angles, offsets, and global alignment parameters  

---

## Installation

### Requirements

- **AnyBody Modeling System** version 8.0 or higher

### Get the repository

```bash
git clone https://github.com/USERNAME/biplanar-spinal-alignment.git
cd biplanar-spinal-alignment
```

--- 

## Usage

toDo: Alice model flags

---

## Installation

redundant?

---

## Repository structure 

```
biplanar-spinal-alignment/
├─ Application/
│  ├─ Main.any             # Entry point for the AnyBody model
├─ Model/
│  ├─ Segments/            # Vertebra/pelvis segment definitions
│  ├─ Drivers/             # Kinematic drivers for the reconstruction
│  └─ Measures/            # Alignment measures, output measures
├─ Input/
│  ├─ landmarks/           # Example 2D landmark CSV files
│  └─ config/              # Subject-specific parameter files
├─ Scripts/
├─ docs/
│  ├─ images/             
│  └─ input
├─ tests/                  # (Optional) regression tests or small checks
├─ LICENSE
└─ README.md
```

---

## Input Data

Patient-specific input parameters are extracted from annotated (bi-)planar X-ray landmarks. These include sagittal and coronal geometric descriptors, as well as patient covariates used for model scaling. The right-handed orthogonal reference frame is defined in the sagittal plane and originates at the posterior sacral reference point. The x-axis points in the anterior–posterior (AP) direction, the y-axis in the superior–inferior (Sup–Inf) direction, and the z-axis in the medial–lateral (ML) direction.

__Sagittal plane landmarks (x–y plane):__
These consist of vertebral sagittal inclinations from T1 (_Angle_T1_) to L5 (_Angle_L5_), vertebral centroid coordinates from T1 (_T1_x_, _T1_y_) to L5 (_L5_x_, _L5_y_), anterior and posterior sacral reference points (_S1_ant_x_, _S1_ant_y_, _S1_post_x_, _S1_post_y_), the bi-femoral head axis (_FH_x_, _FH_y_), and the spinopelvic parameters Pelvic Incidence (_PI_) and Sacral Slope (_SS_).

__Coronal plane landmarks (y–z plane):__
These include vertebral coronal inclinations from T1 (_CorAngle_T1_) to L5 (_CorAngle_L5_), vertebral centroid z-coordinates from T1 (_T1_z_) to L5 (_L5_z_), the bi-femoral head axis (_FH_z_, _FH_y_), and the spinopelvic parameter Pelvic Obliquity (_PelvicObl_).

__Patient covariates:__
Body height (_BH_) and body mass (_BM_) are provided in SI units.

An example ANYBODY input file is provided here:
[docs/input/Example_Patient.any](docs/input/Example_Patient.any)


---

## Outputs 

---

## How to cite

todo

---

## Contributions

Special thanks to all co-authors for their contributions, as well as the European Spine Study Group (ESSG) for constantly collecting clinically relevant data.

---

## Contact 

For questions about the method or collaborations, please contact:  
  
Alice Caimi  
ETH Zurich  
Institute for Biomechanics  
GLC H23. 
Gloriastrasse 37 / 39. 
8092 Zurich, Switzerland  
alice.caimi@hest.ethz.ch  

Florian Rieger  
ETH Zurich  
Institute for Biomechanics  
GLC H23. 
Gloriastrasse 37 / 39. 
8092 Zurich, Switzerland  
florian.rieger@hest.ethz.ch  
