# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:12:06 2018

@author: morit
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([7,4]) #1
y = np.array([3,3])

x = np.array([10,10]) #1
y = np.array([17,7])

x = np.array([15,7]) #1
y = np.array([10,10])







a = 2.46
winkel = np.array([60,120])
f = np.sqrt((a*x)**2+(a*y)**2-2*a**2*x*y*np.cos(2.*np.pi*winkel/360))
print f


