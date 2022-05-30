# Autonomous-vacuum-cleaner
The main goal of this repostery is to show and follow the progress of the construction and programming of an autonomous vacuum cleaner. 

# Material we use: 
- Arduino UNO 
- Servo motor
- Stepper motor 
- TF Mini-S LIDAR sensor
- Gyroscope (GY-521)
- 3D printer (Ender 3)

# Software that we use:
- Visual studio Code 
- Arduino IDE 
- SolidWorks 
- Cura
- Fusion 360

# Work that we have done until now: 
- Work on the navigation system (2D mapping)

  The first step of the project is to build a mapping solution. The idea is to use a sensor to measure a distance, and the angle of the sensor. With this data     we are able to define polar coordinates that we later convert in cartesian coordinates to display a dot cloud in the python program using pygame. 
  At first, we used an ultrasonic sensor and a servo motor. We soon realized that the ultrasonic sensor wasn't precise enough, so we decide to go with a LIDAR     sensor. The results were better but it seems like the servo motor wasn't providing us the smoothness that we needed, so we decide to use a stepper motor wich   is very precise but need a stubborn to define his position. We are currently working on this stubborn, and we are also studying the posibilitie of using a       gyroscope to enslave the stepper motor (WORK IN PROGRESS) 
  
- Equations :\
   ![equation](https://latex.codecogs.com/svg.image?x=&space;distance&space;*cos(\frac%7Bangle*\pi%7D%7B180%7D&space;))\
   ![equation](https://latex.codecogs.com/svg.image?y=&space;distance&space;*sin(\frac%7Bangle*\pi%7D%7B180%7D&space;))
 
- 3D Printing :

As we decided to use a stepper motor and a switch button (used to set the angle at 0), we had to create a mecanism to make the sensor press the switch. 
For that purpose, we designed two piesces with Solidworks and printed it with a 3D printer. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/90306651/171063021-10252cfd-1782-4e20-865a-fef87d306f5d.png" />
</p>
![image](https://user-images.githubusercontent.com/90306651/171063021-10252cfd-1782-4e20-865a-fef87d306f5d.png)

![image](https://user-images.githubusercontent.com/90306651/171063060-5dea7741-92d9-42bd-b3d6-0e473c63f916.png)

  
  
  
# Results:

![image](https://user-images.githubusercontent.com/90306651/171043274-94945094-7e0a-4613-8707-792434d4c4f3.png)







# Next steps (no specific order)
- Design the vacuum cleaner housing
- Path finding algorithm 
- Work on the suction system
- Work on the movement system
- Work on the obstacle avoidance system
- Auto scale pygame 
- Process all the calculation on the python program to make all the process faster

# Ideas to explore
- Try to use an analog Hall Effect Sensor + magnet to define the stubborn instead of a pushbutton
- Try to use a DC motor instead of a stepper motor to achieve faster scans 
- Create our own PCB with JLCPCB 
