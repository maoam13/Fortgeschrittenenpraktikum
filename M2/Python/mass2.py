# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:42:22 2019

@author: Moritz
"""
import numpy as np
import matplotlib.pyplot as plt
import Praktikummo2 as p
from scipy.interpolate import interp1d
import scipy.constants as c
import scipy.optimize as opt

A0 = [129.96,-15.84]
dA0 = [5.67,1.83]
B0 = [3.98,2.04]
dB0 = [0.07,0.20]

A1 = [128.05,-9.92]
dA1 = [8.43,0.73]
B1 = [3.02,0.51]
dB1 = [0.09,0.08]
x = np.arange(0.001,10,0.001)
def f(A,B,x):
    return A*np.exp(-B*x)
y = np.array(f(A0[0],B0[0],x)-f(A0[1],B0[1],x))/np.array((f(A1[0],B1[0],x)-f(A1[1],B1[1],x)))
plt.plot(x,y)
T1 = 4.2
T2 = np.mean([2.495,2.403,2.249,2.211,2.195,2.184,2.171,2.168,2.164,2.161,2.163])
const = 2.*np.pi**2*c.k/(c.hbar*c.e)

def g(A,x):
    return T1*np.sinh(const*T2*A*x*c.m_e)/(T2*np.sinh(const*T1*A*x*c.m_e))

fit,cov = opt.curve_fit(g,x,y,p0=[0.057])

plt.plot(x,g(fit[0],x))
plt.xlim([0,4])
plt.ylim([0,2])

print fit[0]



m = fit[0]*c.m_e
t = 1
y = np.log(np.array(f(A0[0],B0[0],x)-f(A0[1],B0[1],x)))
plt.figure(2)
anfang = p.find_nearest(x,2)
a,da,b,db,cov,rest = p.linreg(x[anfang:],y[anfang:],np.full(len(y[anfang:]),0.1))
plt.plot(x,y)
plt.plot(x,a*x+b)
print a