# From Floorplan to Navigation Concepts: Automatic Generation of Text-based Games Descriptions

## Abstract
Text-based games are environments in which defining the world, the representation of the world to the agent and the agent's interaction with the environment are all through text. 
Text-based games expose abstracted, executable representations of indoor spaces through verbally referenced concepts. Yet, the ability of text-based games' to represent indoor environments of real-world complexity is currently limited due to limited support for complex space decomposition and space interaction concepts. 
This paper suggests a procedure to automate the mapping of real-world geometric floorplan information into text-based game environment concepts, using the TextWorld game platform as a case. 
To capture the complexities of indoor spaces, we enrich existing TextWorld concepts supported by theoretical navigation concepts.
We first decompose indoor spaces using skeletonization, and then identify formal space concepts and their relationships. 
We further enhance the spectrum of supported agent interactions with an extended grammar, including egocentric navigation instructions. 
We demonstrate and discuss these new capabilities in an evacuation scenario.
Our implementation extends the capabilities of TextWorld to provide a research testbed for spatial research, including symbolic spatial modelling, interaction with indoor spaces, and agent-based machine learning and language processing tasks.

## How to Run
First, install python 3.8+ and the following dependencies. After downloading the code, you can follow the instruction to test the two environments that are provided in dataset folder (or you can create your own environment files and modify the code):
### Dependencies
General Dependencies:
* matplotlib
* numpy

Spatial Dependencies:
* shapely
* scipy.spatial
* skgeom

TextWorld Dependencies
* textworld

I/O Dependencies:
* geojson

## Running the code
You can simply run the code using python command in terminal (powershell or CMD in windows):
```commandline
python generator.py
```

If you want to change the environment, you can modify the code (**parameters.py**): 

  - change the *ENV_SIMPLE* to **True** if you want to run the simple grid environment;
  - change the *ENV_SIMPLE* to **False** if you want to run the real-world example.

## Jupyter Notebook
You can also use the provided Jupyter Notebook to play and interact with game.

**Note**: You need to install the *Jupyter* dependencies.