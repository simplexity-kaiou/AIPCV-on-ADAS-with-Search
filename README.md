# Analyzing the Impact of Product Configuration Variations on Advanced Driver Assistance Systems with Search

## Description
Due to the complexity of designing vehicle products and the inherent uncertainties in their operating environments, ensuring the safety of their Advanced Driver Assistance Systems (ADASs) becomes crucial. Especially, very minor changes to a vehicle design, for instance due to production errors or component degradation, might lead to failures of ADASs and, therefore, catastrophic consequences such as collision occurrences. Motivated by this, we propose a multi-objective search-based approach (employing NSGA-II)to fnd minimum changes to the confguration of a set of confgurable parameters of a vehicle design, such that the collision probability is maximized, consequently leading to a reversal change in its safety. We conducted experiments, in a vehicle driving simulator, to evaluate the eﬀectiveness of our approach. Results show that our approach with NSGA-II signifcantly outperforms the random search. 

## Repository content
This repository contains: 

* Python code for implementation of the Carla and algorithms(NSGAII and Random Search of jMetalPy).
* Raw data of the experiment results.

## Prerequisite
* **Carla 0.9.10** <https://carla.readthedocs.io/en/0.9.10/>
* **Python** The code should be run using python 3.7.
* **jMetalPy** ```pip install jmetalpy```

## People
* Kaiou Yin
* Paolo Arcaini http://group-mmm.org/~arcaini/
* Tao Yue https://www.simula.no/people/tao
* Shaukat Ali https://www.simula.no/people/shaukat

## Paper
K. Yin, P. Arcaini, T. Yue, S. Ali. Analyzing the impact of product configuration variations on advanced driver assistance systems with search. In Proceedings of the Genetic and Evolutionary Computation Conference (GECCO '21) [[doi](https://doi.org/10.1145/3449639.3459332)]
