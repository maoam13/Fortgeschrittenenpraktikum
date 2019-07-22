import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import matplotlib.pyplot as plt
import csv

font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

labels = ['2', '4', '5', '3', '6', '1']

for i in range(1, 7):
    name = '2 mono bi tri flake/' + str(i) + '.txt'
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
    plt.savefig('../Protokoll/Bilder/Exfoliation/' + name.replace(' ', '_').split('/')[0] + '_' + labels[i-1] + '.png')
    plt.close(fig)

fig = plt.figure()
plt.rc('font', **font)
for i in range(1, 7):
    name = '2 mono bi tri flake/' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')
    plt.plot(data[:,0], data[:,1], label = str(i)) #labels[i-1])
plt.xlabel('Raman shift [cm$^{-1}$]', **font)
plt.ylabel('Intensity [a.u.]', **font)
plt.legend()
#plt.title('Snap-In Curve')
plt.grid()
plt.tight_layout()
#plt.savefig('test.png')
plt.savefig('../Protokoll/Bilder/Exfoliation/' + name.replace(' ', '_').split('/')[0] + '_all.png')
plt.close(fig)

fig = plt.figure()
plt.rc('font', **font)
plt.xlim(2600, 2800)
plt.ylim(800, 1200)
for i in range(1, 7):
    name = '2 mono bi tri flake/' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')
    plt.plot(data[:,0], data[:,1], label = str(i)) # labels[i-1])
plt.xlabel('Raman shift [cm$^{-1}$]', **font)
plt.ylabel('Intensity [a.u.]', **font)
plt.legend()
#plt.title('Snap-In Curve')
plt.grid()
plt.tight_layout()
#plt.savefig('test.png')
plt.savefig('../Protokoll/Bilder/Exfoliation/' + name.replace(' ', '_').split('/')[0] + '_2D_peaks.png')
plt.close(fig)

fig = plt.figure()
plt.rc('font', **font)
plt.xlim(1540, 1650)
plt.ylim(800, 2000)
for i in range(1, 7):
    name = '2 mono bi tri flake/' + str(i) + '.txt'
    data = np.genfromtxt('../Daten/' + name, delimiter = '')
    plt.plot(data[:,0], data[:,1], label = str(i)) # labels[i-1])
plt.xlabel('Raman shift [cm$^{-1}$]', **font)
plt.ylabel('Intensity [a.u.]', **font)
plt.legend()
#plt.title('Snap-In Curve')
plt.grid()
plt.tight_layout()
#plt.savefig('test.png')
plt.savefig('../Protokoll/Bilder/Exfoliation/' + name.replace(' ', '_').split('/')[0] + '_G_peaks.png')
plt.close(fig)
    

