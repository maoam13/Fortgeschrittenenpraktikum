# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 17:54:54 2018

@author: Gerald
"""

import Praktikum as p
import T1_Funktionen as func
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

sig_tau = 8. * 45/2500 / np.sqrt(12)
stat_U = 0.004 / np.sqrt(12)
offset, sig_U = func.Offset_Rauschen()
rohdata = func.Rohdaten(offset, np.sqrt(sig_U**2 + stat_U**2), sig_tau, 18)

Y = np.log((1 - rohdata[:,1])/2)
sig_Y = 2 * rohdata[:,3]/(1 - rohdata[:,1])

def lin(B, x):
    return B[0] * x
startwerte = [1/20.8786826317]
sol = func.fitte_bel_function(rohdata[:,0], Y, rohdata[:,2], sig_Y, lin, startwerte)


T_1_lin = -1/sol[0][0]
sig_T_1_lin = T_1_lin * -sol[1][0]/sol[0][0]
print "T1 aus linearem Fit aus halblogarithmischer Auftragung"
print T_1_lin, sig_T_1_lin


plt.figure(1)
ax1=plt.subplot(211)
ax1.set_ylabel("logarithmische Signalspannung [$ln((1-U/U_0)/2)$]")
plt.figtext(0.7,0.7,
            '\n a= ('+str(np.round(sol[0][0],6))+' +/- '+str(np.round(sol[1][0],6))+') $1/ms$ \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(sol[2], 3)))
x = np.array([0, 35])
y = sol[0][0] * x
plt.plot(x, y, color='r')
plt.errorbar(rohdata[:,0], Y, xerr = rohdata[:,2], yerr = sig_Y, fmt = '.', color='b')

ax2=plt.subplot(212,sharex=ax1)
x_r = np.array([0, 35])
y_r = np.array([0, 0])
H = np.full(len(Y), 0.5)
H_err = np.full(len(Y), 0.5)
for i in range(len(Y)):
    H[i] = Y[i] - sol[0][0] * rohdata[i][0]
    H_err[i] = np.sqrt(np.array(sig_Y[i])**2 + (sol[0][0] * np.array(rohdata[i][2]))**2)
ax2.set_xlabel("tau [ms]")
ax2.set_ylabel("Residuen [$ln((1-U/U_0)/2)$]")
plt.plot(x_r, y_r, color='r')
plt.errorbar(rohdata[:,0], H, yerr=H_err, fmt='.', color='b')
plt.show()


print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))