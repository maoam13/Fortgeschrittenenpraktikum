# -*- coding: utf-8 -*-
"""
Created on Sun Jun 09 23:19:39 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt
import Praktikummo2 as p

data = np.genfromtxt("../Daten/4_2K.txt", delimiter = '',skip_header = 4)

B = data[:,0]
Rxx = data[:,2]
Rxy = data[:,4]
phase1 = data[:,3]
phase2 = data[:,5]

freq,amp = p.fourier_fft(1./B,Rxx)

plt.plot(freq,amp)
plt.xlim([0,100])