# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 01:05:15 2018

@author: morit
"""


import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr

file = open("..\Daten\Propleer.csv")
csv_reader = csv.reader(file, delimiter=";")
x = []
y = []
offset = []
for row in csv_reader:
    wert = row[1]
    wert = float(wert)
    y.append(wert)
    
    wert = row[0]
    wert = float(wert)
    x.append(wert)
file.close()

x = np.array(x)
y = np.array(y)

if 1:#plot
    plt.figure(2)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("n")
    ax.grid(linestyle='--')
    ax.axis([250,2000,0,30])
    plt.plot(x,y)
    
if 1:#plot
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("log(n)")
    ax.grid(linestyle='--')
    ax.axis([250,2000,0,30])
    plt.plot(x,np.log(y))