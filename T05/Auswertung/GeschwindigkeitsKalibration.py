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

i = 1
index = ['1', 'einlinien_echt', 'Extiktion', 'hyperfein', 'quadrupol']
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
'''
def cos(A, x):
    return A[0] * np.cos(A[1] * x)

A, sig_A, chiq = AM.fitte_bel_function(data_x, data_y, sig_x, sig_y, cos, startwerte)

c = 300000 * 10**6
v = data/(45 * 3160.56)
E = 14.4 * (1 + v/c)
'''

#Teste Methode
E1, sig_E1, v1, sig_v1 = test.Kalibration(2)



plt.figure(1)
plt.errorbar(data_x, data_y, xerr = sig_x, yerr = sig_y, fmt = ',', linewidth = 3, color = 'b', label = 'Messung')
#plt.plot(data_x, abs_cos(A, data_x), color = 'r', label = 'Anpassung')
#plt.plot(data_x, v, color = 'g', label = 'Geschwindigkeit')
#plt.plot(data_x, E, color = 'g', label = 'Energie')
#plt.figtext(0.23,0.72,
#            'Model: y = A $\cdot$ cos($\omega \cdot x$)'
#            +'\n A= '+str(np.round(A[0],2))+' +/- '+str(np.round(sig_A[0],2))+' '
#            +'\n $\omega$= ('+str(np.round(A[1],8))+' +/- '+str(np.round(sig_A[1],8))+') $1/s$ \n'
#            +'$\chi ^2 / ndof$= ' + str(np.round(chiq, 3)))
plt.xlabel('Chanel')
plt.ylabel('counts')
#plt.ylim(14.3, 14.5)
#plt.legend()
plt.title('Geschwindigkeitsmessung')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))