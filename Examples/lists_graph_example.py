# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:55:23 2020

@author: Ben

Refer to this GitHub: https://github.com/rasbt/matplotlib-gallery/blob/master/ipynb/lineplots.ipynb
"""
import matplotlib.pyplot as nugget

# Graph with lists example

days = [1, 2, 3, 4] # x-axis data

alive_mice_with_drug = [20, 18, 6, 1] # y axis data (Could be floats)
alive_mice_without_drug = [20, 19, 15, 10]
alive_mice_with_drug_err = [0, 2, 0.5, 1] # y axis data error
alive_mice_without_drug_err = [0, 0, 2, 1]

#nugget.plot(days, alive_mice_with_drug, marker = "*")
#nugget.plot(days, alive_mice_without_drug, marker = "^")
nugget.errorbar(days, alive_mice_with_drug, yerr = alive_mice_with_drug_err, fmt='-x')
nugget.errorbar(days, alive_mice_without_drug, yerr = alive_mice_without_drug_err, fmt='-^')

day_labels = ["day 1", "day 2", "day 3", "day 4"]
nugget.xticks(days, day_labels)
nugget.xlabel("Total Days")
nugget.ylabel("Alive Mice")
nugget.title("Harsh Environment: Mouse Drug Experiment")
nugget.legend(["Mice with drugs", "Mice without drugs"], loc = "lower left")
nugget.show()
