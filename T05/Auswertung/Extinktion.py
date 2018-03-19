# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:21:06 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import Kalibration_Methode as test

start_time=timeit.default_timer()

#wähle auszuwertenden Datensatz aus; i = 0 und i = 1 führen zu divisionen durch 0!!!
i = 4
index = ['Rauschmessung', 'leer', 'Eisen', 'Eisensulfat', 'Stahl']
data_rausch = np.genfromtxt("../Daten/GR2830/Extinsion " + index[0] + ".ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
data_leer = np.genfromtxt("../Daten/GR2830/Extinsion " + index[1] + ".ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
data = np.genfromtxt("../Daten/GR2830/Extinsion " + index[i] + ".ws5", delimiter = ',', skip_header = 1, skip_footer = 1)

Z_oA = sum(data_leer) - sum(data_rausch)
Z_inf = sum(data) - sum(data_rausch)

sig_Z_oA = np.sqrt(sum(data_leer) + sum(data_rausch))
sig_Z_inf = np.sqrt(sum(data) + sum(data_rausch))

D_ex = Z_inf/Z_oA
sig_D_ex = D_ex * np.sqrt((sig_Z_oA/Z_oA)**2 + (sig_Z_inf/Z_inf)**2)
print D_ex, sig_D_ex

#plotte Spektrum e
e = 4
title = ['ohne Quelle', 'ohne Absorber', 'Eisenabsorber', 'Eisensulfatabsorber', 'Stahlabsorber']
data_y = np.genfromtxt("../Daten/GR2830/Extinsion " + index[e] + ".ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
data_x = np.arange(len(data_y))
sig_x = np.full(len(data_x), 1./np.sqrt(12))
sig_y = np.sqrt(data_y)
plt.figure(1)
ax = plt.subplot(111)
plt.errorbar(data_x, data_y, xerr = sig_x, yerr = sig_y, fmt = '.', color = 'b', label = 'Messung')
if i == e:
    plt.figtext(0.15,0.7,
                'Gesamt gezaehlte Ereignisse: '+str(np.round(sum(data_y),0))
                +'\n $D_{ex}$= '+str(np.round(D_ex,5))+' +/- '+str(np.round(sig_D_ex,5)))
else:
    plt.figtext(0.38,0.75,
                'Gesamt gezaehlte Ereignisse: '+str(sum(data_y)))
plt.xlabel('Chanel')
plt.ylabel('n')
plt.legend()
plt.title('Gesamtes Spektrum bei Messung ' + title[e])

plt.figure(2)
ax = plt.subplot(111)
plt.plot(data_x, data_y, label = title[e])
plt.xlabel('Channel')
plt.ylabel('n')
plt.legend()

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))