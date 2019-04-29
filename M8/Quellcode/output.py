# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:39:28 2019

@author: morit
"""
import numpy as np
data = np.genfromtxt("../Daten/output_4c3.csv",delimiter = ';')

for i in range(1,5):
    x = data[:,4*i-2]
    y = data[:,4*i-1]
    U = data[:,4*i-3]
    print U