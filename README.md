# grid-mEP
This repo is meant to analyse the environmental and economic costs of the insulation materials found in `materials.py`.
This should lead to the mapping of a grid of building materials to energy demands based on Energy Plus simulations.

# Usage of `materials.py`
This file contains the description of the materials that are to be used in the Energy Plus simulations. 
These materials are described by their physical properties, such as their density, and also require a desired thickness for the walls, grounds and roofs
that are to be varied in the Energy Plus model.

# Usage of `simulation.ipynb`
The jupyter notebook `simulation.ipynb` uses the package `opyplus` to run whole-building energy simulations using Energy Plus.
The required inputs, in addition to the material descriptions as in `materials.py`, are the following:
- Weather file in the format `.epw`
- Building model in the format `.idf`
- The surface of the walls, grounds and roofs that use the materials found in `materials.py`

Using `simulation.ipynb` runs Energy Plus simulations. The results of these simulations are stored in new folders named after each material analysed.
The notebook will also display the total economic and environmental costs of each building material.

# Use case
- The economic and environmental costs of the buildings materials can be used as inputs in the optimization performed in the following repo: 
https://github.com/julie-vienne/single_energy_hub_single_year

# Source
- `opyplus` documentation: https://opyplus.readthedocs.io/en/v1.3.0/index.html 