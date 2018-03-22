# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:01:46 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s
import Kalibration_Methoden as met
posi1 = [[[2295,15,3500,2,30],[2635,25,1000,2,45]],[[1588,5,10000,3,25],[1806,15,2000,2,35]],[[575,2,2500,1,15],[639,20,2500,1,10]],[[1251,3,12000,3,100],[1410,10,1400,2,22]],[[955,3,10000,3,50],[1071,2,1200,1,15]],[[3168,24,2000,2,100],[3662,50,500,2,80]]]
posi = [[[2310,15,3500,2,50],[2635,25,1000,2,60]],[[1588,5,10000,3,70],[1815,10,2000,2,60]],[[575,2,2500,1,100],[639,20,2500,1,100]],[[1251,3,12000,3,100],[1415,10,1400,2,40]],[[955,3,10000,3,100],[1071,2,1200,1,50]],[[3168,24,2000,2,100],[3662,50,500,2,150]]]
pos,poserr,inte,interr = met.Peaks(posi,posi1)
"""Name = a1,a2,b1,b2/3||a1,a2,b2,b1/3||a,b1/3||a1,b2,b3||a1,b1||a1,a2,b2,b1
"""
E = np.array([32193.6,31817.1,37257,36350,   22162.9,25456.4,24925,   8035,8905.3,   (17374.3+17479.3)/2,19965.2,19590.3,   13395.3,14961.3,   44481.6,43744.1,51698,(50382*2+50229)/3])*10**-3
#plt.figure(1)
#plt.errorbar(pos,inte,xerr = poserr,yerr = interr,fmt = '.')
#plt.axis([0,4000,0,14000])
pos = np.array(pos)
poserr = np.array(poserr)
def lin(a,x):
    return a[0]*x+a[1]
a,da,chi,eps = p.fitte_bel_functionx(pos,E,poserr,lin,[71,5])
b = a[1]
a = a[0]
x = pos
y = E
chi = sum((y-(a*x+b))**2/(a*poserr)**2)/len(x)

plt.figure(2)
ax = plt.subplot(211)
ax.set_title("Energiekalibration")
ax.set_xlabel("Channel")
ax.set_ylabel("Energie[keV]")
plt.figtext(0.2,0.7,
                'a= '+str(np.round(a,6))+' +/- '+str(np.round(da[0],6))+'\n'
                +'b= '+str(np.round(b,5))+' +/- '+str(np.round(da[1],5))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 5)))
plt.errorbar(x,y,xerr = poserr,fmt = '.')
x2 = np.arange(0,4096)
plt.plot(x2,a*x2+b)
axen =[plt.xlim()[0],plt.xlim()[1],plt.ylim()[0],plt.ylim()[1]]
ax2 = plt.subplot(212)
ax2.set_ylabel("Residuen")
plt.errorbar(x,(y-(a*x+b)),a*poserr,fmt = '.')
x_r = np.array([-100,4096])
y_r = np.array([0, 0])
ax2.axis([plt.xlim()[0],plt.xlim()[1],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x_r, y_r, color='r',linestyle = "dashed")


