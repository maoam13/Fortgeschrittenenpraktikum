import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import matplotlib.pyplot as plt
import csv

path = '../Daten/Tapping mode/amplitude_nah.csv'
data = np.genfromtxt(path, delimiter = ';', skip_header = 1)
z, amp = data[:,1] * 10**(-7), data[:,3] * 10**(-4)
sig_z, sig_amp = np.full(len(z), (z[1] - z[0])/np.sqrt(12)), np.full(len(z), np.std(amp[200:300])) #* 10**(-3)

fig = plt.figure()
plt.errorbar(z, amp, xerr = sig_z * 10**3, yerr = sig_amp, fmt = '.')
plt.grid()
plt.xlabel('Z [nm]')
plt.ylabel('Amplitude [mV]')
plt.tight_layout()
plt.savefig('../Protokoll/Bilder/Tapping_Mode/Snap_in_curve.png')
plt.close(fig)

#start_index, end_index = [0, 970], [60, 1024]
start_index, end_index = [0, 780], [240, 1024]
labels = ['Z [nm]', 'Amplitude [mV]', 'Residuals [mV]', '']
save_path = '../Protokoll/Bilder/Tapping_Mode/Snap_in_curve_fit.png'
out = STMM.multi_lin_reg_one_plot(z, amp, sig_z, sig_amp, start_index, end_index, labels, save_path)

print('a_1 = (' + str(out[0][0]) + ' +/- ' + str(out[0][1]) + ') mV/nm') #mV/nm
print('a_2 = (' + str(out[1][0]) + ' +/- ' + str(out[1][1]) + ') mV/nm')

k_fit, sig_k_fit = AM.gew_mittelwert(np.array([out[0][0], out[1][0]]), np.array([out[0][1], out[1][1]]))[0], np.max(AM.gew_mittelwert(np.array([out[0][0], out[1][0]]), np.array([out[0][1], out[1][1]]))[1:])
print(k_fit, sig_k_fit)

k_real, sig_k_real_p, sig_k_real_m = 40., 40./np.sqrt(12), 20./np.sqrt(12) #N/m
k_z, sig_k_z = 0.694620393244303, 0.07388999316538382 #kalibrationskonstante z-richtung

alpha = k_real * k_z / (k_fit * 10**(9)) #N/mV
sig_alpha_p = alpha * np.sqrt((sig_k_fit / k_fit)**2 + (sig_k_real_p/k_real)**2)
sig_alpha_m = alpha * np.sqrt((sig_k_fit / k_fit)**2 + (sig_k_real_m/k_real)**2)

print('Umrechenfaktor:')
print('alpha = (' + str(alpha) + ' + ' + str(sig_alpha_p) + ' - ' + str(sig_alpha_m) + ' (stat.) +/- ' + str(alpha * sig_k_z/k_z) + ' (sys.)) N/mV')


#free oszillation amplitude (plateau)
start_index, end_index = [280, 480], [460, 740]
labels = ['Z [nm]', 'Amplitude [mV]', 'Residuals [mV]', '']
save_path = '../Protokoll/Bilder/Tapping_Mode/Free_Oszillation_Amplitude.png'
out = STMM.multi_lin_reg_one_plot(z, amp, sig_z, sig_amp, start_index, end_index, labels, save_path)

print('a_1 = (' + str(out[0][0]) + ' +/- ' + str(out[0][1]) + ') mV/nm') #mV/nm
print('a_2 = (' + str(out[1][0]) + ' +/- ' + str(out[1][1]) + ') mV/nm')

b_fit, sig_b_fit = AM.gew_mittelwert(np.array([out[0][2], out[1][2]]), np.array([out[0][3], out[1][3]]))[0], np.max(AM.gew_mittelwert(np.array([out[0][2], out[1][2]]), np.array([out[0][3], out[1][3]]))[1:])
foa = b_fit / k_fit
sig_foa = foa * np.sqrt((sig_b_fit/b_fit)**2 + (sig_k_fit/k_fit)**2)

print('b = (' + str(b_fit) + ' +/- ' + str(sig_b_fit) + ') mV')

print('Free oszillation amplitude:')
print('amplitude = (' + str(foa) + ' +/- ' + str(sig_foa) + ') nm')
