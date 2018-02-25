# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:59:10 2018

@author: Moritz
"""

import Praktikum as p
import numpy as np
x = np.array([30.7,28.6,27.3,29.5])
y = np.array([28.3,27.7,27.5,27.9])
dx = np.array([1.1,1.0 ,0.8 , 1.3])
dy = np.array([1.1,1.3 ,1.0 , 1.9])
print p.gew_mittelwert(x,dy)