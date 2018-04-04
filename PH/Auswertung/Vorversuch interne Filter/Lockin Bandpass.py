# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:23:10 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

data = np.genfromtxt("../../Daten/Vorversuch 2/lockin Bandpass.csv", delimiter = ';', skip_header = 1)

f, A, B = AM.sortieren([data[:,0], data[:,1], data[:,2]], 0)
sA = np.full(len(A), 0.001/np.sqrt(12))
sB = np.full(len(B), 0.001/np.sqrt(12))
sf = np.full(len(f), 1./np.sqrt(12))

#fitte Funktion zur Bestimmung der Grenzfrequenz
def band(A, x): # A = [2D/w_0, w_0, max]
    return A[2] * (A[0] * x)/(1 + A[0] * x + (x/A[1])**2)
def band_abl(A, x):
    return -x/(A[0]**2 * (1 + (x/A[0])**2)**(3/2))

w_0 = np.log(2 * np.pi * 1000)
sol = AM.fitte_bel_function(f, A, sf, sA, band, [1./w_0, w_0, 2])

#Plotte Tiefpass Kennlinie
plt.close('all')
plt.figure(1)
ax1 = plt.subplot(111)
#ax1.set_xscale("log", nonposx = 'clip')
plt.errorbar(f[:48], A[:48], xerr = sf[:48], yerr = sA[:48], fmt = '.', color = 'b', label = 'Messung mit Multimeter')
#plt.plot(f[:48], band(sol[0], f[:48]), color = 'r')
#plt.errorbar(f, A, xerr = sf, yerr = sA, fmt = '.', color = 'y', label = 'Messung mit Oszilloskop')
plt.title('Kennlinie Lockin Bandpass')
#plt.ylabel('$\dfrac{U_a}{U_e}$')
plt.ylabel('$U_a$ [V]')
plt.legend()

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))