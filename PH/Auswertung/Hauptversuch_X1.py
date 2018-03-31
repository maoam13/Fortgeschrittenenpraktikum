# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:01:58 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        datei = ["Abkuhlung_supraX1_kalibriert","Phasenkalibration",]
        self.data = np.genfromtxt("../Daten/Hauptversuch/"+datei[index]+".dat", delimiter = '\t',dtype = np.float)
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

plt.close("all")
index = 1
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]