# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:41:24 2018

@author: grldm
"""

import Praktikum as p
import Peakabstaende_Funktionen as func
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

data = np.genfromtxt("GMgauss.csv", delimiter = ',')

x = np.arange(min(data),max(data))
y = np.full(len(x), 0)
for i in range(len(x)):
    for j in range(len(data)):
        if data[j] == i + min(data):
            y[i] += 1

#chi^2 anpassung
def gauss(A, x):
    return 1/np.sqrt(2 * np.pi * A[1]**2) * np.exp(-(x - A[0])**2/(2 * A[1]**2))

#Berechne Fehler auf y
ey = []
for i in range(len(y)):
    y_fehler = 0
    for j in range(len(y)):
        if i == j:
            y_fehler += y[j] * (1/sum(y) - y[j] / (sum(y))**2)**2
        else:
            y_fehler += y[j] * (y[j] / (sum(y))**2)**2
    ey.append(np.sqrt(y_fehler))

startwerte = [27, 4]
sol = AM.fitte_bel_function(x, y/sum(y), np.full(len(x), 0.00001), ey, gauss, startwerte)
print sol

#mittelwert und std ausrechnen und aus erwartung dann chi^2 ausrechnen
mu = np.mean(data)
sig = np.std(data, ddof = 1)
chi = AM.chiq_y(x[4:19], y[4:19]/sum(y), ey[4:19], gauss, [mu, sig])

#Plot
plt.figure(1)
plt.hist(data, bins = x, normed = True)
plt.figtext(0.15,0.55,
            '$\chi ^2$ - Anpassung in rot \n'
            +'Modell: P(x) = $1/sqrt(2 \cdot \pi \cdot \sigma ^2)$ $\cdot$ $e^{(x - \mu)^2/(2 \cdot \sigma ^2)}$'
            +'\n $\mu$= ('+str(np.round(sol[0][0],6))+' +/- '+str(np.round(sol[1][0],6))+') '
            +'\n $\sigma$= ('+str(np.round(sol[0][1],6))+' +/- '+str(np.round(sol[1][1],6))+')  \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(sol[2], 3))+' \n'
            +'\n Erwartung aus Mittelwert und Fehler in gruen'
            +'\n $\mu$= '+str(np.round(mu,6))
            +'\n $\sigma$= '+str(np.round(sig,6))+'  \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
plt.xlabel('Anzahl Pulse in 3s Intervallen')
plt.ylabel('Relative Haeufigkeit')
plt.title('Gaussverteilung der Pulsraten bei Messzeit von 0.3s')
plt.plot(x, gauss([sol[0][0], sol[0][1]], x), color = 'r')
plt.plot(x, gauss([mu, sig], x), color = 'g')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))