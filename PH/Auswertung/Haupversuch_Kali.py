# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:29:28 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        datei = ["Abkuhlung_supraX1_kalibriert","Phasenkalibration",]
        self.data = np.genfromtxt("../Daten/Hauptversuch/"+datei[index]+".dat", delimiter = '\t',dtype = np.float)
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

plt.close("all")
index = 1
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]

cut = find_nearest(x,116)
x1 = x[:cut]
y1 = y[:cut]
x = x[cut:]
y = y[cut:]

cut = find_nearest(x,83.5)
x2 = x[:cut]
y2 = y[:cut]
x = x[cut:]
y = y[cut:]
"""
cut = find_nearest(x,116)
cut3 = find_nearest(x,95)
x3 = x[:cut]
y3 = y[:cut]
x = x[cut3:]
y = y[cut3:]
"""

plt.figure("Vor3_"+str(index))
ax = plt.subplot(111)
plt.plot(x2,y2)
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
#plt.savefig("../Protokoll/Bilder/Hauptversuch/Kal_"+str(index))