import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import Temp_kalibration as TK
import matplotlib.pyplot as plt
import csv

R_Ohm = 10**4
files = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
R_T = np.array([108, 100, 95, 90, 85, 78, 75, 70, 65, 60, 55, 50, 43, 36, 30, 26, 25, 24, 23, 22, 21, 20.3]) #k Ohm
T, sig_T = TK.temp_kalibration(R_T)

R, sig_R = [], []
for i in range(len(files)):
    I = np.genfromtxt('../Daten/ALL00' + files[i] + '/F00' + files[i] + 'CH1.csv', delimiter=',', skip_header=18)[:,4] / R_Ohm
    U = np.genfromtxt('../Daten/ALL00' + files[i] + '/F00' + files[i] + 'CH2.csv', delimiter=',', skip_header=18)[:,4]
    sig_U = np.full(len(U), np.std(np.genfromtxt('../Daten/ALL0030/F0030CH2.csv', delimiter=',', skip_header=18)[:,4]))
    sig_I = np.full(len(I), 0.2*10**(-6)/np.sqrt(12))
    start_index, end_index = [0], [len(U) - 1]
    labels = ['I [A]', 'U [V]', 'Residuals [V]', '']
    save_path = '../Protokoll/Bilder/Critical_Temperature/Resistance_fit_' + files[i] + '.png'
    out = STMM.multi_lin_reg_one_plot(I, U, sig_I, sig_U, start_index, end_index, labels, save_path)
    R.append(out[0][0]), sig_R.append(out[0][1]) #Ohm

fig = plt.figure()
plt.errorbar(T, np.array(R)*10**(-3), xerr=sig_T, yerr=np.array(sig_R)*10**(-3), fmt = '.', color = 'b')
plt.xlabel('T [K]')
plt.ylabel('R [k$\Omega$]')
plt.grid()
plt.tight_layout()
plt.savefig('../Protokoll/Bilder/Critical_Temperature/Temp_Resistance.png')
plt.close(fig)

i = AM.max_diff_index(R)[0]
T_C = (T[i] + T[i+1]) / 2
sig_T_C = (T[i] - T[i+1]) / np.sqrt(12)

print('Critical Temperature:')
print('T_C = (' + str(T_C) + ' +/- ' + str(sig_T_C) + ') K')
