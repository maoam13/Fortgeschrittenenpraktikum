# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:24:33 2018

@author: morit
"""

import numpy as np
import matplotlib.pyplot as plt

l = [8.75,8.83,8.67,8.91,8.91,8.79]#h1
#l = [2.16,2.14,2.15,2.14,2.15,2.16]#h2
#l = [6.13,6.07,5.98,6.1,5.99,6.13]#s1
#l = [1.57,1.65,1.69,1.71,1.7,1.73]#s2
#l = [1.46,1.43,1.47,1.43,1.46,1.48]#s3

l = [8.68,8.53,8.41,8.53,8.57,8.57]#vh1
l = []#vh2
print np.mean(l)
print np.std(l)/np.sqrt(len(l)-1)