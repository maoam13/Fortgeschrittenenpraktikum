# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:28:13 2018

@author: grldm
"""

import Praktikum as p
import Peakabstaende_Funktionen as func
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

data = np.genfromtxt("GMpoisson.csv", delimiter = ',')

#x = np.arange(min(data),max(data))
x = np.arange(int(min(data)),int(max(data)))
y = np.full(len(x), 0)
for i in range(len(x)):
    for j in range(len(data)):
        if data[j] == i + min(data):
            y[i] += 1

#chi^2 anpassung
def fakultaet(n):
    ret = []
    for j in range(len(n)):
        fak = 1
        for i in range(1, n[j]):
            fak = fak * (i + 1)
        ret.append(fak)
    return ret

def poisson(A, x):
    return A[0]**x * np.exp(-A[0]) / (x+1)

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

startwerte = [1]
sol = AM.fitte_bel_function(x, y/sum(y), np.full(len(x), 0.1), ey, poisson, startwerte)
print sol

#mittelwert und std ausrechnen und aus erwartung dann chi^2 ausrechnen
mu = np.mean(data)
#sig = np.std(data, ddof = 1)
chi = AM.chiq_y(x[0:3], y[0:3], np.sqrt(y[0:3]), poisson, [mu])

#Plot
plt.figure(1)
plt.hist(data, bins = x, normed = True)
plt.figtext(0.7,0.6,
            '$\chi ^2$ - Anpassung in rot \n'
            +'Modell: P(n) = $\mu ^n / n!$ $\cdot$ $e^{-\mu}$'
            +'\n $\mu$= ('+str(np.round(sol[0][0],6))+' +/- '+str(np.round(sol[1][0],6))+') '
            +'\n $\chi ^2 / ndof$= ' + str(np.round(sol[2], 3))+' \n'
            +'\n Erwartung aus Mittelwert und Fehler in gruen'
            +'\n $\mu$= '+str(np.round(mu,6))
            +'\n $\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
plt.xlabel('Anzahl Pulse in 0.3s Intervallen')
plt.ylabel('Relative Haeufigkeit')
plt.title('Poissonverteilung der Pulsraten bei Messzeit von 0.3s')
plt.plot(x, poisson([sol[0][0]], x), color = 'r')
plt.plot(x, poisson([mu], x), color = 'g')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))