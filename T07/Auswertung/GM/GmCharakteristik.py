# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:40:29 2018

@author: Moritz
"""
import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr


file = open("..\..\Daten\GMcharakteristik.csv")
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

file = open("..\..\Daten\GMpoisson.csv")
csv_reader = csv.reader(file, delimiter=";")
test = []
for row in csv_reader:
    
    wert = row[0]
    wert = float(wert)
    test.append(wert)
file.close()

offset = np.mean(test)

"""Variablen"""
x = np.array(x)
y = np.array(y)

#Totzeitkorrektur
ydot =y/10
y = y/(1.-ydot*0.0018)
y = y-1

logy = np.log(y)
plateau = 27
xplateau = x[plateau:]
yplateau = y[plateau:]
UE = 316
UG = 350


sy = np.sqrt(x)
slogy = 1./y * sy

def f(a,x):
    return a[0]+a[1]*x+a[2]*x**2+a[3]*x**3+a[4]*x**4+a[5]*x**5

#var,svar,chi = p.fitte_bel_function(x[11:34],logy[11:34],slogy[11:34],f,[8,-100,10000,300,1,1,1])

if 1:#logplot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:])
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("log(n)")
    ax.axis([300,650,1,8])
    ax.grid(linestyle='--')
    plt.plot(x,logy)
    plt.plot(x,a*x+b)
   # plt.plot(x[11:34],f(var,x[11:34]))
    plt.vlines(UE,0,8,linestyle='--',color = 'g')
    plt.vlines(UG,0,8,linestyle='--',color = 'r')
    
if 1:#plot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,yplateau,sy[plateau:])
    plt.figure(2)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("n")
    ax.grid(linestyle='--')
    ax.axis([250,650,0,1300])
    plt.plot(x,y)
    plt.plot(x,a*x+b)
    plt.vlines(UE,0,1300,linestyle='--',color = 'g')
    plt.vlines(UG,0,1300,linestyle='--',color = 'r')
    