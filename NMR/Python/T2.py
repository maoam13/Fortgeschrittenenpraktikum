# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:53:57 2018

@author: Moritz
"""

import Praktikum as p
import numpy as np
import matplotlib.pyplot as plt
import csv

file = open("F0000CH2.CSV")
csv_reader = csv.reader(file, delimiter=",")
x = []
y = []
for row in csv_reader:
    wert = row[4]
    wert = float(wert)
    y.append(wert)
    
    wert = row[3]
    wert = float(wert)
    x.append(wert)
file.close()


dt = float(0.004)
t = float(-0.002)

ypeak = []
xpeak = np.zeros(11)

for i in range(11):
    array = y[x.index(round(t,5)):x.index(round(t+dt,5))]
    ypeak.append(float(max(array)))
    xwert = np.argmax(array)+x.index(round(t,5))
    print max(array),x[xwert],x.index(round(t,5)),x.index(round(t+dt,3))
    xpeak[i] = float(x[xwert])
    
    t = t+2*dt

offset = np.mean(y[x.index(0.086):])

test = np.zeros(11)
ystd = float(np.std(y[x.index(0.086):]))
for i in range(len(test)):
    test[i] = ystd
        
ypeak = ypeak - offset
y = y -offset

abra = test**2

plt.plot(xpeak,np.log(ypeak))

a, sig_a, b, sig_b, chi, cor = p.lineare_regression_xy(xpeak, ypeak,[0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002], test)
print -1/a