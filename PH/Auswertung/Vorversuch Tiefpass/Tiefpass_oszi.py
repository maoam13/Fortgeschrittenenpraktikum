# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:44:35 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

def aus(i, startwerte, startwerte1, sy = 0.01/np.sqrt(12)):
    data = np.genfromtxt("../../Daten/Vorversuch Tiefpass/Oszi/ALL00{0:1.0f}{1:1.0f}/F00{0:1.0f}{1:1.0f}CH1.csv".format((i-(i%10))/10, i%10), delimiter = ',', skip_header = 19)
    data1 = np.genfromtxt("../../Daten/Vorversuch Tiefpass/Oszi/ALL00{0:1.0f}{1:1.0f}/F00{0:1.0f}{1:1.0f}CH2.csv".format((i-(i%10))/10, i%10), delimiter = ',', skip_header = 19)
    def func(A, x):
        return A[0] * np.cos(2 * np.pi * (A[1] * x + A[2]))
    ex = np.full(len(data[:,3]), (data[0][3] - data[1][3])/np.sqrt(12))
    ey = np.full(len(data[:,4]), sy)
    sol = AM.fitte_bel_function(data[:,3], data[:,4], ex, ey, func, startwerte)
    ex1 = np.full(len(data[:,3]), (data[0][3] - data[1][3])/np.sqrt(12))
    ey1 = np.full(len(data[:,4]), sy)
    sol1 = AM.fitte_bel_function(data1[:,3], data1[:,4], ex1, ey1, func, startwerte1)
    return sol, sol1

startwerte = [[0.9, 10, 3./4], [0.9, 100, 3./4], [0.9, 200, 3./4], [0.9, 400, 1./4], [0.9, 500, 3./4], [0.9, 600, 1./8], 
              [0.9, 700, 5./8], [0.9, 800, 1./4], [0.9, 900, 1./2], [0.9, 1000, 3./4], [0.9, 1100, 0.], [0.9, 1200, 1./4], 
              [0.9, 1300, 1./2], [0.9, 1400, 3./4], [0.9, 1500, 0.], [0.9, 1600, 1./4], [0.5, 1700, 1./2], [0.5, 1800, 3./4], 
              [0.5, 1900, 0.], [0.5, 2000, 1./4], [0.5, 2100, 1./2], [0.5, 2200, 3./4], [0.5, 2300, 0.], [0.5, 2400, 1./4], 
              [0.5, 2500, 1./4], [0.5, 2600, 1./2], [0.5, 2800, 3./4], [0.5, 2900, 3./4], [0.5, 3000, 0.], [0.5, 4000, 1./4], 
              [0.2, 5000, 3./4], [0.2, 6000, 0.], [0.2, 7000, 1./2], [0.2, 8000, 0.], [0.2, 9000, 3./8], [0.2, 10000, 1./2], 
              [0.2, 3500, 1./2], [0.9, 20, 3./4], [0.9, 40, 1./4], [0.9, 60, 1./4], [0.9, 80, 1./4]]

startwerte1 = [[0.9, 10, 3./4], [0.9, 100, 3./4], [0.9, 200, 3./4], [0.9, 400, 1./4], [0.9, 500, 3./4], [0.9, 600, 1./8], 
              [0.9, 700, 5./8], [0.9, 800, 1./4], [0.9, 900, 1./2], [0.9, 1000, 3./4], [0.9, 1100, 0.], [0.9, 1200, 1./4], 
              [0.9, 1300, 1./2], [0.9, 1400, 3./4], [0.9, 1500, 0.], [0.9, 1600, 1./4], [0.9, 1700, 1./2], [0.9, 1800, 3./4], 
              [0.9, 1900, 0.], [0.9, 2000, 1./4], [0.9, 2100, 1./2], [0.9, 2200, 3./4], [0.9, 2300, 0.], [0.9, 2400, 1./4], 
              [0.9, 2500, 1./4], [0.9, 2600, 1./2], [0.9, 2800, 3./4], [0.9, 2900, 3./4], [0.9, 3000, 0.], [0.9, 4000, 1./4], 
              [0.9, 5000, 3./4], [0.9, 6000, 0.], [0.9, 7000, 1./2], [0.9, 8000, 0.], [0.9, 9000, 3./8], [0.9, 10000, 1./2], 
              [0.9, 3500, 1./2], [0.9, 20, 3./4], [0.9, 40, 1./4], [0.9, 60, 1./4], [0.9, 80, 1./4]]

f = []
sf = []
A = []
sA = []
chiq = []
A1 = []
sA1 = []
chiq1 = []
for i in range(len(startwerte)):
    test, test1 = aus(i, startwerte[i], startwerte1[i])
    f.append(test[0][1])
    sf.append(test[1][1])
    A.append(test[0][0])
    sA.append(test[1][0])
    chiq.append(test[2])
    A1.append(test1[0][0])
    sA1.append(test1[1][0])
    chiq1.append(test1[2])

Y = np.abs(np.array(A)/np.array(A1))
sY = Y * np.sqrt((np.array(sA)/np.array(A))**2 + (np.array(sA1)/np.array(A1))**2)

f, Y, sf, sY = AM.sortieren([f, Y, sf, sY], 0)

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
H = Y[2:]
H_err = sY[2:]
for i in range(len(f)-2):
    H[i] = Y[i+2] - kenn(sol[0], f[i+2])
    H_err[i] = np.sqrt(sY[i+2]**2 + (sf[i+2] * kenn_abl(sol[0], f[i+2]))**2)
plt.errorbar(f[2:], H, yerr = H_err, fmt = '.', color = 'b')
x_r = np.array([min(f), max(f)])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color = 'r')
plt.ylabel('Residuen')
plt.xlabel('Frequenz [Hz]')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))