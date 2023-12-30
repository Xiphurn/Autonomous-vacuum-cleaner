import serial
import serial.tools.list_ports
import numpy as np 
import pygame
import math
import sys
import time

IRL_coordinates = np.zeros((181,2))
Screen_coordinates = np.zeros((181,2))
screen_size_x = 1920
screen_size_y = 1080
size = 4
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
image = pygame.image.load(r'C:\Users\guilh\Mon Drive\Perso\Projets info\Autonomous-vacuum-cleaner\Images\aspi.png').convert_alpha()   # robot picture for the display
image = pygame.transform.scale(image, (255, 170))   # resize robot
image = pygame.transform.flip(image, False, True)     # flip the image
pygame.font.init()  # initialize font 
font = pygame.font.Font(None, 24)

Screen_center_y = screen_size_y/2   # Center of the screen y coordinate
Screen_center_x = screen_size_x/2   # Center of the screen x coordinate

scale_factor_global = 1


def calculate_scale_factor(number):
    """
    Calculate the nearest multiple of 10 greater than the given number,
    then divide this multiple by 100 and store the result in scale_factor.

    :param number: The input number to process
    :return: The calculated scale factor
    """
    # Find the nearest multiple of 10 greater than the input number
    nearest_multiple_of_10 = (number + 9) // 10 * 10

    # Divide the nearest multiple of 10 by 100 and store in scale_factor
    scale_factor = nearest_multiple_of_10 / 100

    return 1#scale_factor



def draw_points(screen, x, y, angle):
    global scale_factor_global

    if scale_factor_global != calculate_scale_factor(np.max(IRL_coordinates[:, 1])): #scale factor different from the one already calculated
        scale_factor_global = calculate_scale_factor(np.max(IRL_coordinates[:, 1]))

        for i in range(0, 181):
            Screen_coordinates[i][0] = (Screen_coordinates[i][0])
            Screen_coordinates[i][1] = (Screen_coordinates[i][1])/scale_factor_global

    else: #same scale factor
        Screen_coordinates[angle][0] = x + Screen_center_x
        Screen_coordinates[angle][1] = (-(y*5/scale_factor_global)) + Screen_center_y

       # print("screen coordinates: " + str(Screen_coordinates[angle][0]) + " " + str(Screen_coordinates[angle][1]))
        
    for i in range(angle):
        pygame.draw.circle(screen, "red",(Screen_coordinates[i][0], Screen_coordinates[i][1]), size, 0)
        pygame.display.flip() 
        #print("Ok")

    #print("x: " + str(x) + " y: " + str(y))
    #x_coord = x + Screen_center_x
    #y_coord = (-(y*5/scale_factor)) + Screen_center_y
    #print("x_coord: " + str(x_coord) + " y_coord: " + str(y_coord))
    
    #pygame.draw.circle(screen, "red",(x_coord, y_coord), size, 0)   # displaying the cartography via pygame






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

    #portChoisi = int(input("Choose a port: "))   # choosing port
    portChoisi = 1
    baud = 115200

    # Establishing serial connection 
    arduino = serial.Serial(ports[int(portChoisi) -1  ].device, baud, timeout = 0.5)
    
    print('Connection to ' + arduino.name + ' at ' + str(baud) + ' baud was succesful! ')

    
    # printing decoded data if received
    while True:
        data = arduino.readline().decode('ascii').rstrip() 
        #print(data)
        
        if len(data) > 0:

            datasplit=data.split(' , ') 
            if len(datasplit) == 2 and (datasplit != " " ):     # making sure the data is in the right format 
                angle = int(datasplit[0])
                distance = 0
                distance = float(datasplit[1])
                x = distance*math.cos(angle*(math.pi/180))    # calculating cartesian coordinates
                y = distance*math.sin(angle*(math.pi/180))

                IRL_coordinates[angle][0] = x       # assigning the coordinates into a numpy array for the corresponding angle
                IRL_coordinates[angle][1] = y

                #print(angle)
                #print(y)


                #time.sleep(1)

                if (angle == 180 or angle == 0):    # resesting the screen once a full scan has been made
                    screen.fill("black")
                    
                #print (B)   # for testing purposes
                
                # d=90
                # for i in range (1,17): 
                #     pygame.draw.line(screen,'white',(0,(i/10)*(tailley-image.get_height())/2+10),(taillex,(i/10)*(tailley-image.get_height())/2+10))    # displaying the grid (scale)
                #     text = font.render(str(d)+" cm",1,(255,255,255))
                #     screen.blit(text, (1850,(i/10)*(tailley-image.get_height())/2-5 ))
                #     d = d-6

                

                pygame.draw.line(screen,'white',(0, screen_size_y),(screen_size_x, 0))
                pygame.draw.line(screen,'blue',(0, Screen_center_y),(screen_size_x, Screen_center_y))    # displaying the grid (scale) y axis 
                #text = font.render(str(0)+" cm", 1, (255,255,255))
                #screen.blit(text, (1850, Screen_center_y - 15 ))
                
                pygame.draw.line(screen,'blue',(Screen_center_x, screen_size_y),(Screen_center_x, -screen_size_y))
                

                y_scale_max = 100
                #for i in range (-10,11): 
                #for i in range(-10, 0) + range(1, 11):
                for i in [x for x in range(-10, 11) if x != 0]:

                    pygame.draw.line(screen,'white',(0, Screen_center_y - i*50),(screen_size_x, Screen_center_y - i*50))    # displaying the grid (scale) y axis 
                    #pygame.draw.line(screen,'white',(Screen_center_x, tailley),(Screen_center_x, -tailley))    # displaying the grid (scale) x axis
                    
                    

                
                for i in range(-10, 11):
                    # Calcul de la position où le texte sera affiché
                    text_position = (1850, Screen_center_y - i * 50 - 15)

                    # Efface la zone précédente en dessinant un rectangle de fond
                    # Assurez-vous que la taille du rectangle soit suffisante pour couvrir l'ancien texte
                    background_rect = pygame.Rect(text_position[0], text_position[1], 70, 20)
                    screen.fill("black", background_rect)

                    # Génération et affichage du nouveau texte
                    #text = font.render(str(int(- x_scale_max)) + " cm", 1, (255, 255, 255))
                    text = font.render(str(int(- y_scale_max * calculate_scale_factor(np.max(IRL_coordinates[:, 1])))) + " cm", 1, (255, 255, 255))
                    screen.blit(text, text_position)

                    # Mise à jour de la variable x_scale_max
                    y_scale_max = y_scale_max - 10
                
                    
                # screen.blit(image, Screen_center_y)    
                
                if float(datasplit[1])>10: #only displaying the cartography if the distance is greater than 10 cm
                    #draw_points(screen, B[angle][0], B[angle][0])
                    draw_points(screen, IRL_coordinates[angle][0], IRL_coordinates[angle][1], angle)


                pygame.display.flip()   

        for event in pygame.event.get():    # quitting pygame interface
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            
else: 
    print("No active port was found")

