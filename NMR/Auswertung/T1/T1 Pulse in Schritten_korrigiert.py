# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:57:14 2018

@author: Gerald
"""

import Praktikum as p
import T1_Funktionen_korrigiert as func
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

sig_tau = 8. * 45/2500 / np.sqrt(12)
stat_U = 0.004 / np.sqrt(12)
offset, sig_U = func.Offset_Rauschen()
rohdata = func.Rohdaten(offset, np.sqrt(sig_U**2 + stat_U**2), sig_tau, 18)

#T1 aus zero-crossing-point-Methode
U_Null = np.zeros(len(rohdata[:,0]))
zeros = AM.Schnittpunkte(rohdata[:,0], rohdata[:,1], U_Null)
T1_zero = 1/np.log(2) * (rohdata[21][0] + rohdata[15][0])/2
sig_T1_zero = 1/np.log(2) * (rohdata[21][0] - rohdata[15][0])/np.sqrt(12)
print "T1 aus zero crossing point Methode"
print T1_zero, sig_T1_zero

#T1 aus linearer Fit an halblogarithmischer Auftragung
Y = np.log(1 - rohdata[:,1])
sig_Y = rohdata[:,3]/(1 - rohdata[:,1])
a, sig_a, b, sig_b, chi, cor = p.lineare_regression_xy(rohdata[:,0], Y, rohdata[:,2], sig_Y)
T_1_lin = -1/a
sig_T_1_lin = T_1_lin * (-sig_a)/a
print "T1 aus linearem Fit aus halblogarithmischer Auftragung"
print T_1_lin, sig_T_1_lin

#Plotte linearen Fit
plt.figure(1)
ax1=plt.subplot(211)
ax1.set_ylabel("logarithmische Signalspannung [$ln(1-U/U_0)$]")
plt.figtext(0.7,0.7,
            '\n a= ('+str(np.round(a,6))+' +/- '+str(np.round(sig_a,6))+') $1/ms$ \n'
            +' b= ('+str(np.round(b,6))+' +/- '+str(np.round(sig_b,6))+') \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(chi/(len(rohdata[:,0]) - 2), 3)))
x = np.array([0, 35])
y = a * x + b
plt.plot(x, y, color='r')
plt.errorbar(rohdata[:,0], Y, xerr = rohdata[:,2], yerr = sig_Y, fmt = '.', color='b')

ax2=plt.subplot(212,sharex=ax1)
x_r = np.array([0, 35])
y_r = np.array([0, 0])
H = np.full(len(Y), 1)
H_err = np.full(len(Y), 1)
for i in range(len(Y)):
    H[i] = Y[i] - a * rohdata[i][0] - b
    H_err[i] = np.sqrt(np.array(sig_Y[i])**2 + (a * np.array(rohdata[i][2]))**2)
ax2.set_xlabel("tau [ms]")
ax2.set_ylabel("Residuen [$ln(1-U/U_0)$]")
plt.plot(x_r, y_r, color='r')
plt.errorbar(rohdata[:,0], H, yerr=H_err, fmt='.', color='b')
plt.show()
#plt.savefig('linFit.png')

#Fitte Exponentialfunktion an Originaldaten
def exp(B, x):
    return 1 - 2 * np.exp(- B[0] * x)
startwerte = [a]
sol = func.fitte_bel_function(rohdata[:,0], rohdata[:,1], rohdata[:,2], rohdata[:,3], exp, startwerte)
T_1_exp = 1/sol[0][0]
sig_T_1_exp = T_1_lin * sol[1][0]/sol[0][0]
print "T1 aus Fit von Exponentialfunktion"
print T_1_exp, sig_T_1_exp

#Plotte Rohdaten
plt.figure(2)
ax1=plt.subplot(111)
plt.errorbar(rohdata[:,0], rohdata[:,1], xerr = rohdata[:,2], yerr = rohdata[:,3], fmt = '.', color='b')
#Nulllinie zur Verdeutlichung von zero crossing point Methode
x_n = [0, 40]
y_n = [0.0, 0.0]
plt.plot(x_n, y_n, color='r')
#Plotte gefittete Exponentialfnktion in Daten
plt.figtext(0.2,0.7,
            '\n Model: $U_{rel} = 1-2e^{-c \cdot t}$ \n'
            +' c= ('+str(np.round(sol[0][0],6))+' +/- '+str(np.round(sol[1][0],6))+') \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(sol[2], 3)))
x_exp_vor = np.arange(0, 320)
x_exp = x_exp_vor * 0.1
y_exp = exp([sol[0][0]], x_exp)
plt.plot(x_exp, y_exp, color='g')
plt.show()

#print rohdata[:,0]

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))