# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 10:55:29 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import STM_Methoden as STMM

start_time=timeit.default_timer()

data_index = [52, 80, 100, 200, 400, 600, 2000]
data_nach = []
data_vor = []
for i in range(len(data_index)):
    data_nach.append(STMM.lese_Profillinie_ein_Zeit(data_index[i], vor = 0))
    data_vor.append(STMM.lese_Profillinie_ein_Zeit(data_index[i], vor = 1))

peak_approx = [92, 160]
peaks_nach = []
for i in range(len(data_nach)):
    peak = STMM.get_peak_by_approx(data_nach[i][:,0], data_nach[i][:,1], peak_approx)
    peaks_nach.append(peak)
peaks_vor = []
for i in range(len(data_vor)):
    peak = STMM.get_peak_by_approx(data_vor[i][:,0], data_vor[i][:,1], peak_approx)
    peaks_vor.append(peak)

#Berechne Flankensteigung als Mittelwert aus Vor- und Rückrichtung 
steigung = STMM.steigung_bestimmen(peaks_nach, peaks_vor)

#Berechne Abstände der Peaks zwischen Vor- und Rückrichtung
abst = STMM.peak_abstaende(peaks_nach, peaks_vor)

#Plotte Datensatz e
e = 1
plt.figure(1)
x = [(peaks_nach[e][0][0] + peaks_vor[e][0][0])/2, (peaks_nach[e][1][0] + peaks_vor[e][1][0])/2]
y = [(peaks_nach[e][0][1] + peaks_vor[e][0][1])/2, (peaks_nach[e][1][1] + peaks_vor[e][1][1])/2]
plt.plot(x, y, color = 'r')
plt.figtext(0.15,0.75,
            'a= '+ str(np.round(steigung[e],5)) + '\n'
            +'$\Sigma$= ' + str(np.round(abst[e], 5)))
plt.plot(data_nach[e][:,0], data_nach[e][:,1], color = 'b')
plt.plot(data_vor[e][:,0], data_vor[e][:,1], color = 'g')
for i in range(len(peaks_nach[e])):
    plt.axvline(peaks_nach[e][i][0], color = 'b')
for i in range(len(peaks_vor[e])):
    plt.axvline(peaks_vor[e][i][0], color = 'g')
plt.xlabel('X [nm]')
plt.ylabel('Z [nm]')
plt.title('Hoehenprofil bei {0:5.0f} ms Messzeit'.format(data_index[e]))

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))