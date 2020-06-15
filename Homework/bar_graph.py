# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:30:07 2020

@author: Ben

Refer to: https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm

"""
# Bar Graph/Lists homework

import matplotlib.pyplot as plt
import numpy as np

coolness_level = [36, 43, 95, 69] # X-axis data
person = ["Lonzo Ball", "Loren Gray", "Ben Grudzien", "George Lopez"] # Y-axis data

fig, ax = plt.subplots()
fig.suptitle("How cool is Ben? (100 coolness = coolest person to ever live)")
ax.bar(person[0], coolness_level[0], color = "b", width = 0.5)
ax.bar(person[1], coolness_level[1], color = "r", width = 0.6)
ax.bar(person[2], coolness_level[2], color = "g", width = 1)
ax.bar(person[3], coolness_level[3], color = "y", width = 0.7)
ax.set(xlabel = "People", ylabel = "Coolness Level")

ax.set_yticks(np.arange(0, 110, 10))

