# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:31:15 2018

@author: morit
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr


#y = np.array([8.81,21.5,18.4,6.07,16.74,40])
#sy = np.array([0.04,0.04,0.07,0.03,0.14,0.09])
#x = np.array([13.02,32.54,28.38,8.87,23.72,60.91])

y = np.array([8.55,20.81,22.88,6.18,18,32.22])
sy = np.array([0.04,0.06,0.17,0.06,0.07,0.15])
x = np.array([19.21,36.4,36.4,10.72,29.93,47.13])

def f(a,x):
    return a[0]*x

var,svar,chi, corr,out= p.fitte_bel_function(x,y,sy,f,[1.5])
a,sa,b,sb,chi2,rest = p.lineare_regression(x,y,sy)

plt.figure(2)
ax = plt.subplot(111)
ax.set_title("y-Achsen Korrektur")
ax.set_xlabel("berechnete Strecke [A]")
ax.set_ylabel("gemessene Strecke [A]")
plt.figtext(0.3,0.65,'Modell: y = a*x'+ '\n'
                'a= '+str(np.round(var[0],3))+' +/- '+str(np.round(svar[0],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 2)))
#plt.figtext(0.3,0.65,'Modell: y = a*x'+ '\n'
#                'a= '+str(np.round(a,3))+' +/- '+str(np.round(sa,3))+'\n'
                #+'b= '+str(np.round(var[1],5))+' +/- '+str(np.round(svar[1],5))+'\n'
#                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 2)))
ax.grid(linestyle='--')
#ax.axis([250,650,0,1300])
plt.errorbar(x,y,yerr = sy,fmt='.')
plt.plot(x,var[0]*x)
"""
plt.figure(1)
ax = plt.subplot(111)
ax.set_title("y-Achsen Korrektur")
ax.set_ylabel("berechnete Strecke [A]")
ax.set_xlabel("gemessene Strecke [A]")
plt.figtext(0.3,0.65,'Modell: y = a*x'+ '\n'
                'a= '+str(np.round(1./var[0],3))+' +/- '+str(np.round(1./var[0]**2*svar[0],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 2)))
#plt.figtext(0.3,0.65,'Modell: y = a*x'+ '\n'
#                'a= '+str(np.round(a,3))+' +/- '+str(np.round(sa,3))+'\n'
                #+'b= '+str(np.round(var[1],5))+' +/- '+str(np.round(svar[1],5))+'\n'
#                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 2)))
ax.grid(linestyle='--')
#ax.axis([250,650,0,1300])
plt.errorbar(y,x,xerr = sy,fmt='.')
xwerte = np.arange(0,50)
plt.plot(xwerte,1./var[0]*xwerte)
"""