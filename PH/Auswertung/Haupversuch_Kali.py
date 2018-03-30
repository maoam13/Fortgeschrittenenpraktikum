# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:29:28 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    datei = ["Abkuhlung_supraX1_kalibriert"]
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Haupversuch/Abkuhlung_supraX1.dat", delimiter = '\t',dtype = np.float)
        

plt.close("all")
index = 0
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]