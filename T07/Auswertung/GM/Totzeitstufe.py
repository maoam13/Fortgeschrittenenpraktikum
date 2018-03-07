# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:55:42 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv


T = 60.
N1 = 10603.#1mus
N2 = 8284.#2ms

if 0:
    T =10
    N1 = 1788.
    N2 = 1381.

if 1:
    N1 = 10689.
    N2 = 8257.
    
if 0:
    N1 = 10546.
    N2 = 8307.
    
if 0:
    N1 = 5359.
    N2 = 4599.

m1 = N1/T
m2 = N2/T
sm1 = np.sqrt(N1)/T
sm2 = np.sqrt(N2)/T

print m1, sm1 
print m2, sm2
print N1 ,np.sqrt(N1)
print N2 ,np.sqrt(N2)

T2 = 0.001908 #1.908ms

t = 1./m1 - 1./m2 + T2

sigt = np.sqrt((sm1/m1**2)**2 + (sm2/m2**2)**2)

print t,sigt

print p.gew_mittelwert(np.array([520,450]),np.array([50,30]))

print p.gew_mittelwert(np.array([324,255,375]),np.array([97,97,97]))

print sigt/t