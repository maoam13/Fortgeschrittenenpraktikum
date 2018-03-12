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
nach_kante_vor = [111, 61, 92, 67]
vor_kante_nach = [93, 50, 74, 42]
nach_kante_nach = [104, 60, 85, 68]

#lineare Regressionen an Bereich vor und hinter Kante, betrachte Datensatz k
sig_x = 0.4/np.sqrt(12)
sig_y = 0.4/np.sqrt(12)
vor_sol_vor, nach_sol_vor, vor_sol_nach, nach_sol_nach = STMM.multi_lin_reg(data_nach, data_vor, vor_kante_vor, nach_kante_vor, vor_kante_nach, nach_kante_nach, sig_x, sig_y)

#Plotte Datensatz e
e = 0
plt.figure(1)
x_vor = np.array([data_vor[e][0][0], data_vor[e][vor_kante_vor[e]][0]])
x_nach = np.array([data_vor[e][nach_kante_vor[e]][0], data_vor[e][-1][0]])
plt.plot(x_vor, vor_sol_vor[e][0] * x_vor + vor_sol_vor[e][2], color = 'r')
plt.plot(x_nach, nach_sol_vor[e][0] * x_nach + nach_sol_vor[e][2], color = 'r')
#plt.figtext(0.2,0.75,
#            'a= '+ str(np.round(steigung[e],5)) + '\n'
#            +'$\Sigma$= ' + str(np.round(abst[e], 5)))
plt.plot(data_vor[e][:,0], data_vor[e][:,1], color = 'g')
#plt.plot(data_nach[e][:,0], data_nach[e][:,1], color = 'b')
plt.xlabel('X [nm]')
plt.ylabel('Z [nm]')
plt.title('Hoehenprofil der Kante bei ({0:5.1f} x {0:5.1f}) nm$^2$ Aufloesung'.format(data_index[e] /10))

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))