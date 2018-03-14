# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:18:55 2018

@author: grldm
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit
import STM_Methoden as STMM

start_time=timeit.default_timer()

data_index = [132, 297, 644, 1269]
data_nach = []
data_vor = []
for i in range(len(data_index)):
    data_vor.append(STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 1)) 
    data_nach.append(STMM.lese_Profillinie_ein_Kante(data_index[i], vor = 0))

#abgelesene Schätzwerte für die Position der Kante
vor_kante_vor = [98, 50, 73, 58]
nach_kante_vor = [111, 61, 92, 86]
vor_kante_nach = [93, 50, 74, 42]
nach_kante_nach = [104, 60, 85, 68]

kante_vor = [103, 57, 87, 62]
kante_nach = [99, 52, 80, 47]

#lineare Regressionen an Bereich vor und hinter Kante, betrachte Datensatz k
sig_x = 0.1/np.sqrt(12)
sig_y = 0.2/np.sqrt(12)
vor_sol_vor, nach_sol_vor, vor_sol_nach, nach_sol_nach = STMM.multi_lin_reg(data_nach, data_vor, vor_kante_vor, nach_kante_vor, vor_kante_nach, nach_kante_nach, sig_x, sig_y)

#berechne Höhe der Kante mit Gerade, die senkrecht auf der Geraden hinter der Kante steht und durch 
#die abgelesenen Kantenmittelpunkte geht
a_k_nach = -1./nach_sol_nach[:,0]
a_k_vor = -1./nach_sol_vor[:,0]
b_k_nach = []
b_k_vor = []
for i in range(len(a_k_nach)):
    b_k_nach.append(data_nach[i][kante_nach[i]][1] - a_k_nach[i] * data_nach[i][kante_nach[i]][0])
    b_k_vor.append(data_vor[i][kante_vor[i]][1] - a_k_vor[i] * data_vor[i][kante_vor[i]][0])
b_k_nach = np.array(b_k_nach)
b_k_vor = np.array(b_k_vor)
x1_nach = (b_k_nach - nach_sol_nach[:,2])/(nach_sol_nach[:,0] - a_k_nach)
x2_nach = (b_k_nach - vor_sol_nach[:,2])/(vor_sol_nach[:,0] - a_k_nach)
y1_nach = a_k_nach * x1_nach + b_k_nach
y2_nach = a_k_nach * x2_nach + b_k_nach
h_nach_m = np.sqrt((x1_nach - x2_nach)**2 + (y1_nach - y2_nach)**2)

x1_vor = (b_k_vor - nach_sol_vor[:,2])/(nach_sol_vor[:,0] - a_k_vor)
x2_vor = (b_k_vor - vor_sol_vor[:,2])/(vor_sol_vor[:,0] - a_k_vor)
y1_vor = a_k_vor * x1_vor + b_k_vor
y2_vor = a_k_vor * x2_vor + b_k_vor
h_vor_m = np.sqrt((x1_vor - x2_vor)**2 + (y1_vor - y2_vor)**2)

#Berechne Fehler mit Verschiebemethode
h_nach = STMM.verschiebemethode(nach_sol_nach, vor_sol_nach, data_nach, kante_nach)
h_vor = STMM.verschiebemethode(nach_sol_vor, vor_sol_vor, data_vor, kante_vor)
max_h_nach_index = []
min_h_nach_index = []
max_h_vor_index = []
min_h_vor_index = []
for i in range(4):
    max_h_nach_index_z = AM.getmax_1d(h_nach[:,i])
    min_h_nach_index_z = AM.getmax_1d(-h_nach[:,i])
    max_h_vor_index_z = AM.getmax_1d(h_vor[:,i])
    min_h_vor_index_z = AM.getmax_1d(-h_vor[:,i])
    max_h_nach_index.append(max_h_nach_index_z)
    min_h_nach_index.append(min_h_nach_index_z)
    max_h_vor_index.append(max_h_vor_index_z)
    min_h_vor_index.append(min_h_vor_index_z)
nach_st = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1]
vor_st = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
nach_ab = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]
vor_ab = [1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1]

print 'h_nach:', h_nach_m, '\n'
print 'h_nach_max:', h_nach[max_h_nach_index[0][0]][0], h_nach[max_h_nach_index[1][0]][1], h_nach[max_h_nach_index[2][0]][2], h_nach[max_h_nach_index[3][0]][3], '\n'
print 'h_nach_min:', h_nach[min_h_nach_index[0][0]][0], h_nach[min_h_nach_index[1][0]][1], h_nach[min_h_nach_index[2][0]][2], h_nach[min_h_nach_index[3][0]][3], '\n'
print 'h_vor:', h_vor_m, '\n'
print 'h_vor_max:', h_vor[max_h_vor_index[0][0]][0], h_vor[max_h_vor_index[1][0]][1], h_vor[max_h_vor_index[2][0]][2], h_vor[max_h_vor_index[3][0]][3], '\n'
print 'h_vor_min:', h_vor[min_h_vor_index[0][0]][0], h_vor[min_h_vor_index[1][0]][1], h_vor[min_h_vor_index[2][0]][2], h_vor[min_h_vor_index[3][0]][3]

#Plotte Datensatz e für vor = 1 in Vorwaerts- und für vor = 0 in Rueckwaertsrichtung
e = 0
vor = 1
if vor:
    plt.figure(1)
    ax1=plt.subplot(211)
    x_vor = np.array([data_vor[e][0][0], data_vor[e][vor_kante_vor[e]][0]])
    x_nach = np.array([data_vor[e][nach_kante_vor[e]][0], data_vor[e][-1][0]])
    plt.plot(x_vor, vor_sol_vor[e][0] * x_vor + vor_sol_vor[e][2], color = 'r')
    #plt.plot(x_vor, (vor_sol_vor[e][0] + vor_sol_vor[e][1]) * x_vor + (vor_sol_vor[e][2] + vor_sol_vor[e][3]), color = 'r')
    plt.plot(x_nach, nach_sol_vor[e][0] * x_nach + nach_sol_vor[e][2], color = 'r')
    plt.plot(x_vor, (vor_sol_vor[e][0] + vor_st[max_h_vor_index[e][0]] * vor_sol_vor[e][1]) * x_vor + (vor_sol_vor[e][2] + vor_ab[max_h_vor_index[e][0]] * vor_sol_vor[e][3]), color = 'y')
    plt.plot(x_nach, (nach_sol_vor[e][0] + nach_st[max_h_vor_index[e][0]] * nach_sol_vor[e][1]) * x_nach + (nach_sol_vor[e][2] + nach_ab[max_h_vor_index[e][0]] * nach_sol_vor[e][3]), color = 'y')
    plt.plot(x_vor, (vor_sol_vor[e][0] + vor_st[min_h_vor_index[e][0]] * vor_sol_vor[e][1]) * x_vor + (vor_sol_vor[e][2] + vor_ab[min_h_vor_index[e][0]] * vor_sol_vor[e][3]), color = 'b')
    plt.plot(x_nach, (nach_sol_vor[e][0] + nach_st[min_h_vor_index[e][0]] * nach_sol_vor[e][1]) * x_nach + (nach_sol_vor[e][2] + nach_ab[min_h_vor_index[e][0]] * nach_sol_vor[e][3]), color = 'b')
    #plt.figtext(0.2,0.75,
    #            'a= '+ str(np.round(steigung[e],5)) + '\n'
    #            +'$\Sigma$= ' + str(np.round(abst[e], 5)))
    halbe_kantenbreite = [0.17, 0.017, 0.008, 0.025]
    x_h = np.array([data_vor[e][kante_vor[e]][0] - halbe_kantenbreite[e], data_vor[e][kante_vor[e]][0] + halbe_kantenbreite[e]])
    plt.plot(x_h, a_k_vor[e] * x_h + b_k_vor[e], color = 'orange')
    plt.plot(data_vor[e][:,0], data_vor[e][:,1], color = 'g')
    plt.ylabel('Z [nm]')
    plt.title('Hoehenprofil der Kante bei ({0:5.1f} x {0:5.1f}) nm$^2$ Aufloesung'.format(float(data_index[e]) / 10))

    ax2=plt.subplot(212,sharex=ax1)
    plt.ylabel('Residuen [nm]')
    plt.xlabel('X [nm]')
    x_r = np.array([0, data_vor[e][-1][0]])
    y_r = np.array([0, 0])
    H_vor = np.full(vor_kante_vor[e], 0.5)
    H_vor_err = np.full(vor_kante_vor[e], 0.5)
    H_nach = np.full(len(data_vor[e][:,0]) - nach_kante_vor[e] - 1, 0.5)
    H_nach_err = np.full(len(data_vor[e][:,0]) - nach_kante_vor[e] - 1, 0.5)
    for i in range(vor_kante_vor[e]):
        H_vor[i] = data_vor[e][i][1] - vor_sol_vor[e][0] * data_vor[e][i][0] - vor_sol_vor[e][2]
        H_vor_err[i] = np.sqrt(sig_y**2 + (vor_sol_vor[e][0] * sig_x)**2)
    for i in range(len(data_vor[e][:,0]) - nach_kante_vor[e] - 1):
        H_nach[i] = data_vor[e][i + nach_kante_vor[e] + 1][1] - nach_sol_vor[e][0] * data_vor[e][i + nach_kante_vor[e] + 1][0] - nach_sol_vor[e][2]
        H_nach_err[i] = np.sqrt(sig_y**2 + (nach_sol_vor[e][0] * sig_x)**2)
    plt.plot(x_r, y_r, color='r')
    plt.errorbar(data_vor[e][:,0][0:vor_kante_vor[e]], H_vor, yerr=H_vor_err, fmt='.', color='b')
    plt.errorbar(data_vor[e][:,0][nach_kante_vor[e]:-1], H_nach, yerr=H_nach_err, fmt='.', color='b')
    plt.show()
else:
    plt.figure(1)
    ax1=plt.subplot(211)
    x_vor = np.array([data_nach[e][0][0], data_nach[e][vor_kante_nach[e]][0]])
    x_nach = np.array([data_nach[e][nach_kante_nach[e]][0], data_nach[e][-1][0]])
    plt.plot(x_vor, vor_sol_nach[e][0] * x_vor + vor_sol_nach[e][2], color = 'r')
    plt.plot(x_nach, nach_sol_nach[e][0] * x_nach + nach_sol_nach[e][2], color = 'r')
    plt.plot(x_vor, (vor_sol_nach[e][0] + vor_st[max_h_nach_index[e][0]] * vor_sol_nach[e][1]) * x_vor + (vor_sol_nach[e][2] + vor_ab[max_h_nach_index[e][0]] * vor_sol_nach[e][3]), color = 'y')
    plt.plot(x_nach, (nach_sol_nach[e][0] + nach_st[max_h_nach_index[e][0]] * nach_sol_nach[e][1]) * x_nach + (nach_sol_nach[e][2] + nach_ab[max_h_nach_index[e][0]] * nach_sol_nach[e][3]), color = 'y')
    plt.plot(x_vor, (vor_sol_nach[e][0] + vor_st[min_h_nach_index[e][0]] * vor_sol_nach[e][1]) * x_vor + (vor_sol_nach[e][2] + vor_ab[min_h_nach_index[e][0]] * vor_sol_nach[e][3]), color = 'b')
    plt.plot(x_nach, (nach_sol_nach[e][0] + nach_st[min_h_nach_index[e][0]] * nach_sol_nach[e][1]) * x_nach + (nach_sol_nach[e][2] + nach_ab[min_h_nach_index[e][0]] * nach_sol_nach[e][3]), color = 'b')
    #plt.figtext(0.2,0.75,
    #            'a= '+ str(np.round(steigung[e],5)) + '\n'
    #            +'$\Sigma$= ' + str(np.round(abst[e], 5)))
    halbe_kantenbreite = [0.15, 0.007, 0.0018, 0.05]
    x_h = np.array([data_nach[e][kante_nach[e]][0] - halbe_kantenbreite[e], data_nach[e][kante_nach[e]][0] + halbe_kantenbreite[e]])
    plt.plot(x_h, a_k_nach[e] * x_h + b_k_nach[e], color = 'orange')
    plt.plot(data_nach[e][:,0], data_nach[e][:,1], color = 'g')
    plt.ylabel('Z [nm]')
    plt.title('Hoehenprofil der Kante bei ({0:5.1f} x {0:5.1f}) nm$^2$ Aufloesung'.format(float(data_index[e]) / 10))

    ax2=plt.subplot(212,sharex=ax1)
    plt.ylabel('Residuen [nm]')
    plt.xlabel('X [nm]')
    x_r = np.array([0, data_nach[e][-1][0]])
    y_r = np.array([0, 0])
    H_vor = np.full(vor_kante_nach[e], 0.5)
    H_vor_err = np.full(vor_kante_nach[e], 0.5)
    H_nach = np.full(len(data_nach[e][:,0]) - nach_kante_nach[e] - 1, 0.5)
    H_nach_err = np.full(len(data_nach[e][:,0]) - nach_kante_nach[e] - 1, 0.5)
    for i in range(vor_kante_nach[e]):
        H_vor[i] = data_nach[e][i][1] - vor_sol_nach[e][0] * data_nach[e][i][0] - vor_sol_nach[e][2]
        H_vor_err[i] = np.sqrt(sig_y**2 + (vor_sol_nach[e][0] * sig_x)**2)
    for i in range(len(data_nach[e][:,0]) - nach_kante_nach[e] - 1):
        H_nach[i] = data_nach[e][i + nach_kante_nach[e] + 1][1] - nach_sol_nach[e][0] * data_nach[e][i + nach_kante_nach[e] + 1][0] - nach_sol_nach[e][2]
        H_nach_err[i] = np.sqrt(sig_y**2 + (nach_sol_nach[e][0] * sig_x)**2)
    plt.plot(x_r, y_r, color='r')
    plt.errorbar(data_nach[e][:,0][0:vor_kante_nach[e]], H_vor, yerr=H_vor_err, fmt='.', color='b')
    plt.errorbar(data_nach[e][:,0][nach_kante_nach[e]:-1], H_nach, yerr=H_nach_err, fmt='.', color='b')
    plt.show()

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))