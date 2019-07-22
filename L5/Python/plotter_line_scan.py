import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import matplotlib.pyplot as plt
import csv
import peaks_func as pf


name = '3 mono with wrinkle/mono 1.txt'
data = np.genfromtxt('../Daten/' + name, delimiter = '')
G, D = pf.peaks(name)
print(G)
print(D)
print(pf.Intensity_G(name))


font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

#############################Plotting Spectra Sololy###############################################
for i in range(1, 8):
    name = '3 mono with wrinkle/line scan across wrinkle top to bottom ' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')

    fig = plt.figure()
    plt.rc('font', **font)
    plt.plot(data[:,0], data[:,1])
    plt.xlabel('Raman shift [cm$^{-1}$]', **font)
    plt.ylabel('Intensity [a.u.]', **font)
    #plt.title('Snap-In Curve')
    plt.grid()
    plt.tight_layout()
    #plt.savefig('test.png')
    #plt.savefig('../Protokoll/Bilder/Exfoliation/' + name.split('/')[0] + '_' + name.split('/')[1].split('.')[0] + '.png')
    plt.savefig('../Protokoll/Bilder/Wrinkle/line_scan/' + str(i) + '.png')
    plt.close(fig)


for i in range(1, 4):
    name = '3 mono with wrinkle/mono ' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')

    fig = plt.figure()
    plt.rc('font', **font)
    plt.plot(data[:,0], data[:,1])
    plt.xlabel('Raman shift [cm$^{-1}$]', **font)
    plt.ylabel('Intensity [a.u.]', **font)
    #plt.title('Snap-In Curve')
    plt.grid()
    plt.tight_layout()
    #plt.savefig('test.png')
    #plt.savefig('../Protokoll/Bilder/Exfoliation/' + name.split('/')[0] + '_' + name.split('/')[1].split('.')[0] + '.png')
    plt.savefig('../Protokoll/Bilder/Wrinkle/single_spectra/' + str(i) + '.png')
    plt.close(fig)


#############################Plotting Spectra Together###############################################
fig = plt.figure()
plt.rc('font', **font)
for i in range(1, 8):
    name = '3 mono with wrinkle/line scan across wrinkle top to bottom ' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')
    plt.plot(data[:,0], data[:,1], label = str(i)) #labels[i-1])
plt.xlabel('Raman shift [cm$^{-1}$]', **font)
plt.ylabel('Intensity [a.u.]', **font)
plt.legend()
#plt.title('Snap-In Curve')
plt.grid()
plt.tight_layout()
#plt.savefig('test.png')
plt.savefig('../Protokoll/Bilder/Wrinkle/line_scan/line_scan_all.png')
plt.xlim(1550, 1640)
plt.savefig('../Protokoll/Bilder/Wrinkle/line_scan/line_scan_G_peak.png')
plt.xlim(2620, 2750)
plt.savefig('../Protokoll/Bilder/Wrinkle/line_scan/line_scan_2D_peak.png')
plt.close(fig)


fig = plt.figure()
plt.rc('font', **font)
for i in range(1, 4):
    name = '3 mono with wrinkle/mono ' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')
    plt.plot(data[:,0], data[:,1], label = str(i)) #labels[i-1])
plt.xlabel('Raman shift [cm$^{-1}$]', **font)
plt.ylabel('Intensity [a.u.]', **font)
plt.legend()
#plt.title('Snap-In Curve')
plt.grid()
plt.tight_layout()
#plt.savefig('test.png')
plt.savefig('../Protokoll/Bilder/Wrinkle/single_spectra/single_spectra_all.png')
plt.xlim(1550, 1640)
plt.savefig('../Protokoll/Bilder/Wrinkle/single_spectra/single_spectra_G_peak.png')
plt.xlim(2620, 2750)
plt.savefig('../Protokoll/Bilder/Wrinkle/single_spectra/single_spectra_2D_peak.png')
plt.close(fig)
