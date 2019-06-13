# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 02:53:27 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt
import Praktikummo2 as p
from scipy.interpolate import interp1d
import scipy.constants as c

data = np.genfromtxt("../Daten/3_6K.txt", delimiter = '',skip_header = 4)

B1 = data[:,0]
cut = p.find_nearest(B1,0.1)
B = B1[:cut]
Rxx = data[:cut,2]
Rxy = data[:cut,4]
dRxy = np.full(len(Rxy),0.0001)
phase1 = data[:,3]
phase2 = data[:,5]
zeros, = np.where(B == 0)
B = np.delete(B, zeros)
Rxx = np.delete(Rxx, zeros)
Rxy = np.delete(Rxy, zeros)
dRxy = np.full(len(Rxy),1)
#a = p.find_nearest(B,-0.1)
#b = p.find_nearest(B,0.1)
#B = np.append(B[:a],B[b:])
#Rxx = np.append(Rxx[:a],Rxx[b:])

f = interp1d(1./B, Rxx)
x = np.linspace(min(1./B),max(1./B),1e7)
freq,amp = p.fourier_fft(x,f(x))
pos = p.find_nearest(freq,8)+np.argmax(amp[p.find_nearest(freq,8):p.find_nearest(freq,10)])
err = (freq[pos+1]-freq[pos-1])/np.sqrt(3)
print freq[pos],err
print 2*c.e/c.h/freq[pos]*10**-13, 2*c.e/c.h/(freq[pos]**2) *err*10**-13
begin = p.find_nearest(B,1)
a,da,b,db,chi,cor = p.linreg(B[begin:],Rxy[begin:],dRxy[begin:])
da = da* 10
a = 140.88
da = 0.66
print a,da
print np.round(1./(a*c.e)*10**-16,3),np.round(1./(a**2*c.e)*da*10**-16,3)

plt.figure(1)
plt.plot(freq[:len(freq)/2],amp[:len(freq)/2]/max(amp))
plt.xlim([0,40])
plt.ylim([0,0.1])
plt.ylabel("Amplitude")
plt.xlabel("Frequency [1/T]")
plt.grid()

plt.figure(2)
plt.plot(B,Rxy,label = "data")
plt.grid()
plt.plot(B[begin:],a*B[begin:]+b,label = "fit")
plt.ylabel("Rxy [$\Omega$]")
plt.xlabel("B [T]")
plt.legend()

plt.figure(3)
plt.plot(x,f(x))
plt.xlim([-2,0])
plt.ylabel("Rxx [$\Omega$]")
plt.xlabel("1/B [1/T]")
plt.grid()

B0 = p.find_nearest(B,0)
R0 = np.mean(Rxx[B0-500:B0+500])
dR0 = np.std(Rxx[B0-500:B0+500])
print R0,dR0
tau = 2./5 * 0.059 * c.m_e/c.e**2/(4.36e16)/R0
print tau, np.sqrt((tau/0.059*0.006)**2 + (tau/(4.36e16)*(0.07e16))**2 + (tau/R0*(dR0))**2)
