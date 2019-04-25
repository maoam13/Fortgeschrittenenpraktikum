# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:20:15 2019

@author: morit
"""

import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx
def derivative(f0,h):
    f1 = [0,0,0,0]
    for i in range(4,len(data[:-4])):
        f1.append((1./280*f0[i-4]-4./105*f0[i-3]+1./5*f0[i-2]-4./5*f0[i-1]-1./280*f0[i+4]+4./105*f0[i+3]-1./5*f0[i+2]+4./5*f0[i+1])/(h))
    
    for i in range(4,len(data[:-4])):
        f1[i] = np.mean(f1[i-4:i+4])
    return f1
data = np.genfromtxt("../Daten/transfer_4c4.csv",delimiter = ',', skip_header = 1)

x = data[:,5]
y = data[:,6]
ey = y/y * 10**-12
h = np.round(x[1]-x[0],5)
der= derivative(y,h)
wendepunkt = np.argmax(derivative(y,h))

a = int(wendepunkt-np.round(1./h))
b = int(wendepunkt+np.round(1./h))
lin = p.lineare_regression(x[a:b],y[a:b],ey[a:b])

b2 = a
a2 = int(2./h)
ylog = np.log(y)
linlog = p.lineare_regression(x[a2:b2],np.log(y[a2:b2]),ey[a2:b2])

y2 = y/np.sqrt(lin[0])
x2 = x
lin2 = p.lineare_regression(x2[a:b],y2[a:b],ey[a:b])

print lin[0]

print lin2[0]**2/(2*np.pi/np.log(225./75)*s.epsilon_0*3.9/(145*10**-9)*0.05) * 100**2

begin = 0
end = len(x)-1

plt.figure("linreg")
ax1=plt.subplot(211)
ax1.set_ylabel("U[V]")
plt.errorbar(x,y,yerr = ey,fmt=',')
plt.plot(x[begin:b],lin[0]*x[begin:b]+lin[2],color = 'r')
plt.axis([x[begin],x[end],0,max(y)])
ax2=plt.subplot(212,sharex=ax1)
ax2.set_xlabel("t[s]")
ax2.set_ylabel("Residuen")
res = y-(lin[0]*x+lin[2])
plt.errorbar(x,res,yerr = ey,fmt='.')
x_r = np.array([x[0], x[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color='r')
plt.axis([x[begin],x[end],min(res[a:b]),max(res[a:b])])

plt.figure("log")
ax1=plt.subplot(211)
ax1.set_ylabel("U[V]")
plt.plot(x,y)
plt.plot(x[a2:b2],np.exp(linlog[0]*x[a2:b2]+linlog[2]),color = 'r')

plt.yscale('log')
ax2=plt.subplot(212,sharex=ax1)
ax2.set_xlabel("t[s]")
ax2.set_ylabel("Residuen")
res = ylog-(lin[0]*x+lin[2])
plt.errorbar(x,res,yerr = ey,fmt='.')
x_r = np.array([x[0], x[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color='r')
#plt.axis([x[a],x[b],min(res[a:b]),max(res[a:b])])

plt.figure('mu')
plt.plot(x2[a:b],y[a:b]/np.sqrt(lin[0]))