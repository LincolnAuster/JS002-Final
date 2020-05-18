# The Physics of Shielding

## Abstract
Filler Content

## Methods
The goal is to simulate the shielding experienced by electrons on outer layers of the nucleus only by simulating the charges of the electrons. The open source program [Blender](https://blender.org) was used for this as it is primarily a graphics program (which removes any need to write code for graphics) and has a robust scripting API that exposes nearly everything to a Python interface. The program must be able to compute the magnetic force exerted on an object from an object in accordance with the inverse square law. It must also be able to specify magnetic weights for each object. A nucleus containing 4 protons would have a weight of 4. Were these to be represented as 4 separate objects, they would repel each other without a binding force also applied. As it is easier to implement a weight, and no effect would be made on shielding, this will be used.

## Program Requirements
As the program is written in Blender's environment, it should comply with Blender's best practices. Loosely, this means that it must expose most values that it uses to the graphical interface, and must only run when activated, as well as complying with Blender's object oriented style.

It must be able to
- Understand magnetic weights
- Compute the positively charged particles' and negatively charged particles' pushes simultaneously.

## Program Implementation 

The program, when initialized, loops through every object. If its name contains the word "Positive" (case-sensitive) it automatically assigns a weight of 1. If its name contains the word "Negative" (case-sensitive) it automatically assigns a weight of -1. It then loops through the set of positively charged particles. For each of the positively charged particles it finds the distance to each of the negatively charged particles. From these, the inverse square law can be used to find the distance the negatively charged particles are pulled. The pull of all the particles on one are summed. This does not provide the direction that the particle must move, but it does provide the total strength of the pull.

This is summed for all particles. 

## Miscellaneous Notes about Implementation

- Blender 2.83.15 (beta) was used
- Python 3.8.2 was used
- Tabs were used over spaces (obviously)
- And Vim was used over emacs.

These last two points are by far the most important.

## Replicating Shielding with the Above Implementation
Objects were laid out such that a circle of 2 negatively charged cubes surrounding a positively charged cube (weight=6). 4 negatively charged cubes surrounded these. This represents a carbon atom, and is shown in figure 1.

![Figure 1: Carbon molecule laid out in blender](/fig1.png)
> Figure 1: Carbon molecule laid out in blender

The charges on the outer (blue in figure 1) particles are measured to be 0.036024 units by the simulation. When the inner shell is removed (figure 2), the charges on the outer particles are measured to be 0.105469 units by the simulation, a 151.87% increase.
![Figure 2: Carbon molecule with only valence electrons](/fig2.png)
> Figure 2: Carbon molecule with only valence electrons]
