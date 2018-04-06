# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:01:58 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        datei = ["SupraX2","SupraX2_kalibriert","LeermessungX2"]
        self.data = np.genfromtxt("../Daten/Hauptversuch/"+datei[index]+".dat", delimiter = '\t',dtype = np.float)
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

def diff(x,y,leerx,leery):
    y1 = np.copy(y)
    for i in range(len(x)):
        idx = find_nearest(leerx,x[i])
        y1[i] -= leery[idx]
    return y1
        
def func(a,x):
    return a[0]/(x-a[1])+a[2]
def xrate(x):
    rate = []
    for i in range(len(x)-5):
        rate.append(x[i+5]-x[i])
    return rate

plt.close("all")
index = 1
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]

index = 2
data = Einlesen(index).data
leerx = data[:,0]
leery = data[:,1]
err = np.full(len(leerx),0.0001)
sol = p.fitte_bel_function(leerx[100:],leery[100:],err[100:],func,[-1,70,0.1,-1])
yoff = diff(x,y,leerx,leery)

plt.figure("Untergrund")
ax = plt.subplot(111)
plt.plot(leerx,leery)
#plt.plot(leerx,func(sol[0],leerx))
#plt.plot(leerx,func(a,leerx))
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/Untergrund")
 
plt.figure("Vor3_"+str(index))
ax = plt.subplot(111)
plt.plot(leerx,leery)
plt.plot(x,yoff)
plt.plot(x,y)
plt.plot(x[:-5],xrate(x))
#plt.plot(leerx,func(a,leerx))
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()