"""

This program introduces popular libraries for science use

LIBRARIES

matplot doc: https://matplotlib.org/
numpy doc: https://www.geeksforgeeks.org/python-numpy/
math doc: https://docs.python.org/3/library/math.html 

EXTRA REOSOURCES

Star this GitHub: https://github.com/rasbt/matplotlib-gallery/blob/master/ipynb/lineplots.ipynb
Layout Help: https://matplotlib.org/3.2.1/tutorials/intermediate/tight_layout_guide.html

"""

import matplotlib.pyplot as plt # Formats graphs
import numpy as np # Nicely manipulates arrays (Great for matricies)
# import math # Enables some convenient math functions, issue with array I dont understand right now

# X axis data 
time = np.arange(0, 14, 0.01) # (start, finish, step)

# Y axis data for superimposed graphs
cos_fucntion = np.cos(time) # math.cos gives scaler/array type error
sin_fucntion = np.sin(time)

# Organize data and intialize to superimpose on 1 figure 
fig, ax = plt.subplots(2) # intializes plot
#fig.suptitle("Trigometric Function Comparison")
fig.tight_layout()
ax[0].plot(time, cos_fucntion, label = "Voltage") # set up axis relationships
ax[0].legend()
ax[1].plot(time, sin_fucntion, label = "Voltage", color = "red") # set up axis relationships
ax[1].legend()

# Graph lables/design for first figure
ax[0].set(xlabel = "Time (s)", ylabel = "Voltage (V)", title="Cos Function")
ax[0].grid() # Intializes grid
ax[1].set(xlabel = "Time (s)", ylabel = "Voltage (V)", title="Sin Function")
ax[1].grid() # Intializes grid

# Display/Save figure
fig.tight_layout()
plt.show() # display figure
#fig.savefig("trig_subplots.png") 

