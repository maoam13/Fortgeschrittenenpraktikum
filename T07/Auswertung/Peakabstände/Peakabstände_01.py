# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:56:05 2018

@author: grldm
"""

import Praktikum as p
import Peakabstaende_Funktionen as func
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

delta_t = []
for i in range(16):
    j = i % 10
    k = (i - j) / 10
    delta = func.get_delta_t(k, j, 0.01)
    for n in range(len(delta)):
        delta_t.append(delta[n])

#Daten für Fit aufbereiten
bin_breite = 0.0005
num = int(np.round(0.035/bin_breite) + 1)
y = np.full(num, 0)
t = []
for i in range(num):
    t.append(i * bin_breite)
for i in range(len(t) - 1):
    for j in range(len(delta_t)):
        if delta_t[j] < t[i + 1] and delta_t[j] > t[i]:
            y[i] += 1

#Daten für Fit anpassen
x = np.arange(max(y))
y_kom = np.full(max(y), 0)
for i in range(int(max(y))):
    for j in range(len(y)):
        if y[j] == i:
            y_kom[i] += 1

#Fit
def func(A, x):
    return A[0] * np.exp(-A[0] * x)

#sol = AM.fitte_bel_function(x, y_kom/sum(y_kom), np.full(len(x), 0.1), np.full(len(y), 0.1), func, [25])
sol = AM.fitte_bel_function(x, y_kom/sum(y_kom), np.full(len(x), 1.0/sum(y_kom)), np.full(len(y_kom), 4./sum(y_kom)), func, [0.3])
print sol

#mittelwert (und std) ausrechnen und aus erwartung dann chi^2 ausrechnen
mu = np.mean(y_kom)
std = np.std(y_kom, ddof = 1)
chi_mu = AM.chiq_y(x[0:7], y_kom[0:7], np.sqrt(y_kom[0:7]), func, [1./mu])
chi_std = AM.chiq_y(x[0:7], y_kom[0:7], np.sqrt(y_kom[0:7]), func, [1./std])

#Plot
plt.figure(1)
plt.hist(y, bins = x, normed = True)
plt.figtext(0.4,0.42,
            '$\chi ^2$ Anpassung in rot: \n'
            +'Modell: rho ($\Delta$t) = A $\cdot$ $e^{- A \cdot \Delta t}$'
            +'\n A= ('+str(np.round(sol[0][0],6))+' +/- '+str(np.round(sol[1][0],6))+') $1/s$ \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(sol[2], 3)) + '\n'
            +'\n Erwartung aus Mittelwert in gruen'
            +'\n A= '+str(np.round(1./mu,6))+'\n'
            +'$\chi ^2 / ndof$= ' + str(np.round(chi_mu, 3)) + '\n'
            +'\n Erwartung aus Standardabweichung in gelb'
            +'\n A= '+str(np.round(1./std,6))+'\n'
            +'$\chi ^2 / ndof$= ' + str(np.round(chi_std, 3)) + '\n')
plt.xlabel('Anzahl der gemessenen $\Delta$ t in einem Intervall')
plt.ylabel('relative Haeufigkeit der Anzahlen')
plt.title('Zeitabstaende zwischen Peaks bei Intervallbreite ' + str(bin_breite * 1000) + ' ms.')
plt.plot(x, func([sol[0][0]],x), color = 'r')
plt.plot(x, func([1./mu],x), color = 'g')
plt.plot(x, func([1./std],x), color = 'y')


print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))