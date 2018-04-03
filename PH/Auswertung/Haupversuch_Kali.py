# -*- coding: utf-8 -*-

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        datei = ["Abkuhlung_supraX1_kalibriert","Phasenkalibration",]
        self.data = np.genfromtxt("../Daten/Hauptversuch/"+datei[index]+".dat", delimiter = '\t',dtype = np.float)
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

plt.close("all")
index = 1
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]
xall = np.copy(x)
yall = np.copy(y)

cut = find_nearest(x,116)
x1 = x[:cut]
y1 = y[:cut]
x = x[cut:]
y = y[cut:]

cut = find_nearest(x,83.5)
x2 = x[:cut]
y2 = y[:cut]
x = x[cut:]
y = y[cut:]
cut = find_nearest(x,116)
cut3 = find_nearest(x,95)
x3 = x[:cut]
y3 = y[:cut]
x4 = x[cut3:]
y4 = y[cut3:]

plt.figure("Kali3_0")
ax = plt.subplot(111)
plt.plot(xall,yall)
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
#plt.savefig("../Protokoll/Bilder/Hauptversuch/Kal_"+str(index))

plt.figure("Kali3_1")
ax = plt.subplot(111)
plt.plot(x1[30:],y1[30:])
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
ax.set_title("Aufwaermung 86"+u'\u00b0')
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/Kal_0")

plt.figure("Kali3_2")
ax = plt.subplot(111)
plt.plot(x2[150:-20],y2[150:-20])
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
ax.set_title("Abkuelung 82"+u'\u00b0')
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/Kal_1")

plt.figure("Kali3_3")
ax = plt.subplot(111)
plt.plot(x3[150:-20],y3[150:-20])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
ax.set_title("Aufwaermung 90"+u'\u00b0')
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/Kal_2")

plt.figure("Kali3_4")
ax = plt.subplot(111)
plt.plot(x4,y4)
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
ax.set_title("Abkuelung 84.5"+u'\u00b0')
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/Kal_3")