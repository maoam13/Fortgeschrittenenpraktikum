import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import Temp_kalibration as TK
import matplotlib.pyplot as plt
import csv

R_Ohm = 10**4
k = '43'
I = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH1.csv', delimiter=',', skip_header=18)[:,4] / R_Ohm
U = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH2.csv', delimiter=',', skip_header=18)[:,4] / R_Ohm

sig_U = np.full(len(U), np.std(np.genfromtxt('../Daten/ALL0030/F0030CH2.csv', delimiter=',', skip_header=18)[:,4] / R_Ohm))
sig_I = np.full(len(I), 0.2*10**(-6)/np.sqrt(12))

fig = plt.figure()
plt.errorbar(I * 10**6, U * 10**6, xerr=sig_I * 10**6, yerr=sig_U * 10**6, fmt = ',', color = 'b')
plt.xlabel('I [$\mu$A]')
plt.ylabel('U [$\mu$V]')
plt.grid()
plt.tight_layout()
plt.savefig('../Protokoll/Bilder/U_I_characteristic/characteristic.png')
plt.close(fig)

start_index, end_index = [0, 800, 1700], [650, 1500, 2482]
labels = ['I [$\mu$A]', 'U [$\mu$V]', 'Residuals [$\mu$V]', '']
save_path = '../Protokoll/Bilder/U_I_characteristic/fit_' + k + '.png'
out = STMM.multi_lin_reg_one_plot(I * 10**6, U * 10**6, sig_I * 10**6, sig_U * 10**6, start_index, end_index, labels, save_path)

#R_N
R_N = (out[0][0] + out[2][0])/2
sig_R_N = np.abs(out[0][0] - out[2][0])/np.sqrt(12)
print('R_N = (' + str(R_N) + ' +/- ' + str(sig_R_N) + ') Ohm')

#I_C
x1, sig_x1, y1, sig_y1 = STMM.geraden_schnittpunkte_fehler(out[0], out[1])
x2, sig_x2, y2, sig_y2 = STMM.geraden_schnittpunkte_fehler(out[1], out[2])

I_C = (np.abs(x1) + np.abs(x2))/2 * 10**(-6)
sig_I_C = 1./2 * np.sqrt(sig_x1**2 + sig_x2**2) * 10**(-6)
print('I_C = (' + str(I_C) + ' +/- ' + str(sig_I_C) + ') A')

#V_C
V_C = I_C * R_N
sig_V_C = np.sqrt((I_C * sig_R_N)**2 + (sig_I_C * R_N)**2)
print('V_C = (' + str(V_C) + ' +/- ' + str(sig_V_C) + ') V')
