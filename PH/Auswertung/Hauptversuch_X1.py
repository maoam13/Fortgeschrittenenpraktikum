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
        datei = ["SupraX2","SupraX1_kalibriert","LeermessungX2"]
        self.data = np.genfromtxt("../Daten/Hauptversuch/"+datei[index]+".dat", delimiter = '\t',dtype = np.float)
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx


def diff(x,y,leerx,leery):
    y1 = np.copy(y)
    for i in range(len(x)):
        idx = find_nearest(leerx,x[i])
        y1[i] += leery[idx]
    return y1

def find_max(x,y,xerr,yerr):
    x = np.array(x)
    y = np.array(y)
    xerr = np.array(xerr)
    yerr = np.array(yerr)
    res = []
    b = 10
    i = b
    a = 0
    apos = 0
    while i+b < len(x):
        ai = p.lineare_regression_xy(x[i-b:i+b],y[i-b:i+b],xerr[i-b:i+b],yerr[i-b:i+b])
        if ai[0] < a:
            a = ai[0]
            apos = i
        res.append(ai)
        i +=1
    return apos, a,res,b
            
def func(A,x):
    #return A[0]*np.arctan(A[1]*x-A[2])+A[3]+A[4]*1./(x-A[5])
    return A[0]*np.exp(A[1]/(x-A[2]))+A[3]+A[4]*1./(x-A[5])

def xrate(x):
    rate = []
    for i in range(len(x)-4):
        rate.append(x[i+4]-x[i])
    return rate

def constante(x,y):
    start1 = find_nearest(x,82)
    ende1 = find_nearest(x,90)
    start2 = find_nearest(x,110)
    ende2 = find_nearest(x,120)
    U1 = np.mean(y[start1:ende1])
    dU1 = np.std(y[start1:ende1])
    U2 = np.max(y[start2:ende2])
    dU2 = np.std(y[start2:ende2])
    Uint = U1-U2
    Vsupra = 14.7*10**-9
    dVsupra = 0.1/np.sqrt(12)*10**-9
    v = 10./(0.5*10**-3)
    C =  Uint/v/Vsupra
    dC = np.sqrt((dU1/v/Vsupra)**2+(dU2/v/Vsupra)**2+(Uint/v/Vsupra**2*dVsupra)**2)
    print C,dC
    
    
    

plt.close("all")
index = 1
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]#*-1
xerr = np.full(len(x),np.std(x[:20])/np.sqrt(10))
yerr = np.full(len(y),np.std(y[:20])*np.sqrt(2))
index = 2
data = Einlesen(index).data
leerx = data[:,0]
leery = data[:,1]#*-1
err = np.full(len(leerx),0.0001)
yoff = diff(x,y,leerx,leery)
apos,a,res,b = find_max(x,yoff,xerr,yerr)
print x[apos],a
constante(x,yoff)


plt.figure("X1roh")
ax = plt.subplot(111)
plt.plot(x,y,label = "Rohdaten")
plt.plot(x,yoff,label = "ohne Untergrund")
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.title("X'-Rohdaten")
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1roh")

#sol = p.fitte_bel_function_xy(x,yoff,xerr,yerr,func,[-1,-1,100,1,1,100])
plt.figure("X1off")
ax = plt.subplot(111)
#plt.plot(leerx,leery)
#plt.errorbar(x,y,xerr = xerr,yerr = yerr,fmt = ".")
plt.plot(x,yoff)
plt.plot(x[apos-b:apos+b],res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2], color = 'g')
plt.plot(x[:-4],xrate(x))
#plt.plot(leerx,func(a,leerx))
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1")

plt.figure("X1spiegel")
ax = plt.subplot(111)
#plt.plot(leerx,leery)
#plt.plot(x,yoff)
#plt.errorbar(x,y,xerr = xerr,yerr = yerr,fmt = ".")
plt.plot(x,(yoff-yoff[-1])*-1)
#plt.plot(leerx,func(a,leerx))
#plt.axis([90,110,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1_spiegel")