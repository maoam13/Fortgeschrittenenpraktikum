# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:13:41 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import Kalibration_Methode as test

start_time=timeit.default_timer()

i = 0
index = ['1', 'einlinien_echt', 'Extiktion', 'hyperfein', 'quadrupol']
title = ['m Quellspektrum', 'm Einlinienspektrum', 'm Extinktionwirkungsquerschnitt', 'r Hyperfeinstrukturaufspaltung', 'r Quadrupolaufspaltung']
data = np.genfromtxt("../Daten/GR2830/v kalibration " + index[i] + ".ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
sig_y = np.full(len(data), 2.)
startwerte = [1000, np.pi/(766-251)]
data_x = np.arange(len(data))
sig_x = np.full(len(data_x), 1./np.sqrt(12))

#abgelesene Nulldurchgänge
zeros_1 = [255, 256, 255, 255, 255]
zeros_2 = [767, 766, 767, 766, 767]

#"drehe" mittlere Daten um
data_y = []
for j in range(len(data)):
    if j > zeros_1[i] and j < zeros_2[i]:
        data_y.append(-data[j])
    else:
        data_y.append(data[j])

def cos(A, x):
    return A[0] * np.cos(A[1] * x)

A, sig_A, chiq = AM.fitte_bel_function(data_x, data_y, sig_x, sig_y, cos, startwerte)

#Teste Methode
E1, sig_E1, v1, sig_v1 = test.Kalibration(i)

plt.figure(1)
ax = plt.subplot(111)
plt.errorbar(data_x, data_y, xerr = sig_x, yerr = sig_y, fmt = ',', linewidth = 2, color = 'b', label = 'Messung')
plt.plot(data_x, cos(A, data_x), color = 'r', label = 'Anpassung')
plt.figtext(0.35,0.72,
            'Model: y = A $\cdot$ cos($\omega \cdot x$)'
            +'\n A= '+str(np.round(A[0],2))+' +/- '+str(np.round(sig_A[0],2))+' '
            +'\n $\omega$= '+str(np.round(A[1],8))+' +/- '+str(np.round(sig_A[1],8))+' \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(chiq, 3)))
plt.xlabel('Chanel')
plt.ylabel('n')
plt.legend()
plt.title('Geschwindigkeitsmessung zu' + title[i])

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))