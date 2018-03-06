# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 15:49:22 2018

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

peak_approx = [26, 48, 86, 131]
k = 6
x = data[0][:,0]
y = data[0][:,1]
test = p.peak(x, y, x[peak_approx[0] - k], x[peak_approx[0] + k])


print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))