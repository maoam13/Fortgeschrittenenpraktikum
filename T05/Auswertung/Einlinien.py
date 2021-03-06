# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:34:53 2018

@author: morit
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import Data as data
import Kalibration_Methode as kal

def hb_channel(peakpos,xwerte,fitwerte,halbhohe):
    split = np.where(xwerte>np.round(peakpos,1))[0][0]
    splitnach = xwerte[split:]
    splitvor = xwerte[:split]
    return splitnach[np.argmin(abs(data.gauss(fitwerte,splitnach)-halbhohe))]-splitvor[np.argmin(abs(data.gauss(fitwerte,splitvor)-halbhohe))]

def hb_E(peakpos,xwerte,fitwerte,halbhohe):
    splitnach = np.where(xwerte>np.round(peakpos,1))[0]
    splitvor = np.where(xwerte<np.round(peakpos,1))[0]
    return splitnach[np.argmin(abs(data.gauss(fitwerte,splitnach)-halbhohe))]-splitvor[np.argmin(abs(data.gauss(fitwerte,splitvor)-halbhohe))]

ein = data.Spektrum("einlinien 1h1min.ws5")

y = ein.x
x = np.arange(0,1024,1)
err = np.sqrt(y)
mittel = np.mean(y[400:700])
E = kal.Kalibration(1)[0]
dE = kal.Kalibration(1)[1]
v = kal.Kalibration(1)[2]
dv = kal.Kalibration(1)[3]

versetzung = 0
korr = 0

if 0:
    y = y[:512]
    x = x[:512]
    err = err[:512]
    E = E[:512]
    v = v[:512]
    dE = dE[:512]
    dv = dv[:512]
else:
    versetzung = 539
    korr = 512

start = 205+versetzung
ende = 270+versetzung
xfit1 = np.arange(start,ende,1)
xwerte1 = np.arange(start,ende,0.01)
E1 = E[start:ende]
Ewerte = np.arange(np.round(E1[-1],2),np.round(E1[0],2),0.001)
yfit1 = y[start:ende]
errfit1 = err[start:ende]
werte1,fehler1,chi1,m1,m2 = p.fitte_bel_function(xfit1,yfit1,errfit1,data.gauss,[241+versetzung,1,14239,10000])

if versetzung!= 0:
    y = y[512:]
    x = x[512:]
    err = err[512:]
    E = E[512:]
    dE = dE[512:]
    v = v[512:]
    dv = dv[512:]

hohe1 = min(data.gauss(werte1,xwerte1))
print mittel
print hohe1
halbhohe1 = mittel-(mittel-hohe1)/2
halbbreite1 = hb_channel(werte1[0],xwerte1,werte1,halbhohe1)
print halbbreite1, halbhohe1, 2.354*werte1[1]

plt.figure(1)
ax = plt.subplot(111)
ax.set_title("Einlinienspektrum")
ax.set_xlabel("Channel")
ax.set_ylabel("Counts")
plt.plot(x,y)
plt.plot(x,np.full(len(x),halbhohe1))
plt.plot(x,data.gauss(werte1,x))

plt.figure(2)
ax = plt.subplot(111)
ax2 = ax.twiny()
ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax.set_ylabel("Counts")
ax.set_xlabel("Energie[neV]")
ax2.errorbar(v,y,err,dv,fmt = ',')
#ax.errorbar(E,y,err,dE,fmt = ',')
ax.plot(E,np.full(len(E),halbhohe1),color = 'g')
ax2.plot(v[start-korr:ende-korr],data.gauss(werte1,xfit1))
#ax.plot(E[start-korr:ende-korr],data.gauss(werte1,xfit1))