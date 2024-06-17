## Welcome to ElectroSpray!

### Electrospray ionization of small molecules
### ElectroSpray is a computational workflow for predicting the ionization efficiency of chemicals in electrospray ionization using principles of computational chemistry. 

#### As opposed to machine learning approaches, ElectroSpray is a theory-based approach and does not require large datasets to train and test. 

ElectroSpray is part of a project that is currently under review. 

The "OH box files" folder contains the parameter and topology files for generating a cube containing OH- ions. The box was later used to dissolve each chemical used in the calculations. The sytem was neutralized by the addition of H+ ions. 

The "mdp files" folder contains the files that were used for the simulations with GROMACS.

The python scripts "cgenff_charmm2gmx.py" and "charmm2gromacs-pvm.py" were used to convert the topology files from CHARMM to GROMACS. The topology files were generated with the CHARMM-GUI online platform (https://www.charmm-gui.org/),

The "mdrunchem" script was used to automate the simulations and the calculations of the Lennart-Jones interactions and Coulomb interactions between the compounds and the H+ ions.

The folder "interaction energies" contains all the files that were generated from the simulations and the python scripts that were used to construct the model.

![TOC](https://github.com/dimitriabrahamsson/electro-chem/assets/56902317/c06dd01a-6b5f-47b1-8b60-d9c914593ef9)
