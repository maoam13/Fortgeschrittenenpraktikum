import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import matplotlib.pyplot as plt
import csv

def width():
    h, b = [], []
    csv_file = '../Daten/Tapping Mode Profiles/start_index.csv'
    for profile in np.array([1, 2, 4, 5, 6, 7, 8]):
        path = '../Daten/Tapping Mode Profiles/try3_profile{0:1.0f}.prf'.format(profile)
        data = np.genfromtxt(path, delimiter = ' ', skip_header = 127)
        x, y, sig_x, sig_y = data[:,0], data[:,1], np.full(len(data[:,0]), 0.01), np.full(len(data[:,0]), (data[:,0][1] - data[:,0][0])/np.sqrt(12))
        start_index, end_index = [], []
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for line in reader:
                start_index.append([int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4])])
                end_index.append([int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5])])
        start_index, end_index = np.array(start_index), np.array(end_index)
        labels = ['X [$\mu$m]', 'Z [nm]', 'Residuals [nm]', '']
        save_path = '../Protokoll/Bilder/Tapping_Mode/fit_' + 'try3_profile{0:1.0f}.png'.format(profile)
        out = STMM.multi_lin_reg_one_plot(x, y, sig_x, sig_y, start_index[profile-1], end_index[profile-1], labels, save_path)
        schnitt_x, schnitt_y = np.zeros(len(out)-1), np.zeros(len(out)-1)
        for i in range(len(out) - 1):
            schnitt_x[i], schnitt_y[i] = STMM.geraden_schnittpunkte(out[i][0], out[i][2], out[i+1][0], out[i+1][2])

        hoehe = (schnitt_y[0] - schnitt_y[1] + schnitt_y[3] - schnitt_y[2])/2
        breite = (schnitt_x[3] - schnitt_x[0] + schnitt_x[2] - schnitt_x[1])/2
        h.append(hoehe), b.append(breite)
    h_mean, h_sig = np.mean(np.array(h)), np.std(np.array(h), ddof = 1)
    print(h)
    b_mean, b_sig = np.mean(np.array(b)), np.std(np.array(b), ddof = 1)
    return h_mean, h_sig, b_mean, b_sig

if __name__ == '__main__':
    #hoehe in nm, breite in \mu m
    h_mean, h_sig, b_mean, b_sig = width()
    print(h_mean, h_sig, b_mean, b_sig)

    h_real, h_real_sig, b_real, b_real_sig = 19, 2, 4, 1./np.sqrt(12)

    k_h, k_h_sig = np.abs(h_real/h_mean), np.abs(h_real/h_mean) * np.sqrt((h_sig/h_mean)**2 + (h_real_sig/h_real)**2)
    k_b, k_b_sig = np.abs(b_real/b_mean), np.abs(b_real/b_mean) * np.sqrt((b_sig/b_mean)**2 + (b_real_sig/b_real)**2)

    print('Kalibrationskonstanten:')
    print('k_h = ' + str(k_h) + ' +/- ' + str(k_h_sig))
    print('k_b = ' + str(k_b) + ' +/- ' + str(k_b_sig))

