# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 16:38:04 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import PH_Methoden as PH
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

speichern = 0

data = np.genfromtxt("../../Daten/Haupversuch/ProbeX1.dat", delimiter = '\t', dtype = np.float)
T = data[:,0]
U = - data[:,1] - 1.7346600000000003 #PH.offset(T, data[:,1])
sT = np.full(len(T), 0.01/np.sqrt(12))
sU = np.full(len(U), 0.001/np.sqrt(12))
##########Konstanten###############
s = 10**(-3)
C = 8034.7
V = 22.9 * 10**(-9)
n_M = 0.27
v = 10./s
##########Fehler auf Konstanten#####
sC = 34.7
sv = v * 0.1
sV = V * np.sqrt((0.00002/(np.sqrt(12) * 0.00295))**2 + (np.sqrt(2 * (0.00001/(np.sqrt(12) * 2))**2)/0.00335)**2)
sn_M = 0.01/np.sqrt(12)
####################################

chi = U / (C * v * V * (1-n_M))
schi = sU / (C * v * V * (1-n_M))
schi_sys = chi * np.sqrt((sC/C)**2 + (sv/v)**2 + (sV/V)**2 + (sn_M/(1-n_M))**2)

#############Curie-Weiss-Gesetz Anpassung######################################
T_1_CW, T_2_CW = 180, 190
T_CW, chi_CW, sT_CW, schi_CW = AM.untermenge_daten(T, 1./chi, sT, schi/chi**2, T_1_CW, T_2_CW)
sol_CW = p.lineare_regression_xy(T_CW, chi_CW, sT_CW, schi_CW)
T_C_CW = -sol_CW[2] / sol_CW[0]
sT_C_CW = T_C_CW * np.sqrt((sol_CW[1] / sol_CW[0])**2 + (sol_CW[3] / sol_CW[2])**2)
################################################################################

#############Curie-Weiss-Gesetz Anpassung - systematische Fehler################
T1_CW, chi1_CW, sT1_CW, schi1_CW = AM.untermenge_daten(T, 1./(chi + schi_sys), sT, schi/(chi + schi_sys)**2, T_1_CW, T_2_CW)
sol1_CW = p.lineare_regression_xy(T1_CW, chi1_CW, sT1_CW, schi1_CW)
T_C1_CW = -sol1_CW[2] / sol1_CW[0]
T2_CW, chi2_CW, sT2_CW, schi2_CW = AM.untermenge_daten(T, 1./(chi - schi_sys), sT, schi/(chi - schi_sys)**2, T_1_CW, T_2_CW)
sol2_CW = p.lineare_regression_xy(T2_CW, chi2_CW, sT2_CW, schi2_CW)
T_C2_CW = -sol2_CW[2] / sol2_CW[0]
################################################################################

#############Curie-Weiss-Gesetz Anpassung für Annäherung an T_C#################
g = 4./3
T_1_g, T_2_g = 170, 180
T_g, chi_g, sT_g, schi_g = AM.untermenge_daten(T, 1./(chi)**g, sT, g*schi/chi**(1+g), T_1_g, T_2_g)
sol_g = p.lineare_regression_xy(T_g, chi_g, sT_g, schi_g)
T_C_g = -sol_g[2] / sol_g[0]
sT_C_g = T_C_g * np.sqrt((sol_g[1] / sol_g[0])**2 + (sol_g[3] / sol_g[2])**2)
################################################################################

###Curie-Weiss-Gesetz Anpassung für Annäherung an T_C - systematische Fehler###
T1_g, chi1_g, sT1_g, schi1_g = AM.untermenge_daten(T, 1./(chi + schi_sys)**g, sT, g*schi/(chi + schi_sys)**(1+g), T_1_g, T_2_g)
sol1_g = p.lineare_regression_xy(T1_g, chi1_g, sT1_g, schi1_g)
T_C1_g = -sol1_CW[2] / sol1_CW[0]
T2_g, chi2_g, sT2_g, schi2_g = AM.untermenge_daten(T, 1./(chi - schi_sys)**g, sT, g*schi/(chi - schi_sys)**(1+g), T_1_g, T_2_g)
sol2_g = p.lineare_regression_xy(T2_g, chi2_g, sT2_g, schi2_g)
T_C2_g = -sol2_g[2] / sol2_g[0]
################################################################################

print '$T_C^(CW)$ = ', T_C_CW, ' +/- ', sT_C_CW, ' (stat) + ', T_C_CW - T_C2_CW,' - ', T_C1_CW - T_C_CW, ' (sys)'
print '$T_C^(g)$ = ', T_C_g, ' +/- ', sT_C_g, ' (stat) + ', T_C_g - T_C2_g,' - ', T_C1_g - T_C_g, ' (sys)'

#Plotte gesamte Messung
plt.close('all')
plt.figure(1)
plt.errorbar(T, chi, xerr = sT, yerr = schi, fmt = '.', color = 'b', label = 'Messwerte')
plt.title('Verlauf der Suszepibilitaet ueber gesamte Messung')
plt.ylabel('$\chi$')
plt.xlabel('T [K]')
plt.legend()
if speichern == 1:
    plt.savefig("../../Protokoll/Bilder/Haupt_Probe/Suszeptibilitaet_Verlauf")

#Plotte Bereich T > T_C für Curie-Weiss-Gesetz Anpassung
plt.figure(2)
ax1=plt.subplot(211)
plt.plot(T_CW, sol_CW[0] * T_CW + sol_CW[2], color = 'r', label = 'Curie-Weiss-Gesetz Anpassung')
plt.errorbar(T_CW, chi_CW, xerr = sT_CW, yerr = schi_CW, fmt = ',', linewidth = 2.5, color = 'b', label = 'Messwerte')
plt.figtext(0.15,0.65,
            'Model: y = a $\cdot$ x + b \n'
            +'$a$= ('+ str(np.round(sol_CW[0],5)) + ' $\pm$ '+ str(np.round(sol_CW[1],5)) + ') 1/K \n'
            +'$b$= '+ str(np.round(sol_CW[2],3)) + ' $\pm$ '+ str(np.round(sol_CW[3],3)) + ' \n'
            +'$\chi ^2$/ndof= ' + str(np.round(sol_CW[4], 2)))
plt.title('Verlauf der Suszepibilitaet fuer T > $T_C$')
plt.ylabel('$\dfrac{1}{\chi}$')
#plt.legend()
ax2=plt.subplot(212,sharex=ax1)
H = np.full(len(T_CW), 0.5)
H_err = np.full(len(T_CW), 0.5)
for i in range(len(T_CW)):
     H[i] = chi_CW[i] - sol_CW[0] * T_CW[i] - sol_CW[2]
     H_err[i] = np.sqrt(schi_CW[i]**2 + (sol_CW[0] * sT_CW[i])**2)
plt.errorbar(T_CW, H, yerr = H_err, fmt = ',', linewidth = 2.5, color = 'b')
plt.axhline(0.0, color = 'r')
plt.ylabel('Residuen')
plt.xlabel('T [K]')
if speichern == 1:
    plt.savefig("../../Protokoll/Bilder/Haupt_Probe/CurieWeiss")

#Plotte Bereich Annäherung von T an T_C für Curie-Weiss-Gesetz Anpassung
plt.figure(3)
ax1=plt.subplot(211)
plt.plot(T_g, sol_g[0] * T_g + sol_g[2], color = 'r', label = 'Anpassung')
plt.errorbar(T_g, chi_g, xerr = sT_g, yerr = schi_g, fmt = ',', linewidth = 2.5, color = 'b', label = 'Messwerte')
plt.figtext(0.15,0.65,
            'Model: y = a $\cdot$ x + b \n'
            +'$a$= ('+ str(np.round(sol_g[0],4)) + ' $\pm$ '+ str(np.round(sol_g[1],4)) + ') 1/K \n'
            +'$b$= '+ str(np.round(sol_g[2],2)) + ' $\pm$ '+ str(np.round(sol_g[3],2)) + ' \n'
            +'$\chi ^2$/ndof= ' + str(np.round(sol_g[4], 2)))
plt.title('Verlauf der Suszepibilitaet fuer T > $T_C$')
plt.ylabel('$\dfrac{1}{\chi ^{\gamma}}$')
#plt.legend()
ax2=plt.subplot(212,sharex=ax1)
H = np.full(len(T_g), 0.5)
H_err = np.full(len(T_g), 0.5)
for i in range(len(T_g)):
     H[i] = chi_g[i] - sol_g[0] * T_g[i] - sol_g[2]
     H_err[i] = np.sqrt(schi_g[i]**2 + (sol_g[0] * sT_g[i])**2)
plt.errorbar(T_g, H, yerr = H_err, fmt = ',', linewidth = 2.5, color = 'b')
plt.axhline(0.0, color = 'r')
plt.ylabel('Residuen')
plt.xlabel('T [K]')
if speichern == 1:
    plt.savefig("../../Protokoll/Bilder/Haupt_Probe/CurieWeiss_gamma")

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))