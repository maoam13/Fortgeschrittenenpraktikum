# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:55:42 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv

N1 = 10603.#1mus
N2 = 8284.#2ms

if 0:
    N1 = 1788.
    N2 = 1381.

if 0:
    N1 = 1836.
    N2 = 1392.
    
if 0:
    N1 = 1788.
    N2 = 1381.

T2 = 0.001908 #1.908ms

t = 1./N1 - 1./N2 + T2

print t,N1,N2
