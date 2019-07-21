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
"""
#font = {'family' : 'normal',
#            'weight' : 'bold',
#            'size'   : 10}

fig = plt.figure()
#plt.rc('font', **font)
plt.plot(x,y)
plt.grid()
plt.ylabel("Amplitude", **font)
plt.xlabel("Frequency [kHz]", **font)
test = plt.axis()
plt.vlines(76.02,0,10,color = "red",linestyle = "dashed")
plt.axis(test)
"""
fig = plt.figure()
x = np.arange(0,100,0.01)
def func(x):
    return 160. * 1.96**(-4) * (np.exp(-np.pi/x**2) - np.exp(-np.pi*3.1**2/x**2))
plt.plot(x,func(x))
plt.hlines(0.5,0,100,color = "red",linestyle = "dashed",label = "point 1")
plt.hlines(0.06,0,100,color = "blue",linestyle = "dashed",label = "point 2")
plt.grid()
plt.xlabel("$L_D$[nm]")
plt.ylabel("$I_D/I_G$")
plt.legend()