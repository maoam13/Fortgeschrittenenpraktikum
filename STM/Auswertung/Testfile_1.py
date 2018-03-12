# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:12:22 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import STM_Methoden as STMM

start_time=timeit.default_timer()

#Betrachte Datensatz i
i = 0
################

vor_kante_vor = [98, 50, 73, 58]
nach_kante_vor = [111, 61, 92, 67]
vor_kante_nach = [93, 50, 74, 42]
nach_kante_nach = [104, 60, 85, 68]

data_index = [132, 297, 644, 1269]
data_nach = STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 1)
data_vor = STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 0)
#for i in range(len(data_index)):
#    data_vor.append(STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 1)) 
#    data_nach.append(STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 0))

sig_x = 0.4/np.sqrt(12)
sig_y = 0.4/np.sqrt(12)
std_x_vor = np.full(vor_kante_vor[i], sig_x)
std_y_vor = np.full(vor_kante_vor[i], sig_y)
data_vorkante = data_vor[0:vor_kante_vor[i]]
linreg_vorkante = p.lineare_regression_xy(data_vorkante[:,0], data_vorkante[:,1], std_x_vor, std_y_vor)

data_nachkante = data_vor[nach_kante_vor[i]:-1]
std_x_nach = np.full(len(data_nachkante), sig_x)
std_y_nach = np.full(len(data_nachkante), sig_y)
linreg_nachkante = p.lineare_regression_xy(data_nachkante[:,0], data_nachkante[:,1], std_x_nach, std_y_nach)


print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))