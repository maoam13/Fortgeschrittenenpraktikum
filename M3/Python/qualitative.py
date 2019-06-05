# -*- coding: utf-8 -*-
"""
Created on Wed Jun 05 21:52:12 2019

@author: Moritz
"""
import numpy as np
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import Temp_kalibration as TK
import matplotlib.pyplot as plt
import Praktikummo2 as p

R_Ohm = 10**4
k = '51'
phi = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH1.csv', delimiter=',', skip_header=18)[:,4] / R_Ohm
U = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH2.csv', delimiter=',', skip_header=18)[:,4]
t = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH2.csv', delimiter=',', skip_header=18)[:,3]

sig_U = np.full(len(U), np.std(np.genfromtxt('../Daten/ALL0030/F0030CH2.csv', delimiter=',', skip_header=18)[:,4]))/10/np.sqrt(12)
sig_phi = np.full(len(phi), 0.2*10**(-6)/np.sqrt(12))

fig = plt.figure()
#plt.errorbar(t, U, yerr=sig_U, fmt = ',', color = 'b')
plt.plot(t,U,label = "no probe")
plt.xlabel('t [s]')
plt.ylabel('U [V]')
plt.grid()
plt.ylim(-0.7,-0.5)
plt.tight_layout()
plt.grid()

k = '53'
phi = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH1.csv', delimiter=',', skip_header=18)[:,4] / R_Ohm
U = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH2.csv', delimiter=',', skip_header=18)[:,4]
t = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH2.csv', delimiter=',', skip_header=18)[:,3]

sig_U = np.full(len(U), np.std(np.genfromtxt('../Daten/ALL0030/F0030CH2.csv', delimiter=',', skip_header=18)[:,4]))/10/np.sqrt(12)
sig_phi = np.full(len(phi), 0.2*10**(-6)/np.sqrt(12))

#plt.errorbar(t, U, yerr=sig_U, fmt = ',', color = 'r')
plt.plot(t,U,label = "iron")
plt.xlabel('t [s]',)
plt.ylabel('U [V]')
plt.grid()
#plt.ylim(-0.06,0.06)
plt.tight_layout()
plt.legend()