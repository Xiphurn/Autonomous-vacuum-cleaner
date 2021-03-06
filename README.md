# Autonomous vaccum cleaner
The main goal of this repository is to show and follow the progress of the construction and programming of an autonomous vaccum cleaner. 

# Material we use: 
- Arduino UNO 
- Servo motor
- Stepper motor 
- TF Mini-S LIDAR sensor
- Push switch (button)
- 3D printer (Ender 3)

# Software that we use:
- Visual studio Code 
- Arduino IDE 
- SolidWorks 
- Cura
- Fusion 360

# Work that we have done until now: 
- Work on the navigation system (2D mapping)

  The first step of the project is to build a mapping solution. The idea is to use a sensor to measure a distance, and the angle of the sensor. With this data we are able to define polar coordinates that we later convert in cartesian coordinates to display a dot cloud in the python program using pygame.\
  At first, we used an ultrasonic sensor and a servo motor. We soon realized that the ultrasonic sensor wasn't precise enough to get the results we hoped for, so we decided to use a LIDAR sensor.\
  The results were better, yet the servo motor wasn't providing us the smoothness that we needed, so we decided to use a stepper motor which is very precise but needs a stopper or another sensor to define his position. We are currently working with a push button for that purpose.
  
- Equations :\
   ![equation](https://latex.codecogs.com/svg.image?x=&space;distance&space;*cos(\frac%7Bangle*\pi%7D%7B180%7D&space;))\
   ![equation](https://latex.codecogs.com/svg.image?y=&space;distance&space;*sin(\frac%7Bangle*\pi%7D%7B180%7D&space;))
 
- 3D Printing :

As we decided to use a stepper motor and a push switch (used to set the angle at 0), we had to create a mecanism to make the sensor press the switch. 
For that purpose, we designed two parts with Solidworks and 3D printed them. 

The first part is a support for the Lidar sensor, the support is attached to the stepper motor and supposed to hold the sensor.
It features a tab on the right side of the Lidar. It's purpose is to put pressure on the other tab of the motor support, and consequently press the button.
<p align="center">
  <img src="https://user-images.githubusercontent.com/90306651/171063021-10252cfd-1782-4e20-865a-fef87d306f5d.png" /> <br/>
  Lidar support model (Solidworks)
</p>

The second part is a support for the motor and it is also supporting the switch and the tab who activates it.

<p align="center">
  <img src="https://user-images.githubusercontent.com/90306651/171063060-5dea7741-92d9-42bd-b3d6-0e473c63f916.png" /> <br/>
  Motor support model (Solidworks)
</p>

The Solidworks files have been saved as STL files, and have been printed by a 3d printer (Ender 3).
  
  
  
# Results:

At the current state of work, the results of the mapping are showed on a pygame window with a dimension scale implemented in it. The position of the sensor is marked by a picture of a vacccum cleaner. The results are updated at each transit of the sensor. 
Here is an example of the results showed by the program and a picture of the real corresponding situation : 

<p align="center">
  <img src="https://user-images.githubusercontent.com/90306651/171043274-94945094-7e0a-4613-8707-792434d4c4f3.png" width: 30% /> <br/>
  Results of a Lidar scan <br/>
  <img src="https://user-images.githubusercontent.com/90306651/171064925-54427763-ccd2-4b88-a60e-32765c3acc53.jpg" /> <br/>
  Picture corresponding to the situation
</p>


# Next steps (no specific order)
- Design the vacuum cleaner housing
- Path finding algorithm 
- Work on the suction system
- Work on the movement system
- Work on the obstacle avoidance system
- Auto scale pygame 
- Process all the calculation on the python program to make all the process faster

# Ideas to explore
- Try to use an analog Hall Effect Sensor + magnet to define the stopper instead of a pushbutton
- Try to use a DC motor instead of a stepper motor to achieve faster scans 
- Create our own PCB with JLCPCB 
