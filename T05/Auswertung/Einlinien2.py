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

ein = data.Spektrum("einlinien 1h1min.ws5")

y = ein.x
x = np.arange(0,1024,1)
err = np.sqrt(y)
mittel = np.mean(y[400:700])
fehler = np.std(y[400:700])/len(y[400:700])
E = kal.Kalibration(1)[0]-14.4*10**12
dE = kal.Kalibration(1)[1]
v = kal.Kalibration(1)[2]
dv = kal.Kalibration(1)[3]

versetzung = 0
korr = 0

if 1:
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

start = 241-25+versetzung#-200
ende = 241+25+versetzung#+200
xfit1 = np.arange(start,ende,1)
xwerte1 = np.arange(start,ende,0.01)
E1 = E[start-versetzung:ende-versetzung]
Ewerte = np.arange(np.round(E1[-1],1),np.round(E1[0],1),0.01)
yfit1 = y[start:ende]
errfit1 = err[start:ende]
werte1,fehler1,chi1,m1,m2 = p.fitte_bel_function(E1,yfit1,errfit1,data.gauss,[10,1,14239,10000])

if versetzung!= 0:
    y = y[512:]
    x = x[512:]
    err = err[512:]
    E = E[512:]
    dE = dE[512:]
    v = v[512:]
    dv = dv[512:]
    
hohe1 = min(data.gauss(werte1,Ewerte))
wertef = np.array(werte1)
wertef[2] = werte1[2]-fehler1[2]
wertef[1] = werte1[1]+fehler1[1]
dh = min(data.gauss(wertef,Ewerte))-hohe1
print dh
print hohe1
halbhohe1 = mittel-(mittel-hohe1)/2
dhh = np.sqrt((fehler/2)**2+(dh/2)**2)
halbbreite1 = hb_channel(werte1[0],Ewerte,werte1,halbhohe1)
dhb_unten = hb_channel(werte1[0],Ewerte,werte1,halbhohe1-dhh)
dhb_oben = hb_channel(werte1[0],Ewerte,werte1,halbhohe1+dhh)
print halbbreite1, abs(dhb_unten-halbbreite1), abs(dhb_oben-halbbreite1)

plt.figure(1)
ax = plt.subplot(111)
ax.set_title("Einlinienspektrum")
ax.set_xlabel("Channel")
ax.set_ylabel("Counts")
plt.plot(x,y)
#plt.plot(x,np.full(len(x),halbhohe1))
#plt.plot(xfit1,data.gauss(werte1,E1))

plt.figure(2)
ax = plt.subplot(111)
ax2 = ax.twiny()
ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax.set_ylabel("Counts")
ax.set_xlabel("Energie[neV]")
ax2.errorbar(v,y,err,dv,fmt = ',')
ax.errorbar(E+14.4*10**12,y,err,dE,fmt = ',')
ax.plot(E+14.4*10**12,np.full(len(E),halbhohe1),color = 'g')
ax2.plot(v[start-korr:ende-korr],data.gauss(werte1,E1))
#ax.plot(E[start-korr:ende-korr],data.gauss(werte1,E1))