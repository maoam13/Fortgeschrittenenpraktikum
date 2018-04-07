# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 13:02:22 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import PH_Methoden as PH
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

speichern = 0
dt = 0.2

data = np.genfromtxt("../../Daten/Haupversuch/ProbeX1.dat", delimiter = '\t', dtype = np.float)
T = data[:,0][100:]
sT = np.full(len(T), 0.01/np.sqrt(12))
t = np.arange(0.0, len(T) * dt, dt)

TG = []
for i in range(len(T) - 1):
    TG.append((T[i+1] - T[i])/dt)

TG1 = []
sTG1 = []
t1 = []
st1 = []
chiq = []
for i in range(len(T) /10):
    sol = p.lineare_regression(t[i*10:(i+1)*10], T[i*10:(i+1)*10], sT[i*10:(i+1)*10])
    TG1.append(sol[0])
    sTG1.append(sol[1])
    t1.append(np.mean(t[i*10:(i+1)*10]))
    st1.append(np.std(t[i*10:(i+1)*10]))
    chiq.append(sol[4])

#Plotte Temperaturverlauf
plt.close('all')
plt.figure(1)
plt.errorbar(t, T, fmt = '.', color = 'b', label = 'Messpunkte')
plt.title('Verlauf der Temperatur ueber gesamte Messung')
plt.xlabel('Zeit [s]')
plt.ylabel('T [K]')
plt.legend()
if speichern == 1:
    plt.savefig("../../Protokoll/Bilder/Haupt_Probe/Temperatur_Verlauf")

#Plotte Temperaturgradienten
plt.figure(2)
plt.errorbar(t[1:], TG, fmt = '.', color = 'b', label = 'Messpunkte')
plt.title('Verlauf des Temperaturgradienten ueber gesamte Messung')
plt.xlabel('Zeit [s]')
plt.ylabel('Temperaturgradient [K/s]')
plt.legend()

#Plotte Temperaturgradienten 2. Version
plt.figure(3)
plt.errorbar(t1, TG1, xerr = st1, yerr = sTG1, fmt = '.', color = 'b', label = 'Messpunkte')
plt.title('Verlauf des Temperaturgradienten ueber gesamte Messung')
plt.xlabel('Zeit [s]')
plt.ylabel('Temperaturgradient [K/s]')
plt.legend()
if speichern == 1:
    plt.savefig("../../Protokoll/Bilder/Haupt_Probe/Temperaturgradient_Verlauf")

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))