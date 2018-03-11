# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 00:48:18 2018

@author: morit
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1000,1)
y = x/(1.-x*(0.000318))

ax = plt.subplot(111)
ax.set_xlabel("n")
ax.set_ylabel("N")
plt.plot(x,y)