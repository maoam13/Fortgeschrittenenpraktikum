import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import matplotlib.pyplot as plt
import csv

def hoehe_breite(path, start_index, end_index):
    #data = np.genfromtxt("../Daten/Contact Mode Profiles/x_direction/try{0:1.0f}_profile{1:1.0f}.prf".format(tri, profile), delimiter = ' ', skip_header = 127)
    data = np.genfromtxt(path, delimiter = ' ', skip_header = 127)
    #print(len(data))

    x, y, sig_x, sig_y = data[:,0], data[:,1], np.full(len(data[:,0]), 0.01), np.full(len(data[:,0]), (data[:,0][1] - data[:,0][0])/np.sqrt(12))
    
    labels = ['X [$\mu$m]', 'Z [nm]', 'Residuals [nm]', '']
    save_path = '../Protokoll/Bilder/' + path.split('/')[-3].split(' ')[0] + ' ' + path.split('/')[-3].split(' ')[1] + '/fit_' + path.split('/')[-2] + '/' + path.split('/')[-1].split('.')[0] + '.png'
    out = STMM.multi_lin_reg_one_plot(x, y, sig_x, sig_y, start_index, end_index, labels, save_path)

    schnitt_x, schnitt_y = np.zeros(len(out)-1), np.zeros(len(out)-1)
    for i in range(len(out) - 1):
        schnitt_x[i], schnitt_y[i] = STMM.geraden_schnittpunkte(out[i][0], out[i][2], out[i+1][0], out[i+1][2])

    hoehe = (schnitt_y[0] - schnitt_y[1] + schnitt_y[3] - schnitt_y[2])/2
    breite = (schnitt_x[3] - schnitt_x[0] + schnitt_x[2] - schnitt_x[1])/2
    return hoehe, breite

def radius_x():
    tri, direction = 1, 'x'
    h, b = [], []
    for profile in np.arange(1, 9):
        start_index, end_index = [], [] #[0, 7, 14, 42, 52], [6, 13, 40, 50, 59]
        path = '../Daten/Contact Mode Profiles/' + direction + '_direction/try{0:1.0f}_profile{1:1.0f}.prf'.format(tri, profile)
        csv_file = '../Daten/Contact Mode Profiles/' + direction + '_direction/start_index.csv'
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for line in reader:
                start_index.append([int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4])])
                end_index.append([int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5])])
            start_index, end_index = np.array(start_index), np.array(end_index)
        hoehe, breite = hoehe_breite(path, start_index[profile-1], end_index[profile-1])
        h.append(hoehe), b.append(breite)
    h_mean, h_sig = np.mean(np.array(h)), np.std(np.array(h), ddof = 1)
    b_mean, b_sig = np.mean(np.array(b)), np.std(np.array(b), ddof = 1)
    return h_mean, h_sig, b_mean, b_sig

def radius_y():
    tri, direction = 1, 'y'
    h, b = [], []
    for profile in np.array([2, 4, 5, 6, 7, 8]):
        start_index, end_index = [], [] #[0, 7, 14, 42, 52], [6, 13, 40, 50, 59]
        path = '../Daten/Contact Mode Profiles/' + direction + '_direction/try{0:1.0f}_profile{1:1.0f}.prf'.format(tri, profile)
        csv_file = '../Daten/Contact Mode Profiles/' + direction + '_direction/start_index.csv'
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for line in reader:
                start_index.append([int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4])])
                end_index.append([int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5])])
            start_index, end_index = np.array(start_index), np.array(end_index)
        hoehe, breite = hoehe_breite(path, start_index[profile-1], end_index[profile-1])
        h.append(hoehe), b.append(breite)
    h_mean, h_sig = np.mean(np.array(h)), np.std(np.array(h), ddof = 1)
    b_mean, b_sig = np.mean(np.array(b)), np.std(np.array(b), ddof = 1)
    return h_mean, h_sig, b_mean, b_sig

if __name__ == '__main__':
    #hoehe in nm, breite in \mu m
    x = radius_x()
    y = radius_y()
    print(x)
    print(y)
    print((x[0] - y[0])/(np.sqrt(x[1]**2 + y[1]**2)))

