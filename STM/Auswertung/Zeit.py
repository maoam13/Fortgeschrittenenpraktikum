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

#abgelesene Werte für Peaks
peak_vor_x = [[33.0, 51.1], [22.2, 54.8], [38.6, 54.2], [18.7, 53.8], [36.5, 53.1], [27.6, 52.7], [43.6, 62.8]]
peak_vor_y = [[0.0, 3.5], [0.0, 3.6], [0.0, 3.4], [0.0, 4.2], [0.0, 3.1], [0.0, 3.4], [0.0, 3.1]]
peak_nach_x = [[28.5, 45.3], [20.2, 46.0], [35.2, 50.9], [15.5, 48.4], [33.6, 50.7], [24.6, 48.6], [38.8, 57.0]]
peak_nach_y = [[0.0, 3.4], [0.0, 3.5], [0.0, 3.7], [0.0, 4.2], [0.0, 3.5], [0.0, 3.3], [0.0, 2.7]]
st_vor, st_nach, st_vor_std, st_nach_std = STMM.alt_steigung(peak_vor_x, peak_vor_y , peak_nach_x, peak_nach_y)

#Abweichung zwischen Steigung aus Vorwaerts- und Rueckwaertsrichtung
abw = (np.array(st_vor) - np.array(st_nach))/np.sqrt(np.array(st_vor_std)**2 + np.array(st_nach_std)**2)


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

#Plotte Datensatz e mit abgelesenen Peaks
plt.figure(2)
plt.figtext(0.2,0.75,
            '$a_{vor}$= '+ str(np.round(st_vor[e],5)) + '$\pm$' + str(np.round(st_vor_std[e],5)) + '\n'
            +'$a_{rueck}$= '+ str(np.round(st_nach[e],5)) + '$\pm$' + str(np.round(st_nach_std[e],5)) + '\n'
            +'$\Sigma$= ' + str(np.round(abst[e], 5)))
plt.plot(data_nach[e][:,0], data_nach[e][:,1], color = 'b')
plt.plot(data_vor[e][:,0], data_vor[e][:,1], color = 'g')
for i in range(len(peak_nach_x[e])):
    plt.axvline(peak_nach_x[e][i], color = 'b')
    plt.axvline(peak_vor_x[e][i], color = 'g')
    plt.plot(peak_vor_x[e], peak_vor_y[e], color = 'r')
    plt.plot(peak_nach_x[e], peak_nach_y[e], color = 'r')
plt.xlabel('X [nm]')
plt.ylabel('Z [nm]')
plt.title('Hoehenprofil bei {0:5.0f} ms Messzeit'.format(data_index[e]))

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))