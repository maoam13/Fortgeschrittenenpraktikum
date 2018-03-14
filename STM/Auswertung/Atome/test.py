# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:29:06 2018

@author: morit
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr

a = [0.184,0.172]
sa = [0.012,0.005]
b = [0.414,-1.024]
sb = [0.039,0.05]

av = 0.184
an = 0.172
sav = 0.012
san = 0.005
bv = 0.414
bn = -1.024
sbv = 0.039
sbn = 0.05

da = av-an
db = bn-bv

schnitt = db/da
sschnitt = np.sqrt(1./da**2*(sbn**2+sbv**2+(sav*db/da)**2))#+(san*db/da)**2))
print schnitt,sschnitt

x = np.arange(0,100,0.1)

#plt.plot(x,av*x+bv)
plt.plot(x,2*x+4)
plt.plot(x,-1./2*x+60)
plt.axis([0,100,0,100])