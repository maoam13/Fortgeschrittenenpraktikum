# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:53:57 2018

@author: Moritz
"""

import Praktikum as p
import numpy as np
import matplotlib.pyplot as plt
import csv

file = open("C:\Users\morit\Documents\GitHub\Fortgeschrittenenpraktikum\NMR\Daten\T2CP\ALL0002\F0002CH2.CSV")
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


dt = float(0.0060)
t = float(-0.00252)
N = 8

ypeak = []
xpeak = np.zeros(N)

for i in range(N):
    array = y[x.index(round(t,5)):x.index(round(t+dt,5))]
    ypeak.append(float(max(array)))
    xwert = np.argmax(array)+x.index(round(t,5))
    print max(array),x[xwert],x.index(round(t,5)),x.index(round(t+dt,3))
    xpeak[i] = float(x[xwert])
    
    t = t+2*dt

offset = np.mean(y[x.index(0.086):])

yfehler = np.zeros(N)
ystd = float(np.std(y[x.index(0.086):]))
for i in range(len(yfehler)):
    yfehler[i] = ystd
        
ypeak = ypeak - offset
y = y - offset

plt.scatter(xpeak,np.log(ypeak))
xstd = [0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002,0.0002]

a, sig_a, b, sig_b, chi, cor = p.lineare_regression_xy(xpeak, np.log(ypeak),xstd, yfehler)
ywerte = a*xpeak+b
plt.plot(xpeak,ywerte)
print chi/11
print -1./a