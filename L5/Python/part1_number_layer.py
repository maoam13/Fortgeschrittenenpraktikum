import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import matplotlib.pyplot as plt
import csv
import peaks_func as pf


G_intensity = []
for i in range(1, 7):
    name = '2 mono bi tri flake/' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')
    G, D = pf.peaks(name)
    start = G[0] - G[2]/2
    stop = G[0] + G[2]/2
    start_idx = pf.near(data[:,0], start)
    stop_idx = pf.near(data[:,0], stop)
    _G_intensity = np.max(data[:,1][start_idx:stop_idx])
    G_intensity.append(_G_intensity)

print(G_intensity)

