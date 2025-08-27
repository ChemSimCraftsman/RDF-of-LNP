# RDF_CODE

This repository contains Python code to calculate the **Radial Distribution Function (RDF)** from molecular dynamics (MD) simulations.  
The script reads trajectory data, applies **periodic boundary conditions (PBCs)**, computes pairwise distances, and constructs normalized RDF plots.  

---

## 📌 About the Project
Radial distribution functions are central to understanding the **local structure** in liquids, polymers, and soft matter systems.  
This notebook (`RDF_CODE.ipynb`) automates the RDF calculation for MD simulation output files, making the analysis reusable and reproducible.  

---

## ⚙️ System / Environment
The code has been tested on the following system:
- **OS:** Linux (Ubuntu 22.04 LTS)  
- **Python:** 3.10+  
- **Core packages:** NumPy, Pandas, SciPy, Matplotlib  

The workflow is designed for analyzing LAMMPS/MD dump files (CSV format per timestep), but can be adapted to other simulation packages.

---

## 📦 Requirements
Install the required Python packages using:

```bash
pip install numpy pandas matplotlib scipy
