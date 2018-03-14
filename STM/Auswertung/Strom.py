# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:05:35 2018

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
data_nach = []
data_vor = []
for i in range(len(data_index)):
    data_vor.append(STMM.lese_Profillinie_ein_IGain(data_index[i] * 1000, vor = 1, Strom = 1)) 
    data_nach.append(STMM.lese_Profillinie_ein_IGain(data_index[i] * 1000, vor = 0, Strom = 1))

skala = [1, 1, 1000, 1000]
mean_vor = []
std_vor = []
mean_nach = []
std_nach = []
for i in range(len(data_vor)):
    mean_vor.append(np.mean(data_vor[i][:,1]) * skala[i])
    std_vor.append(np.std(data_vor[i][:,1]) * skala[i])
    mean_nach.append(np.mean(data_nach[i][:,1]) * skala[i])
    std_nach.append(np.std(data_nach[i][:,1]) * skala[i])


print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))