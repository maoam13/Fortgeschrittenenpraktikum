# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:06:26 2019

@author: Moritz
"""

import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt
import csv

font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

def near(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx
def lorentz(A,x):
    return A[0] + A[1]*A[3]/((x**2-A[2]**2)**2 + A[3]**2) + A[4]*x
    
#def peaks(name):
    
#name = "5 full sandwich on sio2/Green laser/Pristine1.csv"
name = "7 Cu continuous oxidized/cont2.txt"
#name = "6 Cu polycrystalline/poly6.txt"
data = np.genfromtxt("../Daten/"+name, delimiter = '',skip_header = 1)
x = data[:,0]
y = data[:,1]
dy = np.full(len(y),np.std(y[near(x,1750):near(x,2250)]))


w = 1580
d = 50
a = near(x,w-d)
b = near(x,w+d)
w1 = x[np.argmax(y[a:b])+a]
start = [850,10000000,w1,15000,1]
fit = p.fitte_bel_function(x[a:b],y[a:b],dy[a:b],lorentz,start)
fit2 = fit
print fit[0][2],fit[1][2]

draw = np.arange(w-d,w+d,0.0001)
draw2 = draw
yfit = lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw
halfmax = max(yfit)/2
h1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
h2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
halfmax = max(yfit)/2-max(dy)
dh1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
dh2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
print h2-h1, 10*np.abs((dh2-dh1)-(h2-h1))
print max(yfit),max(dy)
I1 = max(yfit)
plt.plot(x,y-fit[0][0]-fit[0][4]*x)
plt.plot(draw,lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw)
plt.plot([h1,h2],[halfmax,halfmax])

w = 1360
d = 50
a = near(x,w-d)
b = near(x,w+d)
w1 = x[np.argmax(y[a:b])+a]
start = [850,10000000,w1,15000,1]
fit = p.fitte_bel_function(x[a:b],y[a:b],dy[a:b],lorentz,start)
print fit[0][2],fit[1][2]

draw = np.arange(w-d,w+d,0.0001)
yfit = lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw
halfmax = max(yfit)/2
h1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
h2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
halfmax = max(yfit)/2-max(dy)
dh1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
dh2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
print h2-h1, 2*np.abs((dh2-dh1)-(h2-h1))
print max(yfit),max(dy)
I2 = max(yfit)
dI = max(dy)
plt.figure(2)
plt.plot(x,y-fit[0][0]-fit[0][4]*x)
plt.plot([h1,h2],[halfmax,halfmax])
plt.plot(draw,lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw)

plt.figure(3)
plt.rc('font', **font)
plt.plot(x,y)
plt.xlabel("Raman shift [$cm^{-1}$]",**font)
plt.ylabel('Intensity [a.u.]', **font)
plt.grid()
plt.tight_layout()
plt.plot(draw2,lorentz(fit2[0],draw2))
plt.plot(draw,lorentz(fit[0],draw))

print I2/I1,np.sqrt((dI/I1)**2 + (dI/I1**2 * I2)**2)
#peaks("2 mono bi tri flake/1.txt")