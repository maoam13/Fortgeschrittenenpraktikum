# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:01:58 2018

@author: Moritz
"""

import Praktikummo2 as p
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
    return a[0]*(x-a[1])**2+a[2]
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
xerr = np.full(len(x),np.std(x[:20])/np.sqrt(10))
yerr = np.full(len(y),np.std(y[:20])*np.sqrt(2))

index = 2
data = Einlesen(index).data
leerx = data[:,0]
leery = data[:,1]
err = np.full(len(leerx),0.0001)
anfang = find_nearest(x,99.12)-7
ende = find_nearest(x,99.12)+7
yoff = diff(x,y,leerx,leery)
sol = p.fitte_bel_function_xy(x[anfang:ende],yoff[anfang:ende],xerr[anfang:ende],yerr[anfang:ende],func,[-1,99,0])

plt.figure("Untergrund")
ax = plt.subplot(111)
plt.plot(leerx,leery)
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/Untergrund")
 
plt.figure("X2roh")
ax = plt.subplot(111)
plt.plot(x,y,label = "Rohdaten")
plt.plot(x,yoff,label = "ohne Untergrund")
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.title("X''-Rohdaten")
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X2roh")

plt.figure("X2")
ax = plt.subplot(211)
plt.axis([x[anfang-30],x[ende+30],-0.3,0.1])
plt.errorbar(x,yoff,xerr = xerr,yerr = yerr,fmt=".")
plt.plot(x[anfang:ende], func(sol[0],x[anfang:ende]), color = 'r')
plt.axis([x[anfang-30],x[ende+30],plt.ylim()[0],plt.ylim()[1]])
ax.set_ylabel("Amplitude[V]")
plt.grid()
plt.setp(ax.get_xticklabels(), visible=False)
ax2 = plt.subplot(212,sharex = ax)
ax2.set_ylabel("Residuen[V]")
ax2.set_xlabel("Temperatur[K]")
plt.figtext(0.2,0.75,
                'Modell: y = a * (x-b)^2 + c\n'
                +'a= '+str(np.round(sol[0][0],3))+' +/- '+str(np.round(sol[1][0],3))+'\n'
                +'b= '+str(np.round(sol[0][1],2))+' +/- '+str(np.round(sol[1][1]*2,2))+'\n'
                +'c= '+str(np.round(sol[0][2],3))+' +/- '+str(np.round(sol[1][2],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(sol[2], 2)))
#plt.axis([x[apos-b-10],x[apos+b+10],-0.04,0.04])
plt.grid()
plt.errorbar(x[anfang:ende],yoff[anfang:ende]-func(sol[0],x[anfang:ende]),np.sqrt(yerr[anfang:ende]**2+(xerr[anfang:ende]*2*sol[0][0])**2),fmt = '.')
plt.axis([x[anfang-30],x[ende+30],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x, np.zeros(len(x)), color='r')
plt.tight_layout()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X2_anpassung")