# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:57:14 2018

@author: Gerald
"""

import Praktikum as p
import T1_Funktionen as func
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

sig_tau = 0.5 / np.sqrt(12)
offset, sig_U = func.Offset_Rauschen()
rohdata = func.Rohdaten(offset, sig_U * 500000, sig_tau, 19)

#T1 aus zero-crossing-point-Methode
U_Null = np.zeros(len(rohdata[:,0]))
zeros = AM.Schnittpunkte(rohdata[:,0], rohdata[:,1], U_Null)
T1_zero = 1/np.log(2) * (rohdata[zeros[0]][0] + rohdata[zeros[0] +1][0])/2
#sig_T1_zero = 1/np.log(2)

#T1 aus linearer Fit an halblogarithmischer Auftragung
Y = np.log(1 - rohdata[:,1])
sig_Y = rohdata[:,3]/(1 - rohdata[:,1])
a, sig_a, b, sig_b, chi, cor = p.lineare_regression_xy(rohdata[:,0], Y, rohdata[:,2], sig_Y)


plt.figure(1)
ax1=plt.subplot(211)
plt.errorbar(rohdata[:,0], rohdata[:,1], xerr = rohdata[:,2], yerr = rohdata[:,3], fmt = '.', color='b')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))