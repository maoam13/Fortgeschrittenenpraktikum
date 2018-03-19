# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:10:45 2018

@author: morit
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import Kalibration_Methode as kal

class Spektrum:
    x = "NULL"
    
    def __init__(self,name):
        self.x = np.array(einlesen(name))

def einlesen(name):
    return np.genfromtxt("../Daten/GR2830/"+name, delimiter = ' ', skip_header = 1, skip_footer = 1)

def gauss(a,x):
    return a[2]+a[3]/np.sqrt(2*np.pi*a[1]**2)*np.exp(-(x-a[0])**2/(2*a[1]**2))


#def main():
ein = Spektrum("einlinien 1h1min.ws5")
hyper = Spektrum("Hyperfein messung 18h.ws5")
quad = Spektrum("Quadrupol 1h45min.ws5")
extleer = Spektrum("Extinsion leer.ws5")
extrausch= Spektrum("Extinsion Rauschmessung.ws5")
exteisen = Spektrum("Extinsion Eisen.ws5")
extsulfat = Spektrum("Extinsion Eisensulfat.ws5")
extstahl = Spektrum("Extinsion Stahl.ws5")
quell = Spektrum("Quellspektrum v0_echt.ws5")
#plt.figure(1)
#plt.plot(quell.x)
i = 4
E = kal.Kalibration(i)[0]-14.4*10**12
dE = kal.Kalibration(i)[1]
v = kal.Kalibration(i)[2]
dv = kal.Kalibration(i)[3]
print max(v),dv[np.argmax(v)]
print max(E),dE[np.argmax(E)]

print "$",np.round(max(v),3),"\pm",np.round(dv[np.argmax(v)],3),"$ & $",np.round(max(E),1),"\pm",np.round(dE[np.argmax(E)],1),"$\\\\"



#if  __name__ =='__main__':
#    main()