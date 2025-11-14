<div align="center">
  <h1>Biplanar Spinal Alignment Reconstruction Method</h1>
  <p>
    AnyBody model high fidelity calibration implementation for reconstructing 3D spinal alignment
    from biplanar radiographs and extracting subject-specific sagittal and coronal alignment parameters.
    <br />
    <!-- Optional: link to preprint/paper -->
    <a href="https://doi.org/XX.XXXX/your-doi-here"><strong>Caimi et Rieger et al. (202X)</strong></a>
  </p>
</div>

![Figure](docs/images/Figure_01.jpg)



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
- [Contributing](#contributing)
- [Contact](#contact)

---

## About

This repository provides an AnyBody-based implementation of a biplanar spinal alignment
reconstruction method. Based on vertebral landmark annotations of sagittal or biplanar radiographs (sagittal & coronal), 
the model reconstructs the 3D spinal alignment, i.e. vertebral centroid positions and inclinations in the respective planes.

The code is designed as a **standalone pipeline** for researchers working with
biplanar radiographs who want to:
- Calibrate 3D spinal alignment AnyBody models from 2D projections
- Integrate subject-specific alignments into downstream musculoskeletal models

---

## Features

- ✅ AnyBody Modeling System implementation (version X.X+)
- ✅ Biplanar (coronal + sagittal) landmark-based posture reconstruction
- ✅ Automatic computation of global and segmental alignment parameters
- ✅ Example datasets and scripts for running the full pipeline

---

## Methods Overview

High-level pipeline (adapt to what you actually do):

1. **Input**: Biplanar radiographs (or extracted landmarks) in sagittal and coronal planes  
2. **Landmark definition**: 2D coordinates of vertebral reference points (e.g. T1–L5)  
3. **3D reconstruction**: Optimization that fits a parametric 3D spine model to the 2D projections  
4. **Alignment metrics**: Computation of sagittal and coronal angles, offsets, and global alignment parameters  
5. **Export**: 3D vertebral positions and orientations for downstream use

Include a small schematic figure in `docs/` if you have one and link it here.

---

## Installation

### Requirements

- **AnyBody Modeling System** version X.X or higher
- (Optional) **Python 3.10+** for pre- and post-processing scripts

### Get the repository

```bash
git clone https://github.com/USERNAME/biplanar-spinal-alignment.git
cd biplanar-spinal-alignment
```

--- 

## Usage

---

## Installation

---

## Repository structure 

```
biplanar-spinal-alignment/
├─ Application/
│  ├─ Main.any             # Entry point for the AnyBody model
│  ├─ ModelSetup.any       # Global settings, parameters, folders
│  └─ SpineModel.any       # Spine definition, joint chains, drivers
├─ Model/
│  ├─ Segments/            # Vertebra/pelvis segment definitions
│  ├─ Drivers/             # Kinematic drivers for the reconstruction
│  └─ Measures/            # Alignment measures, output measures
├─ Input/
│  ├─ landmarks/           # Example 2D landmark CSV files
│  └─ config/              # Subject-specific parameter files
├─ Scripts/
│  ├─ run_single_subject.anym   # AnyBody macro(s)
│  ├─ run_batch_reconstruction.py
│  └─ postprocess_results.py
├─ Results/
│  └─ subject_xxx/         # Example output folders (can be in .gitignore)
├─ docs/
│  ├─ figures/             # Method schematics, README images
│  └─ method_description.md
├─ tests/                  # (Optional) regression tests or small checks
├─ LICENSE
└─ README.md
```

---

## Input Data

---

## Outputs 

---

## Validation & Limitations

---

## How to cite

todo

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
