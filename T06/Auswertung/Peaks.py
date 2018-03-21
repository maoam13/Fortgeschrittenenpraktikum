# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 00:40:25 2018

@author: Moritz
"""
import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s
import Kalibration_Methoden as met

class Einlesen:
    data = 0
    datei = ["Ba","Ag","Cu","Mo","Rb","Tb","leer"]
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Alpha/Kalibration "+self.datei[index]+"_15min.mca", delimiter = ',', skip_header = 12, skip_footer = 37)


def gauss(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))

def gauss2(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))

def gauss3(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))+a[9]*np.exp(-(x-a[7])**2/(2*a[8]**2))

