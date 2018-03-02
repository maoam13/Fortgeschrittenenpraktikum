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
data = []
for i in range(len(data_index)):
    bla = STMM.lese_Profillinie_ein(data_index[i] * 1000, vor = 0)
    data.append(bla)
'''
a = STMM.addiere_abstaende(data[0])
b = STMM.addiere_abstaende(data[1])
c = STMM.addiere_abstaende(data[2])
d = STMM.addiere_abstaende(data[3])
'''

#finde extremalstellen
usedData = data[0]
extremal = []
for i in range(len(usedData[0])):
    bla = usedData[1][i]

#Plot
plt.figure(1)
#plt.plot(data[0][:,0], data[0][:,1])
plt.plot(data[1][:,0], data[1][:,1])
#plt.plot(data[2][:,0], data[2][:,1])
#plt.plot(data[3][:,0], data[3][:,1])
plt.xlabel('X [nm]')
plt.ylabel('Z [nm]')
plt.title('Hoehenprofil')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))