# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:20:06 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np

def get_delta_t(i, j, schwelle):
    #schwelle = 0.01
    totzeit = 0.00025
    data = np.genfromtxt("ALL00{0:1.0f}{1:1.0f}/F00{0:1.0f}{1:1.0f}CH1.csv".format(i, j), delimiter = ',')
    schwelle = 3 * np.abs(np.mean(data[:,4]))
    #print schwelle
    index = AM.get_werte_ab_schwelle(data[:,4], schwelle)
    delta_t = []
    for j in range(len(index) - 1):
        delta_t.append(data[index[j+1],3] - data[index[j],3])
    for k in range(len(delta_t)):
        if delta_t[k] < totzeit:
            np.delete(delta_t, k)
    return np.array(delta_t)