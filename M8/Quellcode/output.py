# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:39:28 2019

@author: morit
"""
import numpy as np
data = np.genfromtxt("../Daten/output_4c3.csv",delimiter = ';')
import matplotlib.pyplot as plt

for i in range(1,6):
    y = data[:,4*i-2]
    x = data[:,4*i-1]
    U = data[:,4*i-3]
    print U
    
    plt.figure('output')
    plt.plot(x,y,label="$U_g = $"+str(U[0])+" V" )
    plt.ylabel("$I_d[A]$")
    plt.xlabel("$U_d[V]$")
    plt.legend()
    plt.axis([0,x[-1],0,max(y)*1.1])