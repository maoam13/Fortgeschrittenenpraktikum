# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:10:56 2018

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
data1 = np.genfromtxt("../Daten/Roentgen/Pb_5min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
data2 = np.genfromtxt("../Daten/Roentgen/Pb_ohnePUR_5min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
data_x = np.arange(len(data1))

plt.close('all')
plt.figure(1)
plt.ylabel('Counts')
plt.xlabel('Channel')
plt.title('Vergleich der Spektren von Blei mit und ohne PUR')
plt.plot(data_x, data1, color = 'b', label = 'mit PUR')
plt.plot(data_x, data2, color = 'g', label = 'ohne PUR')
plt.legend()
plt.xlim(1000, 5000)