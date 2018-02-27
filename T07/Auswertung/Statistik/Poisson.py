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

x = np.arange(min(data),max(data))
y = np.full(len(x), 0)
for i in range(len(x)):
    for j in range(len(data)):
        if data[j] == i + min(data):
            y[i] += 1

#chi^2 anpassung
def poisson(A, x):
    return A[0]**x * np.exp(-A[0]) / x

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

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))