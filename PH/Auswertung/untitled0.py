# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:08:49 2018

@author: morit
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s


Nprim = 2046
Nsek = 700
lprim = 50*10**-3
lsek = 20*10**-3
mu = s.mu_0
I0 = 10**-3
Vprobe = 22.9*10**-9
Vsupra = 14.7*10**-9
f = 0.380*10**3
Xi = 5
C =  2*np.pi*f*mu*I0*Nsek*Nprim/lsek/lprim
s =  C*Xi*Vprobe
print C

v = 10./(0.5*10**-3)
Uint = (-0.76+3.22)
#Uint = 0.76+0.3

Cexp = Uint/v/Vsupra

print Cexp
