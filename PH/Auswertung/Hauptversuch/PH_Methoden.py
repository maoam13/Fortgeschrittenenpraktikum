# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 11:44:24 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt

def offset(T, U_ein, o1 = 0., o2 = 1.8, n = 10000):
    chiq = []
    for i in range(n):
        off = o1 + (o2 - o1) * i/n
        U = - U_ein - off
        sT = np.full(len(T), 0.001/np.sqrt(12))
        sU = np.full(len(U), 0.001/np.sqrt(12))
        ##########Konstanten###############
        s = 10**(-3)
        C = 6768
        V = 22.9 * 10**(-9)
        n_M = 0.27
        v = 10./s
        ####################################
        
        chi = U / (C * v * V * (1-n_M))
        schi = sU / (C * v * V * (1-n_M))
        
        #############Curie-Weiss-Gesetz Anpassung######################################
        T_1_CW, T_2_CW = 180, 190
        T_CW, chi_CW, sT_CW, schi_CW = AM.untermenge_daten(T, 1./chi, sT, schi/chi**2, T_1_CW, T_2_CW)
        sol_CW = p.lineare_regression_xy(T_CW, chi_CW, sT_CW, schi_CW)
        ################################################################################
        chiq.append(sol_CW[4])
    ret = AM.minausarray(chiq)
    return o1 + (o2 - o1) * ret[1]/n
