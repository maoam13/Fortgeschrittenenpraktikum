# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:12:06 2018

@author: morit
"""
import numpy as np
import matplotlib.pyplot as plt

#x = np.array([2,6]) #1
#y = np.array([4,4])

#x = np.array([5,15]) #2
#y = np.array([10,10])

x = np.array([13,4]) #3
y = np.array([9,9])

x = np.array([7,7]) #1
y = np.array([11,4])

x = np.array([7,7]) #1
y = np.array([11,4])

x = np.array([7,7]) #1
y = np.array([10,3])






a = 2.46
winkel = np.array([60,120])
f = np.sqrt((a*x)**2+(a*y)**2-2*a**2*x*y*np.cos(2.*np.pi*winkel/360))
print f


