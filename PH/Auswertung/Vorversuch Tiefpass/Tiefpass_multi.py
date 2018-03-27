# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:43:37 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

data = np.genfromtxt("../../Daten/Vorversuch Tiefpass/Vorversuch Tiefpass.csv", delimiter = ';', skip_header = 1)

f, A, B = AM.sortieren([data[:,0], data[:,1], data[:,2]], 0)
sA = 0.001/np.sqrt(12)
sB = 0.001/np.sqrt(12)
Y = np.array(B)/np.array(A)
sf = np.full(len(f), 1./np.sqrt(12))
sY = Y * np.sqrt((sA/A)**2 + (sB/B)**2)

#fitte Funktion zur Bestimmung der Grenzfrequenz
def kenn(A, x):
    return 1./np.sqrt(1 + (x/A[0])**2)
def kenn_abl(A, x):
    return -x/(A[0]**2 * (1 + (x/A[0])**2)**(3/2))

sol = AM.fitte_bel_function(f[2:-1], Y[2:-1], sf[2:-1], sY[2:-1], kenn, [1000])

#test = AM.sortieren([f, Y, sf, sY], 0)

#Plotte Tiefpass Kennlinie
plt.close('all')
plt.figure(1)
ax1 = plt.subplot(211)
plt.errorbar(f, Y, xerr = sf, yerr = sY, fmt = '.', color = 'b')
plt.plot(f, kenn(sol[0], f), color = 'r')
plt.figtext(0.15,0.7,
            'Model: y = $\dfrac{1}{\sqrt{1 + (f/f_G)^2}}$ \n'
            +'$f_G$= ('+ str(np.round(sol[0][0],5)) + ' $\pm$ '+ str(np.round(sol[1][0],5)) + ') Hz \n'
            +'$\chi ^2$/ndof= ' + str(np.round(sol[2], 2)))
plt.title('Kennlinie Tiefpass')
plt.ylabel('$\dfrac{U_a}{U_e}$')
ax2=plt.subplot(212,sharex=ax1)
H = Y
H_err = sY
for i in range(len(f)):
    H[i] = Y[i] - kenn(sol[0], f[i])
    H_err[i] = np.sqrt(sY[i]**2 + (sf[i] * kenn_abl(sol[0], f[i]))**2)
plt.errorbar(f, H, yerr = H_err, fmt = '.', color = 'b')
x_r = np.array([min(f), max(f)])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color = 'r')
plt.ylabel('Residuen')
plt.xlabel('Frequenz [Hz]')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))