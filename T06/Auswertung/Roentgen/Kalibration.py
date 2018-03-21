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

i = 0
index = ["Ag", "Cu", "I"]
data = m.KalibrationEinlesen(i)
data_co = m.fft_cutoff(data)
data_x = np.arange(len(data))


plt.figure(1)
plt.plot(data_x, data_co[0], color = 'b')
plt.xlabel('Channel')
plt.ylabel('counts')
#plt.legend()
plt.title('Spektrum von '+ index[i])

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))