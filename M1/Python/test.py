# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:58:48 2019

@author: Moritz
"""
import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("../Daten/Magnetic/Resonanz_Freq_nah.dat2", delimiter = '')
x = data[:,0]/1000
y = data[:,1]

font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

fig = plt.figure()
plt.rc('font', **font)
plt.plot(x,y)
plt.grid()
plt.ylabel("Amplitude", **font)
plt.xlabel("Frequency [kHz]", **font)
test = plt.axis()
plt.vlines(76.02,0,10,color = "red",linestyle = "dashed")
plt.axis(test)