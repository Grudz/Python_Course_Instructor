# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:00:27 2020

@author: Ben
"""
# Enter help('module') in shell to see all imports https://www.tutorialsteacher.com/python/python-builtin-modules
# Refer to: https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mGalarnyk/Python_Tutorials/master/Kaggle/BreastCancerWisconsin/data/data.csv')

malignant = df[df['diagnosis']=='M']['area_mean']
benign = df[df['diagnosis']=='B']['area_mean']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot([malignant,benign], labels=['M', 'B'])

