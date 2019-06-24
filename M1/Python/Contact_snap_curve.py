import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import matplotlib.pyplot as plt
import csv

path = '../Daten/Contact Mode/Snap_Curve.csv'
data = np.array(AM.genfromcsv(path, skipheader=1)) * 10**(-6)

dz, T_B = data[:,1], data[:,3]

font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

fig = plt.figure()
plt.rc('font', **font)
plt.plot(dz, T_B)
plt.xlabel('dz [nm]', **font)
plt.ylabel('T-B [mV]', **font)
#plt.title('Snap-In Curve')
plt.grid()
plt.tight_layout()
plt.savefig('../Protokoll/Bilder/Contact_Mode/Snap_in_curve.png')
plt.close(fig)

start_index, end_index = [0, 845], [290, 1024]
labels = ['Z [nm]', 'T-B [mV]', 'Residuals [mV]', '']
sig_x, sig_y = np.full(len(dz), (dz[1] - dz[0])/np.sqrt(12)), np.full(len(T_B), 0.01)
save_path = '../Protokoll/Bilder/Contact_Mode/Snap_in_curve_fit.png'
out = STMM.multi_lin_reg_one_plot(dz, T_B, sig_x, sig_y, start_index, end_index, labels, save_path)

diff = (out[0][0] - out[1][0])/np.sqrt(out[0][1]**2 + out[1][1]**2)
print(diff)

k_fit = AM.gew_mittelwert(np.array([out[0][0], out[1][0]]), np.array([out[0][1], out[1][1]]))[0] #mV/nm
sig_k_fit = np.max(AM.gew_mittelwert(np.array([out[0][0], out[1][0]]), np.array([out[0][1], out[1][1]]))[1:])
print(k_fit, sig_k_fit)
print(-sig_k_fit/k_fit)

k_real, sig_k_real_p, sig_k_real_m = 0.18, 0.22/np.sqrt(12), 0.12/np.sqrt(12) #N/m
k_z, sig_k_z = 0.7529706599727144, 0.08560303129030458 #kalibrationskonstante z-richtung

alpha = np.abs(k_real * k_z / (k_fit * 10**(9))) #N/mV
sig_alpha_p = alpha * np.sqrt((sig_k_fit / k_fit)**2 + (sig_k_real_p/k_real)**2)
sig_alpha_m = alpha * np.sqrt((sig_k_fit / k_fit)**2 + (sig_k_real_m/k_real)**2)

print('Umrechenfaktor:')
print('alpha = (' + str(alpha) + ' + ' + str(sig_alpha_p) + ' - ' + str(sig_alpha_m) + ' (stat.) +/- ' + str(alpha * sig_k_z/k_z) + ' (sys.)) N/mV')

#adhesion
save_path = '../Protokoll/Bilder/Contact_Mode/adhesion_and_load_force_fit.png' #'test.png'
out = STMM.multi_lin_reg_one_plot(dz, T_B, sig_x, sig_y, [300], [550], labels, save_path)

adhesion = (out[0][2] - min(T_B)) * alpha
sig_theta, theta = np.sqrt(out[0][3]**2 + 0.01**2), out[0][2] - min(T_B)
sig_adhesion = adhesion * np.abs(sig_theta/theta)
sig_adhesion_m = adhesion * np.abs(sig_alpha_m/alpha)
sig_adhesion_p = adhesion * np.abs(sig_alpha_p/alpha)
print('Adhesion force:')
print('F_a = (' + str(adhesion) + ' +/- ' + str(sig_adhesion) + ' (stat.) + ' + str(sig_adhesion_p) + ' - ' + str(sig_adhesion_m) + ' (sys.)) N')

#load force
index = np.where(dz <= 1.0)[0]
load = alpha * np.abs(T_B[index[0]] - T_B[index[1]])
sig_load = alpha * np.sqrt((T_B[index[0]+1] - T_B[index[0]])**2 /12 + (T_B[index[1]-1] - T_B[index[1]])**2 /12)
sig_load_m = load * np.abs(sig_alpha_m/alpha)
sig_load_p = load * np.abs(sig_alpha_p/alpha)
print('Load force:')
print('F_l = (' + str(load) + ' +/- ' + str(sig_load) + ' (stat.) + ' + str(sig_load_p) + ' - ' + str(sig_load_m) + ' (sys.)) N')
