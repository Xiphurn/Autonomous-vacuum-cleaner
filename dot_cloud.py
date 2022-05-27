#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Receiving data from Arduino via USB 
'''

import serial
import serial.tools.list_ports
import numpy as np 
import pygame
import math
import sys
B=np.zeros((181,2))
taillex=1920
tailley=1080
size=4
screen = pygame.display.set_mode((taillex, tailley))


print("Looking for a serial port...")

ports = serial.tools.list_ports.comports(include_links=False)

if (len(ports) != 0):   # at least one port was found

    if (len(ports) > 1):    # printing number of active ports
        print (str(len(ports)) + " ports were found:") 
    else:
        print ("1 port was found:")

    ligne = 1

    for port in ports :    # printing port name
        print(str(ligne) + ' : ' + port.device)
        ligne = ligne + 1

    portChoisi = 2

    baud = 115200

    # Establishing serial connection 
    arduino = serial.Serial(ports[int(portChoisi) -1  ].device, baud,timeout=0.5)
    
    print('Connection to ' + arduino.name + ' at ' + str(baud) + ' baud was succesful! ')

    # printing decoded data if received
    while True:
        data = arduino.readline().decode('ascii').rstrip() 
        print(data)
      
        
        if len(data) > 0:

            datasplit=data.split(' , ') 
            if len(datasplit)==2 and (datasplit!=" " ):     # making sure the data is in the right format 
                angle=int(datasplit[0])
                distance=float(datasplit[1])
                x=distance*math.cos(angle*(math.pi/180))    # calculating cartesian coordinates
                y=distance*math.sin(angle*(math.pi/180))
            
                B[angle][0]=x
                B[angle][1]=y
                if (angle==180 or angle==0):    #resesting the screen once a full scan has been made
                    screen.fill("black")
                    
                #print (B)

                pygame.draw.circle(screen, "red",(taillex/2+B[angle][0]*5,tailley/2-B[angle][1]*5+200),size,0)
                pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            
else: 
    print("No active port was found")

