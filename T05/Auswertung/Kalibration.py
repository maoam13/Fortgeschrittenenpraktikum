# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:21:05 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

v0 = 1

data_v0 = np.genfromtxt("../Daten/GR2830/Quellspektrum v0_echt.ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
data_vinf = np.genfromtxt("../Daten/GR2830/Quellspektrum vinf.ws5", delimiter = ',', skip_header = 1, skip_footer = 1)
data_x = np.arange(len(data_v0))

sig_ch = np.full(len(data_x), 1./np.sqrt(12))
sig_v0 = np.sqrt(data_v0)
sig_vinf = np.sqrt(data_vinf)

def gauss_fit(x, y, sx, sy, startwerte):
    def gauss(A, x):
        #A = [sig, mu, maxhöhe]
        return A[2] * 1./np.sqrt(2 * np.pi * A[0]**2) * np.exp(-(x - A[1])**2 / (2 * A[0]**2))
    A, sig_A, chiq = AM.fitte_bel_function(x, y, sx, sy, gauss, startwerte)
    return A, sig_A, chiq

A, sig_A, chiq = gauss_fit(data_x[481:600], data_v0[481:600], sig_ch[481:600], sig_v0[481:620], [548, 20, 2500])

#Finde Max bei scharfen peaks
if v0:
    peak1 = AM.getmax(data_x[75:101], data_v0[75:101])
    peak2 = [data_x[241], data_v0[241], 241]
    sig_peak2 = (266 - 216)/np.sqrt(12)
    peak3 = [data_x[546], data_v0[546], 546]
    sig_peak3 = (563 - 529)/np.sqrt(12)
    peak4 = [data_x[768], data_v0[768], 768]
    sig_peak4 = (796 - 740)/np.sqrt(12)
    peak5 = AM.getmax(data_x[980:1020], data_v0[980:1020])
else:
    peak1 = AM.getmax(data_x[75:101], data_v0[75:101])
    peak2 = [data_x[241], data_v0[241], 241]
    sig_peak2 = (266 - 216)/np.sqrt(12)
    peak3 = [data_x[546], data_v0[546], 546]
    sig_peak3 = (563 - 529)/np.sqrt(12)
    peak4 = [data_x[768], data_v0[768], 768]
    sig_peak4 = (796 - 740)/np.sqrt(12)
    peak5 = AM.getmax(data_x[980:1020], data_v0[980:1020])

#Kalibration
#x = [peak1[0], peak2[0], peak3[0], peak4[0], peak5[0]]
#sig_x = [1./np.sqrt(12), sig_peak2, sig_peak3, sig_peak4, 1./np.sqrt(12)]
x = np.array([peak1[0], peak3[0], peak5[0]])
sig_x = np.array([14./np.sqrt(12), sig_peak3, 16./np.sqrt(12)])
#sig_x = np.full(len(x), 1.)
E = np.array([6.4, 14.4, 14.4 + 6.4])
#E = np.array([7.1, 14.4, 14.4 + 7.1])
sig_E = np.array([0.1/np.sqrt(12), 0.1/np.sqrt(12), 0.1/np.sqrt(6)])
sol = p.lineare_regression_xy(x, E, sig_x, sig_E)

#plotte lin reg
plt.figure(1)
ax1 = plt.subplot(211)
plt.errorbar(x, E, xerr = sig_x, yerr = sig_E, fmt = '.', color = 'b')
plt.plot(x, sol[0] * x + sol[2], color = 'r')
plt.title('Grobe Kalibrierung mit bekannten Peaks aus Spektrum')
plt.ylabel('Energie [keV]')
plt.figtext(0.15,0.7,
            'Model: y = a $\cdot$ x + b \n'
            +'a= ('+ str(np.round(sol[0],5)) + ' $\pm$ '+ str(np.round(sol[1],5)) + ') keV/ch \n'
            +'b= ('+ str(np.round(sol[2],2)) + ' $\pm$ '+ str(np.round(sol[3],2)) + ') keV \n'
            +'$\chi ^2$/ndof= ' + str(np.round(sol[4], 2)))
ax2=plt.subplot(212,sharex=ax1)
H = np.full(len(x), 0.5)
H_err = np.full(len(x), 0.5)
for i in range(len(x)):
    H[i] = E[i] - sol[0] * x[i] - sol[2]
    H_err[i] = np.sqrt(sig_E[i]**2 + (sol[0] * sig_x[i])**2)
plt.errorbar(x, H, yerr = H_err, fmt = '.', color = 'b')
x_r = np.array([0, x[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color = 'r')
plt.ylabel('Residuen [keV]')
plt.xlabel('chanel')

#plotte Spektrum
plt.figure(2)
#plt.plot(data_x, data_v0, color = 'b', label = 'v = 0')
#plt.plot(data_x, data_vinf, color = 'g', label = 'v = $\infty$')
if v0:
    plt.errorbar(data_x, data_v0, color = 'b', xerr = sig_ch, yerr = sig_v0, fmt = '.', label = 'Daten')
else:
    plt.errorbar(data_x, data_vinf, color = 'b', xerr = sig_ch, yerr = sig_vinf, fmt = '.', label = 'Daten')
plt.axvline(peak1[0], color = 'r', label = 'peak 1')
#plt.axvline(peak2[0], color = 'y', label = 'peak 2')
plt.axvline(peak3[0], color = 'g', label = 'peak 2')
#plt.axvline(peak4[0], color = 'orange', label = 'peak 4')
plt.axvline(peak5[0], color = 'y', label = 'peak 3')
plt.xlabel('Chanel')
plt.ylabel('counts')
plt.legend()
plt.figtext(0.3,0.65,
            'Abgelesene Peakpositionen in der Form (x, y): \n'
            +'Peak 1: ('+str(peak1[0])+' +/- '+str(np.round(14./np.sqrt(12),1))+', '+str(peak1[1])+' +/- '+str(np.round(np.sqrt(peak1[1]),1)) + ')'
#            +'\n Peak 2: ('+str(peak2[0])+' +/- '+str(np.round(sig_peak2,1))+', '+str(peak2[1])+' +/- '+str(np.round(np.sqrt(peak2[1]),1)) + ')'
            +'\n Peak 2: ('+str(peak3[0])+' +/- '+str(np.round(sig_peak3,1))+', '+str(peak3[1])+' +/- '+str(np.round(np.sqrt(peak3[1]),1)) + ')'
#            +'\n Peak 4: ('+str(peak4[0])+' +/- '+str(np.round(sig_peak4,1))+', '+str(peak4[1])+' +/- '+str(np.round(np.sqrt(peak4[1]),1)) + ')'
            +'\n Peak 3: ('+str(peak5[0])+' +/- '+str(np.round(16./np.sqrt(12),1))+', '+str(peak5[1])+' +/- '+str(np.round(np.sqrt(peak5[1]),1)) + ')')
if v0:
    plt.title('Quellspektrum bei v = 0')
else:
    plt.title('Quellspektrum bei v = $\infty$')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))