# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 02:53:27 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt
import Praktikummo2 as p
from scipy.interpolate import interp1d

data = np.genfromtxt("../Daten/4_2K.txt", delimiter = '',skip_header = 4)

B1 = data[:,0]
cutoff = p.find_nearest(B1,-0.1)
B = B1[:]
Rxx = data[:,2]
Rxy = data[:,4]
phase1 = data[:,3]
phase2 = data[:,5]
zeros, = np.where(B == 0)
B = np.delete(B, zeros)
Rxx = np.delete(Rxx, zeros)
#a = p.find_nearest(B,-0.1)
#b = p.find_nearest(B,0.1)
#B = np.append(B[:a],B[b:])
#Rxx = np.append(Rxx[:a],Rxx[b:])

f = interp1d(1./B, Rxx)
x = np.linspace(min(1./B),max(1./B),1e7)
freq,amp = p.fourier_fft(x,f(x))
print freq[p.find_nearest(freq,8)+np.argmax(amp[p.find_nearest(freq,8):p.find_nearest(freq,10)])]
#f = interp1d(1./B, Rxx)
#x = np.linspace(min(B),max(B),1e5)
#x = 1./x
#freq,amp = p.fourier_fft(x,f(x))
plt.figure(1)
plt.plot(freq[:len(freq)/2],amp[:len(freq)/2])
plt.xlim([0,40])
plt.ylim([0,100000])

plt.figure(2)
plt.plot(B,Rxx)