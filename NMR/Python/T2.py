# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:53:57 2018

@author: Moritz
"""

import Praktikum as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr


def fitte_bel_function(x, y, ex, ey, func, startwerte):
    model  = scipy.odr.Model(func)
    data   = scipy.odr.RealData(x, y, sx=ex, sy=ey)
    odr    = scipy.odr.ODR(data, model, beta0=startwerte)
    output = odr.run()
    return output.beta, output.sd_beta, output.res_var

file = open("C:\Users\morit\Documents\GitHub\Fortgeschrittenenpraktikum\NMR\Daten\T2mgalt\ALL0000\F0000CH2.CSV")
csv_reader = csv.reader(file, delimiter=",")
x = []
y = []
for row in csv_reader:
    wert = row[4]
    wert = float(wert)
    y.append(wert)
    
    wert = row[3]
    wert = float(wert)
    x.append(wert)
file.close()


dt = float(0.004)
t = float(0.006)
N = 6

ypeak = np.zeros(N)
yerr = np.zeros(N)
xpeak = np.zeros(N)
xerr = np.zeros(N)

for i in range(N):
    array = y[x.index(round(t,5)):x.index(round(t+dt,5))]
    xwerte = x[x.index(round(t,5)):x.index(round(t+dt,5))]
    xmaxi = np.argmax(array)
    maxi = np.max(array)
    ypeak[i] = np.mean([maxi,array[xmaxi-1],array[xmaxi+1]])
 #   ypeak[i] = maxi
    yerr[i] = 2*0.008/np.sqrt(12)#(max(ebene)-min(ebene))/np.sqrt(12)
    yerr[i] = np.std([maxi,array[xmaxi-1],array[xmaxi+1]])
    
    xwert = np.argmax(array)+x.index(round(t,5))
    xpeak[i] = float(x[xwert])
    xerr[i] = (x[4]-x[0])/np.sqrt(12)
    
    print maxi,ypeak[i],yerr[i],xpeak[i],xerr[i],xmaxi
    
    t = t+2*dt

offset = np.mean(y[:x.index(0.0)-1])

ypeak = ypeak - offset
y = y - offset


ylogerr = np.zeros(N)
xstd = np.zeros(N)
yfehler = np.zeros(N)
ylog = np.log(ypeak)
ystd = float(np.std(y[x.index(0.086):]))
for i in range(len(ylogerr)):
    ylogerr[i] = 1./ypeak[i] * yerr[i]
    yfehler[i] = yerr[i]
    xstd[i] = xerr[i]
        

plt.figure(1)
plt.errorbar(xpeak,ylog,xerr = xerr,yerr = ylogerr,fmt='.')

a, sig_a, b, sig_b, chi, cor = p.lineare_regression_xy(xpeak, ylog ,xerr, ylogerr)
ywerte = a*xpeak+b
plt.plot(xpeak,ywerte)
print chi/N
print -1./a
plt.figure(2)
plt.errorbar(xpeak,ypeak,xerr = xstd,yerr = yerr,fmt='.')

def exp(B, x):
    return B[1]* np.exp(- B[0] * x)
par,std,chi = fitte_bel_function(xpeak,ypeak,xstd,yerr, exp, [1,1])
print 1./par[0]
print chi
plt.plot(xpeak,exp(par,xpeak))

plt.figure(3)
plt.plot(x,y)
