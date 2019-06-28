import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import matplotlib.pyplot as plt
import csv


if __name__ == '__main__':
    k = 0.694620393244303
    plateau_data = []
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
        zwischen1 = (x[start_index[profile-1][0]:end_index[profile-1][0]] - np.mean(x[start_index[profile-1][0]:end_index[profile-1][0]])) * k
        zwischen2 = (x[start_index[profile-1][2]:end_index[profile-1][2]] - np.mean(x[start_index[profile-1][2]:end_index[profile-1][2]])) * k
        zwischen3 = (x[start_index[profile-1][4]:end_index[profile-1][4]] - np.mean(x[start_index[profile-1][4]:end_index[profile-1][4]])) * k
        plateau_data.extend(zwischen1)
        plateau_data.extend(zwischen2)
        plateau_data.extend(zwischen3)

    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}
    
    fig = plt.figure()
    plt.rc('font', **font)
    plt.hist(plateau_data, density=True, bins=30, color = 'b')
    plt.grid()
    plt.xlabel('Z - Z_mean [nm]', **font)
    plt.ylabel('relative frequency', **font)
    plt.tight_layout()
    plt.savefig('../Protokoll/Bilder/Tapping_Mode/Roughness_histogram.png')
    plt.close(fig)
