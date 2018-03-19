# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:21:05 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

data_v0 = np.genfromtxt("../Daten/GR2830/Quellspektrum v0_echt.ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
data_vinf = np.genfromtxt("../Daten/GR2830/Quellspektrum vinf.ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
data_x = np.arange(len(data_v0))

sig_x = np.full(len(data_x), 1./np.sqrt(12))
sig_v0 = np.sqrt(data_v0)
sig_vinf = np.sqrt(data_vinf)

def gauss_fit(x, y, sx, sy, startwerte):
    def gauss(A, x):
        #A = [sig, mu]
        return 1./np.sqrt(2 * np.pi * A[0]**2) * np.exp(-(x - A[1])**2 / (2 * A[0]**2))
    A, sig_A, chiq = AM.fitte_bel_function(x, y, sx, sy, gauss, startwerte)
    return A, sig_A, chiq

A, sig_A, chiq = gauss_fit(data_x[481:600], data_v0[481:600], sig_x[481:600], sig_v0[481:620], [548, 20])
channels = np.array([97,546,996])
ka = 6.4
E = np.array([ka,14.4,14.4+ka])
dx = np.array([2,5,1])
a,da,b,db,chi,mull = p.lineare_regression(channels,E,dx)

plt.figure(1)
plt.plot(data_x, data_v0, color = 'b', label = 'v = 0')
plt.plot(data_x, data_vinf, color = 'g', label = 'v = $\infty$')
plt.xlabel('Chanel')
plt.ylabel('counts')
plt.legend()
plt.title('Quellspektrum')
x = np.arange(0,1024)
plt.figure(2)
plt.plot(x,a*x+b)
plt.errorbar(channels,E,xerr=dx,fmt='.')
plt.xlabel('Chanel')
plt.ylabel('counts')
plt.legend()
plt.title('Quellspektrum')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))