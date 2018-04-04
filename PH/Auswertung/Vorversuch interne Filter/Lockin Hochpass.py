# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:22:23 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

data = np.genfromtxt("../../Daten/Vorversuch 2/lockin Hochpass.csv", delimiter = ';', skip_header = 1)

f, A, B = AM.sortieren([data[:,0], data[:,1], data[:,2]], 0)
sA = 0.001/np.sqrt(12)
sB = 0.001/np.sqrt(12)
sf = np.full(len(f), 1./np.sqrt(12))

#Plotte Tiefpass Kennlinie
plt.close('all')
plt.figure(1)
#ax1 = plt.subplot(211)
plt.errorbar(f, A, xerr = sf, yerr = sA, fmt = '.', color = 'b', label = 'Messung mit Multimeter')
plt.errorbar(f, B, xerr = sf, yerr = sB, fmt = '.', color = 'y', label = 'Messung mit Oszilloskop')
plt.title('Kennlinie Lockin Hochpass')
#plt.ylabel('$\dfrac{U_a}{U_e}$')
plt.ylabel('$U_a$ [V]')
plt.legend()

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))