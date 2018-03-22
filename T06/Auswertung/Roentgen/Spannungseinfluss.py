# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:00:56 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import Methoden as m

start_time=timeit.default_timer()

i = 0
index = ["20", "35", "50"]
data1 = np.genfromtxt("../Daten/Roentgen/StainlessSteel_"+index[0]+"kV_5min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
data2 = np.genfromtxt("../Daten/Roentgen/StainlessSteel_"+index[1]+"kV_5min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
data3 = np.genfromtxt("../Daten/Roentgen/StainlessSteel_"+index[2]+"kV_5min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
data_x = np.arange(len(data1))

plt.close('all')
plt.figure(1)
plt.ylabel('Counts')
plt.xlabel('Channel')
plt.title('Vergleich der Spektren von Stainless Steel bei variierter Spannung')
plt.plot(data_x, data1, color = 'b', label = 'U = 20 kV')
plt.plot(data_x, data2, color = 'g', label = 'U = 35 kV')
plt.plot(data_x, data3, color = 'orange', label = 'U = 50 kV')
plt.legend()
plt.xlim(400, 3200)