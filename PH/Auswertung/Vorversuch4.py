# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:13:31 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Vorversuch 4/Integrationszeit.CSV", delimiter = ';', skip_header = 1)
        
plt.close("all")
index = 0
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]/50


plt.figure("Vor4_"+str(index))
ax = plt.subplot(111)
plt.plot(x,y)
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Frequenz[Hz]")
ax.set_ylabel("Amplitude[mV]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Vorversuch4/Vor4_"+str(index))
