# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:40:29 2018

@author: Moritz
"""
import Praktikum as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr


file = open("C:\Users\Moritz\Documents\GitHub\Fortgeschrittenenpraktikum\T07\Daten\GMcharakteristik.csv")
csv_reader = csv.reader(file, delimiter=";")
x = []
y = []
for row in csv_reader:
    wert = row[1]
    wert = float(wert)
    y.append(wert)
    
    wert = row[0]
    wert = float(wert)
    x.append(wert)
file.close()