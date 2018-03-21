# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:21:12 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import Methoden as m

start_time=timeit.default_timer()

i = 2
index = ["Ag", "Cu", "I"]
data = m.KalibrationEinlesen(i)
data_co = m.fft_cutoff(data)
data_x = np.arange(len(data))

if i == 0:
    startwerte1 = [3350, 40, 670, 30389]
    startwerte2 = [3774, 28, 615, 5486]
    peak1 = m.peak_best(np.real(data_co[0]), startwerte1)
    peak2 = m.peak_best(np.real(data_co[0]), startwerte2)
if i == 1:
    startwerte1 = [1219, 16, 600, 66372]
    startwerte2 = [1350, 16, 600, 10346]
    peak1 = m.peak_best(np.real(data_co[0]), startwerte1)
    peak2 = m.peak_best(np.real(data_co[0]), startwerte2)
if i == 2:
    startwerte1, p1 = [4329, 27, 860, 20576, 4291, 22, 12739], 2
    startwerte2, p2 = [4885, 12, 660, 4465, 5000, 50, 1375], 2
    #startwerte3 = [5000, 50, 660, 1375]
    peak1 = m.peak_best(np.real(data_co[0]), startwerte1, p = p1)
    peak2 = m.peak_best(np.real(data_co[0]), startwerte2, p = p2)

#Energien der Linien in eV
E = [[22162.9, 24942.4], [8047.8, 8905.3], [28317.2, 28612, 32294.7, 33042]]

plt.figure(1)
plt.plot(data_x, data_co[0], color = 'b')
plt.xlabel('Channel')
plt.ylabel('counts')
#plt.legend()
plt.title('Spektrum von '+ index[i])

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))