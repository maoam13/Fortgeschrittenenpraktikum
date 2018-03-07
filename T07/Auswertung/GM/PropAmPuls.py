# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:10:42 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr

file = open("..\..\Daten\PropAM.csv")
csv_reader = csv.reader(file, delimiter=";")
x = []
y = []
for row in csv_reader:
    wert = row[2]
    wert = float(wert)
    y.append(wert)
    
    wert = row[0]
    wert = float(wert)
    x.append(wert)
file.close()

"""Variablen"""
x = np.array(x)
y = np.array(y)
logy = np.log(y)
sy = 0.1*y
slogy = 1./y * sy
plateau = 43
plateauend = 60
xplateau = x[plateau:plateauend]
yplateau = y[plateau:plateauend]
logyplateau = logy[plateau:plateauend]

a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:plateauend])
if 1:
    plt.figure(3)
    ax1=plt.subplot(211)
    ax1.axis([300,1300,1,10])
    ax1.set_ylabel("gemmessener Puls log(U)[log(mV)]")
    plt.figtext(0.5,0.6,'Modell: y = a*x+b'+
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
    ax.set_xlabel("U [V]")
    ax.set_ylabel("n")
    ax.grid(linestyle='--')
    ax.axis([250,2000,0,7000])
    plt.plot(x,y)
    #plt.plot(x,a*x+b)
    

if 1:#logplot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:plateauend])
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("log(U)")
    ax.axis([250,2000,4,9])
    ax.grid(linestyle='--')
    plt.plot(x,logy)
    plt.plot(x,a*x+b)