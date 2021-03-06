# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:36:53 2019

@author: Moritz
"""

import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("../Daten/Magnetic/amplitude_bias.dat", delimiter = '')
font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 12}
x = data[:,2]
y = data[:,4]/(2*np.pi)*360
ey = np.full(len(y),0.01)
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

bereich = 1000
start = find_nearest(x,-bereich)
ende = find_nearest(x,bereich)
def f(B, x):
        return B[0]*(x-B[1])**2 + B[2]
fit,dfit,res = p.fitte_bel_function(x[start:ende],y[start:ende],ey[start:ende],f,[1,100,-100])

plt.figure("top")
plt.rc('font', **font)
plt.plot(x,y)
plt.plot(x[start:ende],f(fit,x[start:ende]))
plt.grid()
#plt.ylabel("Phase [$^o$]")
plt.ylabel("Phase [$^o$]", **font)
plt.xlabel("V [mV]", **font)
print fit[1],dfit[1]

V,dV,dV2 = p.gew_mittelwert(np.array([151.7,174.8]),np.array([0.3,1.6]))
print V*1.6*10**-19/1000,dV*1.6*10**-19/1000