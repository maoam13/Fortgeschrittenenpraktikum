# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:59:04 2018

@author: grldm
"""

import auswertung_nur_Methoden as AM
import numpy as np

def Kalibration(i):
    #bekannte Größen: Lichtegeschwindigkeit in mm/s und E0 in neV
    c = 300000 * 10**6
    E0 = 14.4 * 10**12
    index = ['1', 'einlinien_echt', 'Extiktion', 'hyperfein', 'quadrupol']
    data = np.genfromtxt("../Daten/GR2830/v kalibration " + index[i] + ".ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
    sig_y = np.full(len(data), 2.)
    startwerte = [1000, np.pi/(766-251)]
    data_x = np.arange(len(data))
    sig_x = np.full(len(data_x), 1./np.sqrt(12))
    #abgelesene Nulldurchgänge
    zeros_1 = [255, 256, 255, 255, 255]
    zeros_2 = [767, 766, 767, 766, 767]

    #"drehe" mittlere Daten um
    data_y = []
    for j in range(len(data)):
        if j > zeros_1[i] and j < zeros_2[i]:
            data_y.append(-data[j])
        else:
            data_y.append(data[j])
    def cos(A, x):
        return A[0] * np.cos(A[1] * x)
    A, sig_A, chiq = AM.fitte_bel_function(data_x, data, sig_x, sig_y, cos, startwerte)
    c = 300000 * 10**6
    v = cos(A, data_x) * 1024/(45 * 3160.56)
    sig_v = 1024./(45 * 3160.56) * np.sqrt((sig_A[0] * np.cos(A[1] * data_x))**2 + (sig_A[1] * A[0] * A[1] * np.sin(A[1] * data_x)))    
    E = E0 * (1 + v/c)
    sig_E = sig_v * E0/c
    return E, sig_E, v, sig_v
    