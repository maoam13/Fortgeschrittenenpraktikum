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
plateau = 20
plateauend = 40
xplateau = x[plateau:plateauend]
yplateau = y[plateau:plateauend]

sy = np.sqrt(x)
slogy = 1./y * sy

if 1:#plot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,yplateau,sy[plateau:plateauend])
    plt.figure(2)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("n")
    ax.grid(linestyle='--')
    ax.axis([250,2000,0,7000])
    plt.plot(x,y)
    #plt.plot(x[plateau-5:plateauend+2],a*x[plateau-5:plateauend+2]+b)
    

if 1:#logplot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:plateauend])
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("log(n)")
    ax.axis([250,2000,1,9])
    ax.grid(linestyle='--')
    plt.plot(x,logy)
    plt.plot(x[plateau-5:plateauend+2],a*x[plateau-5:plateauend+2]+b)