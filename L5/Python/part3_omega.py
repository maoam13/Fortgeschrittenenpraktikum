import Praktikum as p
import part3_strain_doping as sd
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

strain_step, doping_step = [], []
for i in range(len(G_step)):
    _doping, _strain = sd.doping_strain_official(G_step[i], D_step[i])
    strain_step.append(_strain)
    doping_step.append(_doping)

print('step flake:')
print('strain [%], doping [10^12 cm^-3]')
sd.print_table([strain_step, doping_step], transpose=True)


G_wrinkle, sig_G_wrinkle, D_wrinkle, sig_D_wrinkle = [], [], [], []
for i in range(1, 4):
    name = '3 mono with wrinkle/mono ' + str(i) + '.txt'
    __G, __D = pf.peaks(name)
    G_wrinkle.append(__G[0])
    D_wrinkle.append(__D[0])
    sig_G_wrinkle.append(__G[1])
    sig_D_wrinkle.append(__D[1])

strain_wrinkle, doping_wrinkle = [], []
for i in range(len(G_wrinkle)):
    _doping, _strain = sd.doping_strain_official(G_wrinkle[i], D_wrinkle[i])
    strain_wrinkle.append(_strain)
    doping_wrinkle.append(_doping)

print('flake with wrinkle:')
print('strain [%], doping [10^12 cm^-3]')
sd.print_table([strain_wrinkle, doping_wrinkle], transpose=True)


G_PMMA, sig_G_PMMA, D_PMMA, sig_D_PMMA = [], [], [], []
for i in range(1, 6):
    name = '4 Half sandwich on PMMA/Half ' + str(i) + '.txt'
    __G, __D = pf.peaks(name)
    G_PMMA.append(__G[0])
    D_PMMA.append(__D[0])
    sig_G_PMMA.append(__G[1])
    sig_D_PMMA.append(__D[1])

strain_PMMA, doping_PMMA = [], []
for i in range(len(G_PMMA)):
    _doping, _strain = sd.doping_strain_official(G_PMMA[i], D_PMMA[i])
    strain_PMMA.append(_strain)
    doping_PMMA.append(_doping)

print('flake on PMMA:')
print('strain [%], doping [10^12 cm^-3]')
sd.print_table([strain_PMMA, doping_PMMA], transpose=True)


data = np.genfromtxt("../Daten/5 full sandwich on sio2/Green laser/Omega2DvsOmegaG.csv", delimiter = '',skip_header = 1)
G_SiO = data[:,0]
D_SiO = data[:,1]

strain_SiO, doping_SiO = [], []
for i in range(len(G_SiO)):
    _doping, _strain = sd.doping_strain_official(G_SiO[i], D_SiO[i])
    strain_SiO.append(_strain)
    doping_SiO.append(_doping)

#print('flake on SiO:')
#print('strain [%], doping [10^12 cm^-3]')
#sd.print_table([strain_SiO, doping_SiO], transpose=True)
print(np.mean(strain_SiO))
print(np.mean(doping_SiO))

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
