# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:56:29 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import Methoden as m

start_time=timeit.default_timer()

###################Kalibration#############
a = 6.61537
b = -22.46
sa = 0.00191
def En(ch):
    return a * ch + b
###########################################

i = 3
index = ["Ag", "Cu", "I", "StainlessSteel"]
data = m.KalibrationEinlesen(i)
data_co = m.fft_cutoff(data)
data_x = np.arange(len(data))
E = En(data_x)
sE = np.full(len(data_x), np.abs(sa * a))

if 1:#i == 0:
    startwerte1 = [En(3350), 40 * a, En(670), 30389]
    startwerte2 = [En(3774), 28 * a, En(615), 5486]
    k1 = 3350
    k2 = 3774
    peak1_Ag = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(0)), startwerte1, k1, b1 = 40)
    peak2_Ag = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(0)), startwerte2, k2, b1 = 40)
if 1:#i == 1:
    startwerte1 = [En(1219), 16 * a, En(600), 66372]
    startwerte2 = [En(1350), 16 * a, En(600), 10346]
    k1 = 1219
    k2 = 1350
    peak1_Cu = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(1)), startwerte1, k1)
    peak2_Cu = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(1)), startwerte2, k2)
if 1:#i == 2:
    startwerte1, p1 = [En(4329), 27 * a, En(860), 20576, En(4291), 22 * a, 12739], 2
    startwerte2, p2 = [En(4885), 12 * a, En(660), 4465, En(5000), 50 * a, 1375], 2
    k1 = 4329
    k2 = 4885
#    startwerte1, p1 = [4310, 15, 200, 40000, 4300, 10, 24962], 2
#    startwerte2, p2 = [4885, 12, 660, 4465, 5000, 50, 1375], 2
    #startwerte3 = [5000, 50, 660, 1375]
    peak1_I = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(2)), startwerte1, k1, p = p1)
    peak2_I = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(2)), startwerte2, k2, p = p2)
if 1:#i == 3:
    startwerte1 = [En(2644), 20 * a, En(600), 12214]
    startwerte2 = [En(2968), 22 * a, En(600), 2444]
    k1 = 2644
    k2 = 2968
    peak1_SS = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(3)), startwerte1, k1)
    peak2_SS = m.peak_breite_best(E, sE, np.real(m.KalibrationEinlesen(3)), startwerte2, k2)

FWH = 2 * np.sqrt(2 * np.log(2)) * np.array([peak1_Ag[2], peak2_Ag[2], peak1_Cu[2], peak2_Cu[2], peak1_I[2], peak2_I[2], peak1_SS[2], peak2_SS[2]])
e_FWH = np.abs(2 * np.sqrt(2 * np.log(2)) * np.array([peak1_Ag[3], peak2_Ag[3], peak1_Cu[3], peak2_Cu[3], peak1_I[3], peak2_I[3], peak1_SS[3], peak2_SS[3]]))
E_pos = np.array([peak1_Ag[0], peak2_Ag[0], peak1_Cu[0], peak2_Cu[0], peak1_I[0], peak2_I[0], peak1_SS[0], peak2_SS[0]])
e_E_pos = np.abs(np.array([peak1_Ag[1], peak2_Ag[1], peak1_Cu[1], peak2_Cu[1], peak1_I[1], peak2_I[1], peak1_SS[1], peak2_SS[1]]))

FWH = 2 * np.sqrt(2 * np.log(2)) * np.array([peak1_Ag[2], peak2_Ag[2], peak1_Cu[2], peak2_Cu[2], peak1_SS[2]])
e_FWH = np.abs(2 * np.sqrt(2 * np.log(2)) * np.array([peak1_Ag[3], peak2_Ag[3], peak1_Cu[3], peak2_Cu[3], peak1_SS[3]]))
E_pos = np.array([peak1_Ag[0], peak2_Ag[0], peak1_Cu[0], peak2_Cu[0], peak1_SS[0]])
e_E_pos = np.abs(np.array([peak1_Ag[1], peak2_Ag[1], peak1_Cu[1], peak2_Cu[1], peak1_SS[1]]))

####lin reg
sol = p.lineare_regression_xy(np.sqrt(E_pos),FWH,np.abs(e_E_pos /(2*np.sqrt(E_pos))),e_FWH)

#plotte lin reg
plt.close('all')
plt.figure(1)
ax1 = plt.subplot(211)
plt.errorbar(np.sqrt(E_pos), FWH, xerr = np.abs(e_E_pos /(2*np.sqrt(E_pos))), yerr = e_FWH, fmt = '.', color = 'b')
plt.plot(np.sqrt(E_pos), sol[0] * np.sqrt(E_pos) + sol[2], color = 'r')
plt.title('Energieaufloesung')
plt.ylabel('$\Delta$ E')
plt.figtext(0.15,0.7,
            'Model: y = a $\cdot$ x + b \n'
            +'a= ('+ str(np.round(sol[0],5)) + ' $\pm$ '+ str(np.round(sol[1],5)) + ') $\sqrt{eV}$ \n'
            +'b= ('+ str(np.round(sol[2],2)) + ' $\pm$ '+ str(np.round(sol[3],2)) + ') eV \n'
            +'$\chi ^2$/ndof= ' + str(np.round(sol[4], 2)))
ax2=plt.subplot(212,sharex=ax1)
H = np.full(len(np.sqrt(E_pos)), 0.5)
H_err = np.full(len(np.sqrt(E_pos)), 0.5)
for i in range(len(np.sqrt(E_pos))):
    H[i] = FWH[i] - sol[0] * np.sqrt(E_pos)[i] - sol[2]
    H_err[i] = np.sqrt((sol[0] * np.abs(e_E_pos[i] /(2*np.sqrt(E_pos[i]))))**2 + e_FWH[i]**2)
plt.errorbar(np.sqrt(E_pos), H, yerr = H_err, fmt = '.', color = 'b')
x_r = np.array([min(np.sqrt(E_pos)), max(np.sqrt(E_pos))])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color = 'r')
plt.ylabel('Residuen')
plt.xlabel('$\sqrt{E}$ [$\sqrt{eV}$]')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))