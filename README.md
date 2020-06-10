# Team-Hermes-Senior-Design-Tremor-Damping
MATLAB and Python Model for the damping of physical tremors in patient's hands based on IMU measurements

## Actuator Model
**Actuator Model** contains the code for generating actuator model plots for our system, written in python. It is designed to
generate a plot based on inputted motor data. It is not a comprehensive motor selector, as that is outside 
the scope of this project. Instead, it is intended to show how a particular motor would align with our intended
actuation solution, a series of mechanical links that are actuated to dampen tremors

##Orientation Estimation
**Orientation Estimation** contains the python code using the micropython IMU project to estimate the orientation of a joint based on IMU measurements (to get reasonable data)

## Controller
**Controller** contains the matlab/simulink code that actually runs the simulation we designed. Our report contains the details
on the theory, but this is the code we used (along with the data) to generate our results. 

## Visualization
**Visulaization** contains the Blendr files and the code required to visualize our system's results in a more comfortable
form compared to the graph outputs of the MATLAB scripts

## How to Set Up the System: 
**The Matlab portion of our simulation setup is as follows:**
1. Download matlab and simulink. The campuswide licence is all you need. No other toolbox is necessary
2. In the **__Controller__** folder, open the file titled __TremorStabilizingSimulation.mdl__ in simulink. This is the entire model of the      stabilizing system
3. In the center of the simulation, there are 3 disconnected arrows. Top down, they are:
  1. a sinusoidal 1 Hz source
  2. Sample orientation data from a hand 1
  3. Sample orientation data from a hand 2
  Select the arrow you want and drag it to the input of the summation block to the right. 
4. Run the simulation. The viewers should pop up for PSD of the input/output, and a scope viewer of the signals involved. The sim will also output CSV formatted files into the Output folder, for both the input and the output data, which can be entered to other visualizing programs (see: blender simulation)

**The Blender portion of our simulation setup is as follows:**
1. Download Blender v2.80 (https://www.blender.org/download/releases/2-80/). As a side, make sure you also have Python 3 on your system as well.
2. After opening the "rigging_fingers.blend" file, you'll notice that there are various modes of development on the top of the screen ("Animation", "Compositing", "Default Logic" etc.). Click on the **Scripting** tab.
3. You'll need to edit two portions of this code, both of which pertain to a specific **path**. The first path you'll need to modify is in Line 11; edit it to the path of the output CSV file from the Matlab simulation.
4. The other path you'll need to modify is the output of the animation in Line 33.
5. The final step is to simply run the script (Option+P for Mac users) or simply go to the Edit tab below the script (NOT the Edit button next to File) and click "Run Script". 
6. The animation should take a few minutes since it's rendered; once it's complete, you'll have the final visualization at the output path you detailed earlier.
