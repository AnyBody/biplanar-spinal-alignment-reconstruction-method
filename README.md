<div align="center">
  <h1>Biplanar Spinal Alignment Reconstruction Method</h1>
  <p>
    AnyBody plugin for high-fidelity reconstructing of 3D spinal alignment from biplanar radiographs.
    <br />
    <!-- Optional: link to preprint/paper -->
    <a href="https://www.sciencedirect.com/science/article/pii/S0021929026003143?via%3Dihub"><strong>Caimi et Rieger et al. (2026)</strong></a>
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
- [Repository structure](#repository-structure)
- [Input Data](#input-data)
- [Outputs](#outputs)
- [How to cite](#how-to-cite)
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
- Example AnyBody input file

---

## Methods Overview

High-level pipeline:

1. **Input**: Extracted landmarks of biplanar radiographs in sagittal and (optionally) coronal planes  
2. **Anatomical Landmark definition**: 2D coordinates of vertebral corner nodes (T1-L5), sacral endplate and bi-femoral head axis, as well as spinopelvic parameters Pelvic Incidence (PI), Pelvic Tilt (PT), Sacral Slope (SS) and Pelvic Obliquity (PO)
3. **Inputs**: Vertebral inclinations and vertebral centroids coordinates, derrived from anatomical landmarks in the sagittal and coronal plane
4. **3D reconstruction**: Posture reconstruction drivers that integrate the degrees of freedom in the model setup
5. **Alignment metrics**: Computation of sagittal and coronal angles, offsets, and global alignment parameters  

---

## Installation

### Requirements

- **AnyBody Modeling System** version 8.0 or higher

### Get the repository

```bash
git clone https://github.com/Anybody/biplanar-spinal-alignment-reconstruction-method.git
cd biplanar-spinal-alignment
```

--- 

## Usage

1. **Import Anybody input files**: 
    - Place your input files in the **_InputAlignment_** folder. An example input file can be found in the repository documents ([docs/input/Example_Patient.any](docs/input/Example_Patient.any)). 

    Input folder directory:

        Anybody_model/Application/Examples/ThoracicModel/Setup/InputAlignment


2. **Model Setup**: 
    - Configurate your alignment representation mode in the **_UserDefinitions.any_** file. The user can specify whether to model spinal alignment using the Regional Measures method (**_AlignmentModeling_** off) or the Vertebral Inclination and Centroids Position method (**_AlignmentModeling_** on).
    - If cervical annotations, i.e. vertebral inclinations and centroid positions, are available, the alignment representation method can be extended to these segments by enabling the **_IncludeNeckCalibration_** parameter. 
    - To enable a coronal alignment representation, the **_CoronalAlignment_** parameter has to be switched on in the respective Input file (see first line in the coronal alignment section). 

    User definition directory: 

        Anybody_model/Application/Examples/ThoracicModel/Setup/Model/UserDefinitions.any


4. **Run Simulation**: 
    - Run _biplanar-spinal-alignment-reconstruction-method.main.any_ to execute the Anybody Simulation script

    Main file directory:

        Anybody_model/Application/Examples/ThoracicModel/biplanar-spinal-alignment-reconstruction-method.main.any

---

## Repository structure 

```
biplanar-spinal-alignment/
├── Anybody_model/
│   └── Application/
│       └── Examples/
│           └── ThoracicModel/
│               ├── biplanar-spinal-alignment-reconstruction-method.main.any
│               └── Setup/
│                   ├── InputAlignment/
│                   │   └── Example_Patient.any
│                   └── Model/
│                       └── UserDefinitions.any
├── docs/
│   ├── images/
│   └── input/
│       └── Example_Patient.any
└── README.md
```

---

## Input Data

1. **Patient-specific data:**
    - Patient-specific input parameters are extracted from annotated (bi-)planar X-ray landmarks. These include sagittal and coronal geometric descriptors, as well as patient-specific anthropometric data for model scaling, i.e. body height (BH - in m) and body mass (BM - in kg). 
    - The right-handed orthogonal reference frame is defined in the sagittal plane and originates at the posterior sacral reference point. The x-axis points in the anterior–posterior (AP) direction, the y-axis in the superior–inferior (Sup–Inf) direction, and the z-axis in the medial–lateral (ML) direction.

2. **Sagittal plane landmarks (x–y plane):**
    - Sagittal landmarks consist of vertebral sagittal inclinations from T1 (_Angle_T1_) to L5 (_Angle_L5_), vertebral centroid coordinates from T1 (_T1_x_, _T1_y_) to L5 (_L5_x_, _L5_y_), anterior and posterior sacral reference points (_S1_ant_x_, _S1_ant_y_, _S1_post_x_, _S1_post_y_), the bi-femoral head axis (_FH_x_, _FH_y_), and the spinopelvic parameters Pelvic Incidence (_PI_) and Sacral Slope (_SS_).

3. **Coronal plane landmarks (y–z plane):**
    - Coronal landmarks include vertebral coronal inclinations from T1 (_CorAngle_T1_) to L5 (_CorAngle_L5_), vertebral centroid z-coordinates from T1 (_T1_z_) to L5 (_L5_z_), the bi-femoral head axis (_FH_z_, _FH_y_), and the spinopelvic parameter Pelvic Obliquity (_PelvicObl_).


An example ANYBODY input file is provided here:
[docs/input/Example_Patient.any](docs/input/Example_Patient.any)


---

## Outputs 

Model outputs include (1) intervertebral joint reaction forces, (2) muscle forces and activities, (3) segmental rotations, (4) sagittal alignment parameters, (5) calculated centers of mass, and (6) radiographic conformity, i.e. deviations between the model alignment and input parameters.

1. **Joint Reaction Forces:**
    - Compression force: _L4L5CompressionForce_ (i.e. L4L5)
    - AP Shear force: _L4L5AnteroPosteriorShearForce_
    - ML Shear force: _L4L5MedioLateralShearForce_

2. **Muscle Forces & Activities:**
    - Total muscle activity: _AllMuscleMaxAct_
    - Total muscle force: _AllMuscleTotalForce_
    - Individual muscle activities: _ErectorSpinaeMaxAct_ (i.e. ErectorSpinae)
    - Individual muscle force: _MultifidusTotalForce_ (i.e. Multifidus)

3. **Segmental rotations:** 
    - Intervertebral joint angle: 
      - _SegmentalRotationFlexion_ (i.e. sagittal plane)
      - _SegmentalRotationLateralBending_ (i.e. coronal plane)
      - _SegmentalRotationAxialRotation_ (i.e. transverse plane)

4. **Conventional alignment metrics:**
    - Postural measures: _LL_ (i.e. Lumbar Lordosis)

5. **Center of Mass:** 
    - Center of mass measurements: 
      - _CoM_x_ (i.e. anterio-posterior)
      - _CoM_y_ (i.e. superior-inferior)
      - _CoM_z_ (i.e. medio-lateral)

6. **Radiographic conformity metrics:**
    - Positional deviation vector: _L4L5_error_pos_ (i.e. L4L5)
    - Sagittal inclination deviation: _L4L5_error_rotZ_
    - Coronal inclination deviation: _L4L5_error_rotX_
    - Transversal inclination deviation: _L4L5_error_rotY_ (essentially zero, as transversal rotations are not yet included)

    
  Output files will be saved in .csv format to the following directory: 
      
      Anybody_model/Application/Examples/ThoracicModel/Setup/OutputData
---

## How to cite

A. Caimi, F. Rieger, K. Cybulski, F. Galbusera, S. Richner-Wunderlin, F. Kleinstück, D. Haschtmann, D. Jeszensky, T.F. Fekete, M. Loibl, F. Pellisé, I. Obeid, J. Pizones, A. Alanay, C. Yilgor, C. Netzer, S.J. Ferguson, D. Ignasiak,
Sensitivity of musculoskeletal model-predicted loads to spinal alignment individualization in adult spinal deformity,
Journal of Biomechanics, 2026, 113459, ISSN 0021-9290, https://doi.org/10.1016/j.jbiomech.2026.113459.

---

## Contributions

We thank Morten Enemark Lund for maintaining the AnyBody GitHub repository and for his help in setting up this page. Special thanks to all co-authors for their contributions, as well as the European Spine Study Group (ESSG) for constantly collecting clinically relevant data.

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
