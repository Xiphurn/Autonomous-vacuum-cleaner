import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import math
from matplotlib.animation import FuncAnimation
import serial

# Setup Arduino connection (adjust the port and baud rate as needed)
arduino = serial.Serial('COM5', 2000000)  

def get_lidar_data():
    while True:
        data = arduino.readline().decode('ascii').rstrip()
        if len(data) > 0:
            datasplit = data.split(' , ')
            if len(datasplit) == 2 and (datasplit != " "):
                angle = int(datasplit[0])
                distance = float(datasplit[1])
                x = distance * math.cos(angle * (math.pi / 180))
                y = distance * math.sin(angle * (math.pi / 180))
                #print(x, y)
                yield x, y

def plot_lidar_data():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    scatter = ax.scatter([], [], c='blue', s=5)
    # ax.set_ylim(0, 1)  # Remove static limit

    # Using deque as a circular buffer
    data_buffer = deque(maxlen=360)
    
    # Update function for the animation
    def update(frame):
        data_buffer.append(frame)
        theta, r = zip(*[(np.arctan2(y, x), np.sqrt(x**2 + y**2)) for x, y in data_buffer])
        
        # Update scatter plot data
        scatter.set_offsets(np.column_stack([theta, r]))

        # Adjust r-axis limits dynamically
        max_distance = max(r, default=1)
        ax.set_ylim(0, max_distance)

    # Create animation
    ani = FuncAnimation(fig, update, frames=get_lidar_data, interval=1, blit=False)

    plt.show()

# Call the function to start plotting
plot_lidar_data()
