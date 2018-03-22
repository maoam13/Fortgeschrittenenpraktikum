# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:21:12 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import Methoden as m

start_time=timeit.default_timer()

i = 3
index = ["Ag", "Cu", "I", "StainlessSteel"]
data = m.KalibrationEinlesen(i)
data_co = m.fft_cutoff(data)
data_x = np.arange(len(data))


if 1:#i == 0:
    startwerte1 = [3350, 40, 670, 30389]
    startwerte2 = [3774, 28, 615, 5486]
    peak1_Ag = m.peak_best(np.real(m.KalibrationEinlesen(0)), startwerte1, b1 = 40)
    peak2_Ag = m.peak_best(np.real(m.KalibrationEinlesen(0)), startwerte2, b1 = 40)
if 1:#i == 1:
    startwerte1 = [1219, 16, 600, 66372]
    startwerte2 = [1350, 16, 600, 10346]
    peak1_Cu = m.peak_best(np.real(m.KalibrationEinlesen(1)), startwerte1)
    peak2_Cu = m.peak_best(np.real(m.KalibrationEinlesen(1)), startwerte2)
if 1:#i == 2:
    startwerte1, p1 = [4329, 27, 860, 20576, 4291, 22, 12739], 2
    startwerte2, p2 = [4885, 12, 660, 4465, 5000, 50, 1375], 2
#    startwerte1, p1 = [4310, 15, 200, 40000, 4300, 10, 24962], 2
#    startwerte2, p2 = [4885, 12, 660, 4465, 5000, 50, 1375], 2
    #startwerte3 = [5000, 50, 660, 1375]
    peak1_I = m.peak_best(np.real(m.KalibrationEinlesen(2)), startwerte1, p = p1)
    peak2_I = m.peak_best(np.real(m.KalibrationEinlesen(2)), startwerte2, p = p2)
if 1:#i == 3:
    startwerte1 = [2644, 20, 600, 12214]
    startwerte2 = [2968, 22, 600, 2444]
    peak1_SS = m.peak_best(np.real(m.KalibrationEinlesen(3)), startwerte1)
    peak2_SS = m.peak_best(np.real(m.KalibrationEinlesen(3)), startwerte2)

#Energien der Linien in eV
E = [22162.9, 24942.4, 8047.8, 8905.3, 28317.2, 28612, 32294.7, 33042] 
E[0] = (100 * 22162.9 + 53 * 21990.3)/153

def lin(A, x):
    return A[0] + A[1] * x

x = np.array([peak1_Ag[0], peak2_Ag[0], peak1_Cu[0], peak2_Cu[0], peak1_I[0], peak2_I[0], peak1_SS[0], peak2_SS[0]])
ex = np.array([peak1_Ag[1], peak2_Ag[1], peak1_Cu[1], peak2_Cu[1], peak1_I[1], peak2_I[1], peak1_SS[1], peak2_SS[1]])
#y = np.array([22162.9, 24942.4, 8047.8, 8905.3, 28612, 32294.7, 17426, 19600])
y = np.array([22162.9, 24942.4, 8047.8, 8905.3, 28612, 32294.7, 17479.3, 19608.3])
y[0] = (100 * 22162.9 + 53 * 21990.3)/153
y[6] = (100 * 17479.3 + 52 * 17374.3)/152
y[7] = (15 * 19608.3 + 3 * 19965.2 +  8 * 19590.3)/26
startwerte = [130, 6.5]
sol = m.fitte_bel_functionx(x, y, ex, lin, startwerte)

x_pl = np.arange(0, len(data), 1)
plt.close('all')
plt.figure(1)
plt.plot(data_x, m.KalibrationEinlesen(i), color = 'b', label = 'gemessenes Spektrum')
if i == 0:
    x_plt1 = x_pl[int(peak1_Ag[4][0][0]) - 150:int(peak1_Ag[4][0][0]) + 150]
    x_plt2 = x_pl[int(peak2_Ag[4][0][0]) - 150:int(peak2_Ag[4][0][0]) + 150]
    plt.plot(x_plt1, m.gauss(peak1_Ag[4][0][0:4], x_plt1), color = 'g', label = 'Peakanpassung 1')
    plt.plot(x_plt2, m.gauss(peak2_Ag[4][0][0:4], x_plt2), color = 'orange', label = 'Peakanpassung 2')
if i == 1:
    x_plt1 = x_pl[int(peak1_Cu[4][0][0]) - 150:int(peak1_Cu[4][0][0]) + 150]
    x_plt2 = x_pl[int(peak2_Cu[4][0][0]) - 150:int(peak2_Cu[4][0][0]) + 150]
    plt.plot(x_plt1, m.gauss(peak1_Cu[4][0][0:4], x_plt1), color = 'g', label = 'Peakanpassung 1')
    plt.plot(x_plt2, m.gauss(peak2_Cu[4][0][0:4], x_plt2), color = 'orange', label = 'Peakanpassung 2')
if i == 2:
    x_plt1 = x_pl[int(peak1_I[6][0][0]) - 150:int(peak1_I[6][0][0]) + 150]
    x_plt2 = x_pl[int(peak2_I[6][0][0]) - 150:int(peak2_I[6][0][0]) + 150]
    plt.plot(x_plt1, m.gauss(peak1_I[6][0][0:4], x_plt1), color = 'g', label = 'Peakanpassung 1')
    plt.plot(x_plt2, m.gauss(peak2_I[6][0][0:4], x_plt2), color = 'orange', label = 'Peakanpassung 2')
if i == 3:
    x_plt1 = x_pl[int(peak1_SS[4][0][0]) - 150:int(peak1_SS[4][0][0]) + 150]
    x_plt2 = x_pl[int(peak2_SS[4][0][0]) - 150:int(peak2_SS[4][0][0]) + 150]
    plt.plot(x_plt1, m.gauss(peak1_SS[4][0][0:4], x_plt1), color = 'g', label = 'Peakanpassung 1')
    plt.plot(x_plt2, m.gauss(peak2_SS[4][0][0:4], x_plt2), color = 'orange', label = 'Peakanpassung 2')
plt.xlabel('Channel')
plt.ylabel('counts')
plt.xlim(2300, 3200)
plt.legend()
plt.title('Spektrum von '+ index[i])

#plotte lin reg
plt.figure(2)
ax1 = plt.subplot(211)
plt.errorbar(x, y, xerr = ex, fmt = '.', color = 'b')
plt.plot(x, sol[0][1] * x + sol[0][0], color = 'r')
plt.title('Kalibration')
plt.ylabel('Energie [eV]')
plt.figtext(0.15,0.7,
            'Model: y = a $\cdot$ x + b \n'
            +'a= ('+ str(np.round(sol[0][1],5)) + ' $\pm$ '+ str(np.round(sol[1][1],5)) + ') eV/ch \n'
            +'b= ('+ str(np.round(sol[0][0],2)) + ' $\pm$ '+ str(np.round(sol[1][0],2)) + ') eV \n'
            +'$\chi ^2$/ndof= ' + str(np.round(sol[2], 2)))
ax2=plt.subplot(212,sharex=ax1)
H = np.full(len(x), 0.5)
H_err = np.full(len(x), 0.5)
for i in range(len(x)):
    H[i] = y[i] - sol[0][1] * x[i] - sol[0][0]
    H_err[i] = np.sqrt((sol[0][1] * ex[i])**2)
plt.errorbar(x, H, yerr = H_err, fmt = '.', color = 'b')
x_r = np.array([min(x), max(x)])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color = 'r')
plt.ylabel('Residuen [eV]')
plt.xlabel('Channel')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))