import numpy as np
import Praktikum as p
import auswertung_nur_Methoden as AM
import matplotlib.pyplot as plt
import csv

name = '2 mono bi tri flake/3.txt'
data = np.genfromtxt('../Daten/' + name, delimiter = '')

#print(np.shape(data))


font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

fig = plt.figure()
plt.rc('font', **font)
plt.plot(data[:,0], data[:,1])
plt.xlabel('Raman shift [cm$^{-1}$]', **font)
plt.ylabel('Intensity [a.u.]', **font)
#plt.title('Snap-In Curve')
plt.grid()
plt.tight_layout()
#plt.savefig('test.png')
plt.savefig('../Protokoll/Bilder/Exfoliation/' + name.split('/')[0] + '_' + name.split('/')[1].split('.')[0] + '.png')
plt.close(fig)

