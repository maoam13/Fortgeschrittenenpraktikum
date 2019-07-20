import Praktikum as p
import os
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import peaks_func as pf


G_step, sig_G_step, D_step, sig_D_step = [], [], [], []
for i in range(1, 7):
    name = '2 mono bi tri flake/' + str(i) + '.txt'
    __G, __D = pf.peaks(name)
    G_step.append(__G[0])
    D_step.append(__D[0])
    sig_G_step.append(__G[1])
    sig_D_step.append(__D[1])


G_wrinkle, sig_G_wrinkle, D_wrinkle, sig_D_wrinkle = [], [], [], []
for i in range(1, 4):
    name = '3 mono with wrinkle/mono ' + str(i) + '.txt'
    __G, __D = pf.peaks(name)
    G_wrinkle.append(__G[0])
    D_wrinkle.append(__D[0])
    sig_G_wrinkle.append(__G[1])
    sig_D_wrinkle.append(__D[1])


G_PMMA, sig_G_PMMA, D_PMMA, sig_D_PMMA = [], [], [], []
for i in range(1, 6):
    name = '4 Half sandwich on PMMA/Half ' + str(i) + '.txt'
    __G, __D = pf.peaks(name)
    G_PMMA.append(__G[0])
    D_PMMA.append(__D[0])
    sig_G_PMMA.append(__G[1])
    sig_D_PMMA.append(__D[1])


data = np.genfromtxt("../Daten/5 full sandwich on sio2/Green laser/Omega2DvsOmegaG.csv", delimiter = '',skip_header = 1)
G_SiO = data[:,0]
D_SiO = data[:,1]


font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}


fig = plt.figure()
plt.rc('font', **font)
plt.errorbar(G_step, D_step, fmt = '.', color = 'r', label = 'stair flake')
plt.errorbar(G_wrinkle, D_wrinkle, fmt = '.', color = 'g', label = 'mono flake')
plt.errorbar(G_PMMA, D_PMMA, fmt = '.', color = 'y', label = 'half sandwich on PMMA')
plt.errorbar(G_SiO, D_SiO, fmt = '.', color = 'b', label = 'Gr on SiO$_2$')
plt.xlabel('$\omega _G$ [cm$^{-1}$]', **font)
plt.ylabel('$\omega _{2D}$ [cm$^{-1}$]', **font)
plt.legend()
plt.grid()
plt.tight_layout()
#plt.savefig('test.png')
plt.savefig('../Protokoll/Bilder/Part_3/omega_2D_vs_G.png')
plt.close(fig)
