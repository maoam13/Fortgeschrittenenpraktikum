# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:08:49 2018

@author: morit
"""

import Praktikummo as p
import Kalibration_Methoden as met
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

print 100/np.sqrt(2)
print 15./380
Nprim = 2046
Nsek = 700
lprim = 50*10**-3
lsek = 20*10**-3
mu = s.mu_0
I0 = 10**-3
Vprobe = 21*10**-9
f = 0.375*10**3
Xi = 5
print 2*np.pi*f*mu*I0*Nsek*Nprim/lsek/lprim *Xi*Vprobe