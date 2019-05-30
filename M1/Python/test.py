# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:58:48 2019

@author: Moritz
"""
import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("../Daten/Magnetic/Resonanz_Freq_nah.dat2", delimiter = '')
x = data[:,0]
y = data[:,1]

plt.plot(x,y)