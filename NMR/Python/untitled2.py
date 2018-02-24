# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:59:10 2018

@author: Moritz
"""

import Praktikum as p
import numpy as np
x = np.array([28.1,27.4,27.3,27.7])
dx = np.array([1.1,1.0 ,0.8 , 1.3])

print p.gew_mittelwert(x,dx)