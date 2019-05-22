import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import matplotlib.pyplot as plt
import csv

profile = 8
path = '../Daten/Tapping Mode Profiles/try3_profile{0:1.0f}.prf'.format(profile)
data = np.genfromtxt(path, delimiter = ' ', skip_header = 127)
x, y, sig_x, sig_y = data[:,0], data[:,1], np.full(len(data[:,0]), 0.01), np.full(len(data[:,0]), (data[:,0][1] - data[:,0][0])/np.sqrt(12))
print(np.shape(data))

start_index, end_index = [], [] #[0, 7, 14, 42, 52], [6, 13, 40, 50, 59]
#path = '../Daten/Contact Mode Profiles/' + direction + '_direction/try{0:1.0f}_profile{1:1.0f}.prf'.format(tri, profile)
csv_file = '../Daten/Tapping Mode Profiles/start_index.csv'
with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for line in reader:
        start_index.append([int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4])])
        end_index.append([int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5])])
    start_index, end_index = np.array(start_index), np.array(end_index)
labels = ['X [$\mu$m]', 'Z [nm]', 'Residuals [nm]', '']
save_path = 'test.png'
out = STMM.multi_lin_reg_one_plot(x, y, sig_x, sig_y, start_index[profile-1], end_index[profile-1], labels, save_path)
#print(out)
