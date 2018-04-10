# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:22:23 2018

@author: Gerald
"""

import Praktikum as p
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import timeit

start_time=timeit.default_timer()

speichern = 0

data = np.genfromtxt("../../Daten/Vorversuch 2/lockin Hochpass.csv", delimiter = ';', skip_header = 1)
def kenn(A, x):#A = [f_G, Amplitude, Nullphase]
    return A[1]*(x/A[0])/np.sqrt(1 + (x/A[0])**A[4]) * np.sin(np.arctan((x-A[3])*A[2]))
f, A, B = AM.sortieren([data[:,0], data[:,1], data[:,2]], 0)
sA = 0.01/np.sqrt(12)
sB = 0.001/np.sqrt(12)
sf = f*0.02

sol = AM.fitte_bel_function(f, A, sf, sA, kenn, [1000, 2., 0.0001,1000,2,1])
xwerte = np.arange(f[0],f[-1])
#Plotte Tiefpass Kennlinie
plt.close('all')
plt.figure(1)
ax1 = plt.subplot(211)
ax1.set_xscale("log", nonposx = 'clip')
#ax1.set_yscale("log", nonposy = 'clip')
plt.plot(xwerte,( kenn(sol[0], xwerte)), color = 'g')
#plt.plot(xwerte, kenn2O(sol2O[0], xwerte), color = 'r')
plt.errorbar(f, A, xerr = sf, yerr = sA, fmt = '.', color = 'b', label = 'Messung mit Multimeter')
#plt.errorbar(f, B, xerr = sf, yerr = sB, fmt = '.', color = 'y', label = 'Messung mit Oszilloskop')
plt.title('Kennlinie Lockin Hochpass')
plt.ylabel('$U_a$ [V]')
plt.grid()
plt.setp(ax1.get_xticklabels(), visible=False)
ax2 = plt.subplot(212,sharex = ax1)
ax2.set_xlabel("Frequenz[Hz]")
ax2.set_ylabel("Residuen[V]")
ax2.set_xscale("log", nonposx = 'clip')
plt.errorbar(f,A-kenn(sol[0],f),sA*2,fmt = ".")
plt.plot(f, np.zeros(len(f)), color='r')
plt.tight_layout()
plt.figtext(0.65,0.58,
                'a= '+str(np.round(sol[0][0],1))+' +/- '+str(np.round(sol[1][0],1))+'\n'
                +'b= '+str(np.round(sol[0][1],2))+' +/- '+str(np.round(sol[1][1],2))+'\n'
                +'c= '+str(np.round(sol[0][2],4))+' +/- '+str(np.round(sol[1][2],4))+'\n'
                +'d= '+str(np.round(sol[0][3],1))+' +/- '+str(np.round(sol[1][3],1))+'\n'
                +'e= '+str(np.round(sol[0][4],2))+' +/- '+str(np.round(sol[1][4],2))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(sol[2], 2)))
plt.grid()

if speichern == 1:
    plt.savefig("../../Protokoll/Bilder/Vorversuch2/KennlinieHochpass")

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))