# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:27:05 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr

file = open("..\..\Daten\PropC.csv")
csv_reader = csv.reader(file, delimiter=";")
x = []
y = []
offset = []
for row in csv_reader:
    wert = row[2]
    wert = float(wert)
    y.append(wert)
    
    wert = row[0]
    wert = float(wert)
    x.append(wert)
    
    
    wert = row[3]
    wert = float(wert)
    offset.append(wert)
file.close()
"""Variablen"""
x = np.array(x)
y = np.array(y)
offset = np.array(offset)
logy = np.log(y)

sy = 0.1*y
slogy = 1./y * sy
plateau = 20
plateauend = 40
xplateau = x[plateau:plateauend]
yplateau = y[plateau:plateauend]
logyplateau = logy[plateau:plateauend]

a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:plateauend])

if 1:
    plt.figure(3)
    ax1=plt.subplot(211)
    ax1.axis([300,1300,1,10])
    ax1.set_ylabel("gemmessener Puls log(U)")
    plt.figtext(0.2,0.65,'Modell: y = a*x+b'+
                '\n a= '+str(np.round(a,6))+' +/- '+str(np.round(sa,6))+'\n'
                +' b= '+str(np.round(b,3))+' +/- '+str(np.round(sb,3))+' \n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi/len(xplateau), 2)))
    plt.errorbar(x[11:],logy[11:],yerr = slogy[11:],fmt='.')
    plt.plot(x,a*x+b,color = 'r')
    ax2=plt.subplot(212,sharex=ax1)
    ax2.set_xlabel("angelegte Spannung U[V}")
    ax2.set_ylabel("Residuen")
    plt.errorbar(xplateau,logyplateau-(a*xplateau+b),yerr = slogy[plateau:plateauend],fmt='.')
    x_r = np.array([250,2000])
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r')
    
if 1:#plot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,yplateau,sy[plateau:plateauend])
    plt.figure(2)
    ax = plt.subplot(111)
    ax.set_xlabel("Spannung U [V]")
    ax.set_ylabel("Pulshoehe U[mV]")
    ax.grid(linestyle='--')
    ax.axis([250,2000,0,7000])
    plt.plot(x,y)
    #plt.plot(x[plateau-5:plateauend+2],a*x[plateau-5:plateauend+2]+b)
    

if 1:#logplot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:plateauend])
    print chi/len(xplateau)
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_xlabel("Spannung U [V]")
    ax.set_ylabel("Pulshoehe log(U[mV])")
    ax.axis([250,2000,1,9])
    ax.grid(linestyle='--')
    plt.plot(x,logy)
    plt.plot(x[plateau-5:plateauend+2],a*x[plateau-5:plateauend+2]+b)