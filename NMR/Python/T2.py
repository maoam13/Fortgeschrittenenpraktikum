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

def tabelle(x,y,dx,dy):
    for i in range(len(x)):
        print "\hline"
        print "$", np.round(x[i]*1000,2), "\pm",np.round(dx[i]*1000,2),"$ & $",np.round(y[i]*1000,2), "\pm",np.round(dy[i]*1000,2),"$ \\\\"

file = open("..\Daten\T2Mgalt\ALL0001\F0001CH2.CSV")
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

temp = np.zeros(len(x))
temp2 = np.zeros(len(x))
for i in range(len(x)):
    temp[i] = x[i]
    temp2[i] = y[i]
    
xd = temp
yd = temp

dt = float(0.004)
t = float(0.006)
N = 10

ypeak = np.zeros(N)
yerr = np.zeros(N)
xpeak = np.zeros(N)
xerr = np.zeros(N)

for i in range(N):
    array = y[x.index(round(t,5)):x.index(round(t+dt,5))]
    xwerte = x[x.index(round(t,5)):x.index(round(t+dt,5))]
    xmaxi = np.argmax(array)
    maxi = np.max(array)
    maxix = p.peak(xd,yd,round(t,5),round(t+dt,5))
    ypeak[i] = np.mean([maxi,maxi,array[xmaxi-1],array[xmaxi+1]])
    yerr[i] = np.std([maxi,array[xmaxi-1],array[xmaxi+1]])
    #yerr[i] = np.sqrt(yerr[i]**2 + 0.004**2)
    
    xwert = np.argmax(array)+x.index(round(t,5))
    #xpeak[i] = float(x[xwert])
    xpeak[i] = maxix
    xerr[i] = (x[4]-x[0])/np.sqrt(12)
    t = t+2*dt

offset = np.mean(y[:x.index(0.0)-10])
offsetstd =  np.std(y[:x.index(0.0)-10])
print offset,offsetstd/len(y[:x.index(0.0)-11])

ypeak = ypeak - offset
y = y - offset


ylogerr = np.zeros(N)
xstd = np.zeros(N)#=xerr
yfehler = np.zeros(N)#=yerr
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
chilog = chi/N
print chi/N
print -1./a, 1./a**2 * sig_a

plt.figure(1)
ax1=plt.subplot(211)
ax1.set_ylabel("U[V]")
plt.figtext(0.6,0.7,
            '\n a= '+str(np.round(a,2))+' +/- '+str(np.round(sig_a,2))+'\n'
            +' b= '+str(np.round(b,2))+' +/- '+str(np.round(sig_b,2))+' \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(chi/N, 2)))
plt.errorbar(xpeak,ylog,xerr = xstd,yerr = ylogerr,fmt='.')
plt.plot(xpeak,ywerte,color = 'r')

ax2=plt.subplot(212)
ax2.set_xlabel("t[s]")
ax2.set_ylabel("Residuen")
plt.errorbar(xpeak,ylog-ywerte,yerr = np.sqrt(ylogerr**2 + xstd**2),fmt='.')
x_r = np.array([xpeak[0], xpeak[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color='r')


def exp(B, x):
    return B[1]* np.exp(- B[0] * x)
par,std,chi = fitte_bel_function(xpeak,ypeak,xstd,yerr, exp, [1,1])
#print par[0] , std[0]
print 1./par[0] , 1./par[0]**2 * std[0]
print chi

plt.figure(2)
ax1=plt.subplot(211)
ax1.set_ylabel("U[V]")
plt.figtext(0.5,0.7,
            '\n a= '+str(np.round(par[0],2))+' +/- '+str(np.round(std[0],2))+'\n'
            +' b= '+str(np.round(par[1],2))+' +/- '+str(np.round(std[1],2))+' \n'
            +'$\chi ^2 / ndof$= ' + str(np.round(chi, 2)))
plt.errorbar(xpeak,ypeak,xerr = xstd,yerr = yerr,fmt='.')
plt.plot(xpeak,exp(par,xpeak),color = 'r')

ax2=plt.subplot(212)
ax2.set_xlabel("t[s]")
ax2.set_ylabel("Residuen")
plt.errorbar(xpeak,ypeak-exp(par,xpeak),yerr = np.sqrt(yerr**2 + xstd**2),fmt='.')
x_r = np.array([xpeak[0], xpeak[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color='r')

plt.figure(3)
plt.plot(x,y)

print "$", np.round(1./par[0]*1000,1), "\pm",np.round(1./par[0]**2 * std[0]*1000,1),"$ & $",np.round(chi,2),"$ & $",np.round(-1./a*1000,1), "\pm",np.round(1./a**2 * sig_a*1000,1),"$ & $",np.round(chilog,2),"$ \\\\"
