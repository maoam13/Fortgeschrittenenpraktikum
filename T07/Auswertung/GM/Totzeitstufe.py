# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:55:42 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv

N1 = 10603.#1mus
N2 = 8284.#2ms

if 0:
    N1 = 1788.
    N2 = 1381.

if 0:
    N1 = 1836.
    N2 = 600.
    
if 0:
    N1 = 5359.
    N2 = 4599.

T2 = 0.001908 #1.908ms

t = 1./N1 - 1./N2 + T2

sigt = np.sqrt((np.sqrt(N1)/N1**2)**2 + (np.sqrt(N2)/N2**2)**2)

print t,sigt,N1,N2

print p.gew_mittelwert(np.array([520,450]),np.array([50,30]))

print p.gew_mittelwert(np.array([1877,1882]),np.array([4,2]))