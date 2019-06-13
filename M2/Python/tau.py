# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 00:50:36 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt
import Praktikummo2 as p
from scipy.interpolate import interp1d
import scipy.constants as c
import scipy.optimize as opt

m = 0.057*c.m_e

print np.std([5.40,5.38,5.38,5.29,5.23,5.43])
print np.std([4.325,4.240,4.392,4.346,4.436,4.424])
print p.gew_mittelwert(np.array([2.4,2.51,2.63]),np.array([0.25,0.27,0.38]))
print np.mean([2.4,2.51,2.63])
x = 140.69
y = 141.07
a = (x+y)/2
print a
print np.sqrt((a/x * 0.46)**2 + (a/y * 0.47)**2)