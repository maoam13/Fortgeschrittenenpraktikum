# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:39:08 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

data = np.genfromtxt("../../Daten/Vorversuch 2/lockin Tiefpass.csv", delimiter = ';', skip_header = 1)

f, A, B = AM.sortieren([data[:,0], data[:,1], data[:,2]], 0)
sA = np.full(len(A), 0.01/np.sqrt(12))
sB = np.full(len(B), 0.001/np.sqrt(12))
sf = np.full(len(f), 1./np.sqrt(12))
Y = np.array(A)/max(A)
sY = np.sqrt(2) * sA*2000
logf = np.log(f)

#fitte Funktion zur Bestimmung der Grenzfrequenz
def kenn(A, x):#A = [f_G, Amplitude, Nullphase]
    return A[1] * 1./np.sqrt(1 + ((x)*A[0])**2)* np.sin(-np.arctan((x-A[3])*A[2]))

def kenn2O(A, x):#A = [C, L, R, Amplitude]
    return A[3] * (1./(2*np.pi*x*A[0])**2 - A[1]/A[0])/((1./(2*np.pi*x*A[0]) - 2*np.pi*x*A[1])**2 + A[2]**2)* np.sin(-np.arctan((x-A[5])*A[4]))
def kennRLC(A, x):#A = [C, L, R, Amplitude]
    w = 2*np.pi*x
    C = A[0]
    L = A[1]
    R = A[2]
    return A[3]/(np.sqrt(w**4*L**2*C**2+w**2*R**2*C**2-2*w**2*L*C+1))* np.sin(-np.arctan((x-A[5])*A[4]))

#sol = AM.fitte_bel_function(np.log10(f[:19]), np.log10(Y[:19]), sf[:19]/(f[:19] * np.log(10)), sY[:19]/(Y[:19] * np.log(10)), kenn, [3.])
#sol = AM.fitte_bel_function(f, Y, sf, sA, kenn, [1000., 2., 2.])
sol = AM.fitte_bel_function(f, A, sf, sA, kenn, [0.005, 2., 0.02,1000])
#sol = AM.fitte_bel_function(f, A, sf, sA, kenn2, [0.001, 2., 1,1000])
#sol2O = AM.fitte_bel_function(f[:19], A[:19], sf[:19], sA[:19], kenn2O, [10**(-7), 10**(-9), 1500, 2.])
sol2O = AM.fitte_bel_function(f, A, sf, sA, kenn2O, [10**(-7), 10**(-4), 100000, 1.,0.01,1000])
f_G = 1. / (2 * np.pi * sol2O[0][0] * sol2O[0][2])
sol2O[0][0] = sol2O[0][0]*1
sol2O[0][1] = sol2O[0][1]*1
sol2O[0][2] = sol2O[0][2]*1
sol2O[0][3] = sol2O[0][3]*1
print sol2O[0]
print sol[0]
xwerte = np.arange(f[0],f[-1])

#Plotte Tiefpass Kennlinie
plt.close('all')
plt.figure(1)
ax1 = plt.subplot(111)
ax1.set_xscale("log", nonposx = 'clip')
#ax1.set_yscale("log", nonposy = 'clip')
plt.plot(xwerte,( kenn(sol[0], xwerte)), color = 'g')
plt.plot(xwerte, kenn2O(sol2O[0], xwerte), color = 'r')
plt.errorbar(f, A, xerr = sf, yerr = sA, fmt = '.', color = 'b', label = 'Messung mit Multimeter')
#plt.errorbar(f, B, xerr = sf, yerr = sB, fmt = '.', color = 'y', label = 'Messung mit Oszilloskop')
plt.title('Kennlinie Lockin Tiefpass')
plt.ylabel('$U_a$ [V]')
plt.legend()

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))