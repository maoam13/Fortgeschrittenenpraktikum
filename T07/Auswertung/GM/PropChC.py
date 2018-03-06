# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:01:00 2018

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
for row in csv_reader:
    wert = row[1]
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
plateau = 33
plateauend = 43
xplateau = x[plateau:plateauend]
yplateau = y[plateau:plateauend]
logyplateau = logy[plateau:plateauend]

sy = np.sqrt(x)
slogy = 1./y * sy
a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:plateauend])
if 1:
    plt.figure(3)
    ax1=plt.subplot(211)
    ax1.axis([1100,2000,1,10])
    ax1.set_ylabel("U[V]")
    plt.figtext(0.6,0.65,'Modell: y = a*x+b'+
                '\n a= '+str(np.round(a,6))+' +/- '+str(np.round(sa,6))+'\n'
                +' b= '+str(np.round(b,3))+' +/- '+str(np.round(sb,3))+' \n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi/len(xplateau), 2)))
    plt.errorbar(x[23:],logy[23:],yerr = slogy[23:],fmt='.')
    plt.plot(x[23:],a*x[23:]+b,color = 'r')
    plt.vlines(x[plateau],1,10,linestyle='--',color = 'g')
    plt.vlines(x[plateauend-1],1,10,linestyle='--',color = 'g')
    #plt.vlines(1600,0,1300,linestyle='--',color = 'r')
    #plt.vlines(1910,0,1300,linestyle='--',color = 'r')
    ax2=plt.subplot(212,sharex=ax1)
    ax2.set_xlabel("t[s]")
    ax2.set_ylabel("Residuen")
    plt.errorbar(xplateau,logyplateau-(a*xplateau+b),yerr = slogy[plateau:plateauend],fmt='.')
    x_r = np.array([1100,2000])
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r')
    
if 1:#logplot
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("log(n)")
    ax.axis([250,2000,0,9])
    ax.grid(linestyle='--')
    plt.plot(x,logy)
    plt.plot(x[plateau-5:plateauend+2],a*x[plateau-5:plateauend+2]+b)
    plt.vlines(x[plateau],1,10,linestyle='--',color = 'g')
    plt.vlines(x[plateauend-1],1,10,linestyle='--',color = 'g')
    

if 1:#plot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,yplateau,sy[plateau:plateauend])
    plt.figure(2)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("n")
    ax.grid(linestyle='--')
    ax.axis([250,2000,0,8000])
    plt.plot(x,y)
    plt.plot(x[plateau-5:plateauend+2],a*x[plateau-5:plateauend+2]+b)
    

