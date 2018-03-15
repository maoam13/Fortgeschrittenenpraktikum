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

def halbbreite(peakpos,xwerte,fitwerte,halbhohe):
    split = np.where(xwerte>np.round(peakpos,1))[0][0]
    splitnach = xwerte[split:]
    splitvor = xwerte[:split]
    return splitnach[np.argmin(abs(data.gauss(fitwerte,splitnach)-halbhohe))]-splitvor[np.argmin(abs(data.gauss(fitwerte,splitvor)-halbhohe))]


ein = data.Spektrum("einlinien 1h1min.ws5")

y = ein.x
x = np.arange(0,1024,1)
err = np.sqrt(y)
mittel = np.mean(y[400:700])
energie = kal.Kalibration(1)[0]
versetzung = 0

if 1:
    y = y[:512]
    x = x[:512]
    err = err[:512]
    energie = energie[:512]
else:
    y = y[512:]
    x = x[512:]
    err = err[512:]
    energie = energie[512:]
    versetzung = 512

start = 205
ende = 270
#start = 100
#ende = 400
xfit1 = np.arange(start,ende,1)
xwerte1 = np.arange(start,ende,0.01)
yfit1 = y[start:ende]
errfit1 = err[start:ende]
werte1,fehler1,chi1,m1,m2 = p.fitte_bel_function(xfit1,yfit1,errfit1,data.gauss,[241+versetzung,1,14239,10000])

#start = 750
#ende = 804
#xwerte2 = np.arange(start,ende,0.01)
#xfit2 = np.arange(start,ende,1)
#yfit2 = y[start:ende]
#errfit2 = err[start:ende]
#werte2,fehler2,chi2,m1,m2 = p.fitte_bel_function(xfit2,yfit2,errfit2,data.gauss,[780,1,14239,10000])

#Rauschmessung
hohe1 = min(data.gauss(werte1,xwerte1))
#hohe2 = min(data.gauss(werte2,xwerte2))
print mittel
print hohe1
#print hohe2
halbhohe1 = mittel-(mittel-hohe1)/2
#halbhohe2 = mittel-(mittel-hohe2)/2
halbbreite1 = halbbreite(werte1[0],xwerte1,werte1,halbhohe1)
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
plt.plot(energie,y)
plt.plot(energie,np.full(len(energie),halbhohe1))
plt.plot(energie,data.gauss(werte1,x))