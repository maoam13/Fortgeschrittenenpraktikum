# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:48:35 2018

@author: morit
"""
import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Vorversuch 3/ALL000"+str(index)+"/F000"+str(index)+"CH3.CSV", delimiter = ',', skip_header = 1)
plt.close("all")
index = 5
data = Einlesen(index).data

x = data[:,3]
y = data[:,4]
f,amp = p.fourier_fft(x,y)

plt.figure("Vor3_"+str(index))
ax = plt.subplot(111)
plt.plot(f,amp)
plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Frequenz[Hz]")
ax.set_ylabel("Amplitude")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Vorversuch 3/Vor3_"+str(index))
