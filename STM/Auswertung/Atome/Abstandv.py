# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:12:06 2018

@author: morit
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([5,5]) #h1
y = np.array([9,4])

x = np.array([10,10]) #h2
y = np.array([17,7])

x = np.array([21,8]) #h3
y = np.array([13,13])

#x = np.array([3,3]) #s1
#y = np.array([5,2])

#x = np.array([8,8]) #s2
#y = np.array([14,6])

#x = np.array([15,8]) #s3
#y = np.array([23,15])







a = 2.46
winkel = np.array([60,120])
f = np.sqrt((a*x)**2+(a*y)**2-2*a**2*x*y*np.cos(2.*np.pi*winkel/360))
print f


