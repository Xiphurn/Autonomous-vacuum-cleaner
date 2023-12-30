# import serial
# import serial.tools.list_ports
# import numpy as np 
# import pygame
# import math
# import sys

# B = np.zeros((181,2))
# taillex = 1920
# tailley = 1080
# size = 4
# screen = pygame.display.set_mode((taillex, tailley))
# image = pygame.image.load(r'C:\Users\guilh\Mon Drive\Perso\Projets info\Autonomous-vacuum-cleaner\Images\aspi.png').convert_alpha()   # robot picture for the display
# image = pygame.transform.scale(image, (255, 170))   # resize robot
# image = pygame.transform.flip(image, False, True)     # flip the image
# pygame.font.init()  # initialize font 
# font = pygame.font.Font(None, 24)


# print("Looking for a serial port...")

# ports = serial.tools.list_ports.comports(include_links=False)

# if (len(ports) != 0):   # at least one port was found

#     if (len(ports) > 1):    # printing number of active ports
#         print (str(len(ports)) + " ports were found:") 
#     else:
#         print ("1 port was found:")

#     ligne = 1

#     for port in ports :    # printing port name
#         print(str(ligne) + ' : ' + port.device)
#         ligne = ligne + 1

#     portChoisi = int(input("Choose a port: "))   # choosing port
#     baud = 9600

#     # Establishing serial connection 
#     arduino = serial.Serial(ports[int(portChoisi) -1  ].device, baud, timeout = 0.5)
    
#     print('Connection to ' + arduino.name + ' at ' + str(baud) + ' baud was succesful! ')

    
#     # printing decoded data if received
#     while True:
#         data = arduino.readline().decode('ascii').rstrip() 
#         #print(data)
        
#         if len(data) > 0:

#             datasplit=data.split(' , ') 
#             if len(datasplit) == 2 and (datasplit != " " ):     # making sure the data is in the right format 
#                 angle = int(datasplit[0])
#                 distance = 0
#                 distance = float(datasplit[1])
#                 x = distance*math.cos(angle*(math.pi/180))    # calculating cartesian coordinates
#                 y = distance*math.sin(angle*(math.pi/180))

#                 B[angle][0] = x       # assigning the coordinates into a numpy array for the corresponding angle
#                 B[angle][1] = y
#                 if (angle == 180 or angle == 0):    # resesting the screen once a full scan has been made
#                     screen.fill("black")
                    
#                 #print (B)   # for testing purposes
                
#                 # d=90
#                 # for i in range (1,17): 
#                 #     pygame.draw.line(screen,'white',(0,(i/10)*(tailley-image.get_height())/2+10),(taillex,(i/10)*(tailley-image.get_height())/2+10))    # displaying the grid (scale)
#                 #     text = font.render(str(d)+" cm",1,(255,255,255))
#                 #     screen.blit(text, (1850,(i/10)*(tailley-image.get_height())/2-5 ))
#                 #     d = d-6

#                 d=90
#                 for i in range (1,17): 
#                     pygame.draw.line(screen,'white',(0,(i/10)*(tailley-image.get_height())/2+10),(taillex,(i/10)*(tailley-image.get_height())/2+10))    # displaying the grid (scale)
#                     text = font.render(str(d)+" cm",1,(255,255,255))
#                     screen.blit(text, (1850,(i/10)*(tailley-image.get_height())/2-5 ))
#                     d = d-6
                    
#                 image_center = ((taillex-image.get_width())/2,(tailley-image.get_height())/2+255)   # displaying robot picture 
#                 screen.blit(image, image_center)    
                
#                 if float(datasplit[1])>10: #only displaying the cartography if the distance is greater than 10 cm
#                     pygame.draw.circle(screen, "red",(taillex/2 + B[angle][0]*5, tailley/2 - B[angle][1]*5+200), size, 0)   # displaying the cartography via pygame
#                 pygame.display.flip()   

#         for event in pygame.event.get():    # quitting pygame interface
#             if event.type == pygame.QUIT:
#                 running = False
#                 sys.exit()

            
# else: 
#     print("No active port was found")

