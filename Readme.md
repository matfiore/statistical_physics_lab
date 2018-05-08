# Statistical Physics simulations in Python 3

This collection of scripts implements two popular and fundamental statistical physics 
models with Python 3. As a side objective, it aims to introduce the students to few
basic Python Object concepts such as classes, inheritance, iterators, properties,
and decorators, and the most important data structures i.e. list and dictionary. 
In addition it shows how the fundamental numpy and matplotlib libraries can be used 
for scientific computing and visualisation.

## Folder 1: KMC_SAM

This folder contains the implementation of a Surface Absorption Model (SAM) of 
self-assembling molecules based on Kinetic Monte Carlo (KMC)

* Kinetic_MC.py is the main scripts that runs the simulation.
* surface_objects.py contains the definition of the entities used in the simulation.
* cluster_analysis.py contains a recursive algorithm to detect clusters on a lattice.

## Folder 2: MCMC_Ising

This folder stores the implementation of a Spin Glass Ising model using Markov Chain 
Monte Carlo and in particular the Metropolis algorithm.

* Ising2D.py is the main script that implements the simulation.
* Ising_obj.py contains the definition of Spin and SpinGlass object. The thermalisation
process is simulated calling the metropolis_flipper method of SpinGlass.
