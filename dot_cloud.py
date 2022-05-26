#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Receiving data from Arduino via USB 
'''

import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import numpy as np 
import pygame
import math
import sys
A=np.array([[0,0,0]])
B=np.zeros((181,2))
taillex=1920
tailley=1080
size=4
screen = pygame.display.set_mode((taillex, tailley))
n=10
Mx=0
My=0
i=0
a=0
k=0


print("Recherche d'un port serie...")

ports = serial.tools.list_ports.comports(include_links=False)

if (len(ports) != 0): # at least one port was found

    if (len(ports) > 1):     # printing number of active ports
        print (str(len(ports)) + " ports actifs ont ete trouves:") 
    else:
        print ("1 port actif a ete trouve:")

    ligne = 1

    for port in ports :  # affichage du nom de chaque port
        print(str(ligne) + ' : ' + port.device)
        ligne = ligne + 1

    portChoisi = 2

    baud = 115200

    # Establishing serial communication
    arduino = serial.Serial(ports[int(portChoisi) -1  ].device, baud,timeout=0.5)
    
    print('Connexion a ' + arduino.name + ' a un baud rate de ' + str(baud))

    # si on reçoit un message, on l'affiche
    while True:
        data = arduino.readline().decode('ascii').rstrip()
        print(data)
      
        
        
        if len(data) > 0:

            datasplit=data.split(' , ') 
            if len(datasplit)==2 and (datasplit!=" " ):
                angle=int(datasplit[0])
                distance=float(datasplit[1])
                x=distance*math.cos(angle*(math.pi/180))
                y=distance*math.sin(angle*(math.pi/180))
            
                B[angle][0]=x
                B[angle][1]=y
                if (angle==180 or angle==0):
                    screen.fill("black")
                    
                #print (B)

                pygame.draw.circle(screen, "red",(taillex/2+B[angle][0]*5,tailley/2-B[angle][1]*5+200),size,0)
                pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            
else: # on n'a pas trouvé de port actif
    print("Aucun port actif n'a ete trouve")







