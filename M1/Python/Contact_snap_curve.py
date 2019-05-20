import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import matplotlib.pyplot as plt
import csv

path = '../Daten/Contact Mode/Snap_Curve.csv'
data = np.array(AM.genfromcsv(path, skipheader=1)) * 10**(-6)
print(np.shape(data))

print(data[3])

fig = plt.figure()
plt.plot(data[:,1], data[:,3])
plt.xlabel('dz [nm]')
plt.ylabel('T-B [mV]')
plt.title('Snap-In Curve')
plt.savefig('../Protokoll/Bilder/Contact Mode/Snap_in_curve.png')
plt.close(fig)

start_index, end_index = [0, 845], [290, 1024]
labels = ['Z [nm]', 'T-B [mV]', 'Residuals [mV]', '']
sig_x, sig_y = np.full(len(data[:,1]), (data[:,1][1] - data[:,1][0])/np.sqrt(12)), np.full(len(data[:,3]), 0.01)
save_path = '../Protokoll/Bilder/Contact Mode/Snap_in_curve_fit.png'
out = STMM.multi_lin_reg_one_plot(data[:,1], data[:,3], sig_x, sig_y, start_index, end_index, labels, save_path)

print(out[0])
print(out[1])

diff = (out[0][0] - out[1][0])/np.sqrt(out[0][1]**2 + out[1][1]**2)
print(diff)

print(AM.gew_mittelwert(np.array([out[0][0], out[1][0]]), np.array([out[0][1], out[1][1]])))

k = AM.gew_mittelwert(np.array([out[0][0], out[1][0]]), np.array([out[0][1], out[1][1]]))[0] #mV/nm
sig_k = np.max(AM.gew_mittelwert(np.array([out[0][0], out[1][0]]), np.array([out[0][1], out[1][1]]))[1:])
print(k, sig_k)
print(-sig_k/k)

