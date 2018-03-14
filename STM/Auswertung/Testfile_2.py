# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:01:58 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import STM_Methoden as STMM

start_time=timeit.default_timer()

data_index = [132, 297, 644, 1269]
data_nach = []
data_vor = []
for i in range(len(data_index)):
    data_vor.append(STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 1)) 
    data_nach.append(STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 0))

#abgelesene Schätzwerte für die Position der Kante
vor_kante_vor = [98, 50, 73, 58]
nach_kante_vor = [111, 61, 92, 86]
vor_kante_nach = [93, 50, 74, 42]
nach_kante_nach = [104, 60, 85, 68]

kante_vor = [103, 57, 87, 62]
kante_nach = [99, 52, 80, 47]

#lineare Regressionen an Bereich vor und hinter Kante
sig_x = 0.1/np.sqrt(12)
sig_y = 0.2/np.sqrt(12)
vor_sol_vor, nach_sol_vor, vor_sol_nach, nach_sol_nach = STMM.multi_lin_reg(data_nach, data_vor, vor_kante_vor, nach_kante_vor, vor_kante_nach, nach_kante_nach, sig_x, sig_y)

def hoehe(a_vor, b_vor, a_nach, b_nach, x_k, y_k):
    a_k = -1./a_nach
    b_k = y_k - a_k * x_k
    x1 = (b_k - b_nach)/(a_nach - a_k)
    x2 = (b_k - b_vor)/(a_vor - a_k)
    y1 = a_k * x1 + b_k
    y2 = a_k * x2 + b_k
    h = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return h

nach_steigung_var = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1]
vor_steigung_var = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
nach_abschnitt_var = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]
vor_abschnitt_var = [1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1]

#Betrachte Datensatz e
e = 0
h = hoehe(vor_sol_vor[e][0], vor_sol_vor[e][0])