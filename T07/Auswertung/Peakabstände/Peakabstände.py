# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:45:23 2018

@author: Gerald
"""

import Praktikum as p
import Peakabstaende_Funktionen as func
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

#data = np.genfromtxt("ALL0000/F0000CH1.csv", delimiter = ',')
#schwelle = 0.01
#index = AM.get_werte_ab_schwelle(data[:,4], schwelle)
#delta_t = []
#for i in range(len(index) - 1):
#    delta_t.append(data[index[i+1],3] - data[index[i],3])


delta_t_func = func.get_delta_t(0, 0, 0.01)

delta_t = []
for i in range(16):
    j = i % 10
    k = (i - j) / 10
    delta = func.get_delta_t(k, j, 0.01)
    for n in range(len(delta)):
        delta_t.append(delta[n])

#Daten für Fit aufbereiten
bin_breite = 0.001
num = int(np.round(0.035/bin_breite))
y = np.full(num, 0)
t = []
for i in range(num):
    t.append(i * bin_breite)
for i in range(len(t) - 1):
    for j in range(len(delta_t)):
        if delta_t[j] < t[i + 1] and delta_t[j] > t[i]:
            y[i] += 1

# Fit
def func(A, x):
    return A[0] * np.exp(-A[0] * x)

#mogl = []
#for i in range(1000):
#    sol = AM.fitte_bel_function(t, y, np.full(num, bin_breite/np.sqrt(12)), np.full(num, 1), func, [i * 0.01])
#    if sol[2] != 0:
#        mogl.append(sol)

#print mogl

sol = AM.fitte_bel_function(t, y, np.full(num, bin_breite/np.sqrt(12)), np.full(num, 1.5), func, [8])
print sol

#plotte Fit in histogramm
x_fit = np.array(t)
y_fit = func([16],x_fit)#[sol[0][0]], x_fit)

#Histogramm von Zeitabständen
bins_U = np.arange(np.min(delta_t),np.max(delta_t), bin_breite)
plt.figure(1)
plt.hist(np.array(delta_t),bins=bins_U)
plt.xlabel('$\Delta$ t [s]')
plt.ylabel('#')
plt.title('Zeitabstaende zwischen Peaks')
#plt.plot(x_fit, y_fit, color = 'r')


print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))