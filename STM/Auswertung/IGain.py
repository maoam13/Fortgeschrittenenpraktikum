# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 14:25:43 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import STM_Methoden as STMM

start_time=timeit.default_timer()

data_index = [1, 3, 8, 11]
data_nach = []
for i in range(len(data_index)):
    bla = STMM.lese_Profillinie_ein(data_index[i] * 1000, vor = 0)
    data_nach.append(bla)
data_vor = []
for i in range(len(data_index)):
    bla = STMM.lese_Profillinie_ein(data_index[i] * 1000, vor = 1)
    data_vor.append(bla)

peak_approx = [26, 48, 86, 131]
peaks_nach = []
for i in range(len(data_nach)):
    peak = STMM.get_peak_by_approx(data_nach[i][:,0], data_nach[i][:,1], peak_approx)
    peaks_nach.append(peak)
peaks_vor = []
for i in range(len(data_vor)):
    peak = STMM.get_peak_by_approx(data_vor[i][:,0], data_vor[i][:,1], peak_approx)
    peaks_vor.append(peak)

#Berechne Flankensteigung als Mittelwert aus Vor- und Rückrichtung 
steigung_nach = []
steigung_vor = []
for i in range(len(peaks_nach[0])):
    st = (peaks_nach[i][3][1] - peaks_nach[i][2][1])/(peaks_nach[i][3][0] - peaks_nach[i][2][0])
    steigung_nach.append(st)
    st = (peaks_vor[i][3][1] - peaks_vor[i][2][1])/(peaks_vor[i][3][0] - peaks_vor[i][2][0])
    steigung_vor.append(st)

steigung = []
for i in range(len(steigung_vor)):
    steigung.append((steigung_vor[i] + steigung_nach[i])/2)

#Plotte Datensatz e
e = 0
plt.figure(1)
x = [(peaks_nach[e][2][0] + peaks_vor[e][2][0])/2, (peaks_nach[e][3][0] + peaks_vor[e][3][0])/2]
y = [(peaks_nach[e][2][1] + peaks_vor[e][2][1])/2, (peaks_nach[e][3][1] + peaks_vor[e][3][1])/2]
plt.plot(x, y, color = 'r')
plt.plot(data_nach[e][:,0], data_nach[e][:,1], color = 'b')
plt.plot(data_vor[e][:,0], data_vor[e][:,1], color = 'g')
for i in range(2, len(peaks_nach[e])):
    plt.axvline(peaks_nach[e][i][0], color = 'b')
for i in range(2, len(peaks_vor[e])):
    plt.axvline(peaks_vor[e][i][0], color = 'g')
plt.xlabel('X [nm]')
plt.ylabel('Z [nm]')
plt.title('Hoehenprofil')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))