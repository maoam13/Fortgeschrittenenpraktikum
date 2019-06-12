# -*- coding: utf-8 -*-
"""
Created on Sun Jun 09 23:19:39 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt
import Praktikummo2 as p
from scipy.interpolate import interp1d

data = np.genfromtxt("../Daten/2_2K.txt", delimiter = '',skip_header = 4)

B1 = data[:,0]
cutoff = p.find_nearest(B1,0.1)
B = B1[cutoff:]
Rxx = data[cutoff:,2]
Rxy = data[:,4]
phase1 = data[:,3]
phase2 = data[:,5]

freq = 9

zeros, = np.where(B == 0)
B = np.delete(B, zeros)
Rxx = np.delete(Rxx, zeros)
dRxx = np.full(len(B),min(Rxx))

f = interp1d(1./B, Rxx)
x = np.linspace(min(1./B),max(1./B),1e4)
data = f(x)-np.mean(f(x))
dRxx = np.full(len(x),min(Rxx))

def g(A, x):
        return A[0]*np.exp(-A[1]*(x))
xmin = min(x)+0.5 * 1./freq
peaks = []
peakpos = []
for i in range(15):
    anfang = p.find_nearest(x,xmin)
    ende = p.find_nearest(x,xmin+1./freq)
    peaks.append(np.max(data[anfang:ende]))
    peakpos.append(x[anfang+np.argmax(data[anfang:ende])])
    xmin += 1./freq
dpeaks = np.full(len(peaks),np.std(peaks))
fit,dfit,res = p.fitte_bel_function(peakpos,peaks,dpeaks,g,[100,2])
print fit,dfit

xmin = min(x)
peaks2 = []
peakpos2 = []
for i in range(15):
    anfang = p.find_nearest(x,xmin)
    ende = p.find_nearest(x,xmin+1./freq)
    peaks2.append(np.min(data[anfang:ende]))
    peakpos2.append(x[anfang+np.argmin(data[anfang:ende])])
    xmin += 1./freq
dpeaks = np.full(len(peaks),np.std(peaks))
fit2,dfit2,res2 = p.fitte_bel_function(peakpos2,peaks2,dpeaks,g,[100,2])
print fit2,dfit2

plt.plot(x,data)
plt.plot(x,g(fit2,x))
plt.scatter(peakpos2,peaks2)
plt.plot(x,g(fit,x))
plt.scatter(peakpos,peaks)
plt.xlim([0,2])
plt.ylim([-20,80])