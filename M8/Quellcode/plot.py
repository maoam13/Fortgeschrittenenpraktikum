# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:43:28 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt

mu = [5.09,0.21,4.27,7.62,0.07,0.57,0.72,0.04,0.08,3.0,0.04,0.04,0.13,2.77,0.85,0.09,2.65,1.79]
l = [50,50,50,75,75,75,100,100,100,150,150,150,150,200,200,200,200,200]

plt.scatter(l,mu)