"""

This program introduces popular libraries for science use

LIBRARIES

matplot doc: https://matplotlib.org/
numpy doc: https://www.geeksforgeeks.org/python-numpy/
math doc: https://docs.python.org/3/library/math.html 

Star this GitHub: https://github.com/rasbt/matplotlib-gallery/blob/master/ipynb/lineplots.ipynb

"""

import matplotlib.pyplot as plt # Formats graphs
import numpy as np # Nicely manipulates arrays (Great for matricies)

# X axis data 
time = np.arange(-3, 14, 0.01) # (start, finish, step)

# Y axis data for superimposed graphs
position = -time**2 + 10 * time + 21
velocity = -2 * time + 10
acceleration = -2 + 0 * time # interesting data type error... list vs arrays?

# Organize data and intialize to superimpose on 1 figure 
fig, ax1 = plt.subplots() # intializes plot
ax1.plot(time, position, label = "Position") # set up axis relationships
ax1.plot(time, velocity, label = "Velocity")
ax1.plot(time, acceleration, label = "Acceleration")
ax1.legend()

# Graph lables/design for first figure
ax1.set(xlabel = "Time (s)", ylabel = "Meters (m)", title="Position Plot with Superimposed Derivatives")
ax1.grid() # Intializes grid
plt.xlim(-2.5, 14) # Nice for zooming in on graphs
plt.ylim(-17, 50)

# Display/Save figure
plt.show() # display figure
#fig.savefig("example_graph.png") 
