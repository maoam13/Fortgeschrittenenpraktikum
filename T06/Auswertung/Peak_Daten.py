# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:05:03 2018

@author: Moritz
"""
import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s
import Kalibration_Methoden as met





def peakdata():
    pos = [[[2310,15,3500,2,50],[2635,25,1000,2,70]],[[1588,5,10000,1,70],[1815,10,2000,2,60]],         [[575,2,2500,1,50],[639,20,2500,1,40]],[[1251,3,12000,1,60],[1415,10,1400,2,40]],[[955,3,10000,1,60],   [1071,2,1200,1,50]],[[3168,24,2000,2,80],[3662,50,500,2,110]]]
    pos1 = [[[2295,15,3500,2,20],[2635,25,1000,2,45]],[[1586,5,10000,3,15],[1806,15,2000,2,35]],[[577,2,2500,1,10],[639,20,2500,1,10]],[[1251,3,12000,3,15],[1410,10,1400,2,22]],[[958,3,10000,1,10],[1071,2,1200,1,10]],[[3168,24,2000,2,40],[3662,50,500,2,65]]]
    pos,dpos,h,dh,b,db = met.Peakalles(pos,pos1)
    return pos,dpos,h,dh,b,db
