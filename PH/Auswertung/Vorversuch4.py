# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:13:31 2018

@author: Moritz
"""

import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Vorversuch 4/Integrationszeit.CSV", delimiter = ';', skip_header = 1)
        
plt.close("all")
index = 0
data = Einlesen(index).data
def func(a,x):
    return a[0]*1./(x-a[2])**2+a[3]
               
x = data[:,0]
y = data[:,1]/50
dy= np.full(len(y),0.1/np.sqrt(12))/50
sol = p.fitte_bel_function(x,y,dy,func,[1000,1,0,0.01])


plt.figure("Vor4_"+str(index))
ax = plt.subplot(111)
plt.errorbar(x,y,yerr = dy,fmt = ".")
plt.plot(x,func(sol[0],x))
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Frequenz[Hz]")
ax.set_ylabel("Amplitude[mV]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Vorversuch4/Vor4_"+str(index))

plt.figure("Vor4_"+str(index+1))
ax = plt.subplot(211)
plt.errorbar(x,y,yerr = dy,fmt = ".")
plt.plot(x,func(sol[0],x))
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_ylabel("Amplitude[mV]")
plt.setp(ax.get_xticklabels(), visible=False)
plt.grid()
ax2 = plt.subplot(212,sharex = ax)
ax2.set_xlabel("Frequenz[Hz]")
ax2.set_ylabel("Residuen[mV]")
plt.errorbar(x[1:],y[1:]-func(sol[0],x[1:]),dy[1:],fmt = ".")
plt.plot(x, np.zeros(len(x)), color='r')
plt.tight_layout()
plt.figtext(0.6,0.7,
                'Modell: y = a/(x-c)^2+d\n'
                +'a= '+str(np.round(sol[0][0],1))+' +/- '+str(np.round(sol[1][0],1))+'\n'
                #+'b= '+str(np.round(sol[0][1],2))+' +/- '+str(np.round(sol[1][1],2))+'\n'
                +'c= '+str(np.round(sol[0][2],3))+' +/- '+str(np.round(sol[1][2],3))+'\n'
                +'d= '+str(np.round(sol[0][3],4))+' +/- '+str(np.round(sol[1][3],4))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(sol[2], 2)))
plt.grid()
plt.savefig("../Protokoll/Bilder/Vorversuch4/Vor4_"+str(index+1))
