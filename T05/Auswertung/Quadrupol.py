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

ein = data.Spektrum("Quadrupol 1h45min.ws5")

y = ein.x[:1024]
x = np.arange(0,1024,1)
err = np.sqrt(y)
mittel = np.mean(y[115:140])
fehler = np.std(y[115:140])/len(y[115:140])
E = kal.Kalibration(4)[0]-14.4*10**12
dE = kal.Kalibration(4)[1]
v = kal.Kalibration(4)[2]
dv = kal.Kalibration(4)[3]

ver = 0
korr = 0
k = 1

if 1:
    y = y[:512]
    x = x[:512]
    err = err[:512]
    E = E[:512]
    v = v[:512]
    dE = dE[:512]
    dv = dv[:512]
    p1 = 393
    p2 = 235
else:
    k = -1
    ver = 512
    p1 = 627
    p2 = 787

def quad(a,x):
    return a[0]*(x-a[2])**2+a[1]

start = p1-5#72
ende = p1+5#86
xfit1 = x[start:ende]
E1 = E[start:ende]
xwerte1 = np.arange(xfit1[0],xfit1[-1],0.01)
if k ==1:
    Ewerte1 = np.arange(np.round(E1[-1],1),np.round(E1[0],1),0.01)
else:
    Ewerte1 = np.arange(np.round(E1[0],1),np.round(E1[-1],1),0.01)
yfit1 = y[start:ende]
errfit1 = err[start:ende]
werte1,fehler1,chi1,m1,m2 = p.fitte_bel_function(E1,yfit1,errfit1,quad,[1000,40000,-122])

start = p2-5#72
ende = p2+5#86
xfit2 = x[start:ende]
E2 = E[start:ende]
xwerte2 = np.arange(xfit2[0],xfit2[-1],0.01)
if k ==1:
    Ewerte2 = np.arange(np.round(E2[-1],1),np.round(E2[0],1),0.01)
else:
    Ewerte2 = np.arange(np.round(E2[0],1),np.round(E2[-1],1),0.01)
yfit2 = y[start:ende]
errfit2 = err[start:ende]
werte2,fehler2,chi2,m1,m2 = p.fitte_bel_function(E2,yfit2,errfit2,quad,[100,40000,20])


if ver != 0:
    y = y[512:]
    x = x[512:]
    err = err[512:]
    E = E[512:]
    dE = dE[512:]
    v = v[512:]
    dv = dv[512:]
#hohe1 = min(data.gauss(werte1,Ewerte))
#wertef = np.array(werte1)
#wertef[2] = werte1[2]-fehler1[2]
#wertef[1] = werte1[1]+fehler1[1]
#dh = min(data.gauss(wertef,Ewerte))-hohe1
#print dh
#print hohe1
#halbhohe1 = mittel-(mittel-hohe1)/2
#dhh = np.sqrt((fehler/2)**2+(dh/2)**2)
#halbbreite1 = hb_channel(werte1[0],Ewerte,werte1,halbhohe1)
#dhb_unten = hb_channel(werte1[0],Ewerte,werte1,halbhohe1-dhh)
#dhb_oben = hb_channel(werte1[0],Ewerte,werte1,halbhohe1+dhh)
#print halbbreite1, abs(dhb_unten-halbbreite1), abs(dhb_oben-halbbreite1)

pos1 = werte1[2],fehler1[2]
pos2 = werte2[2],fehler2[2]
hoch1 = werte1[1]-mittel,fehler1[1]
hoch2 = werte2[1]-mittel,fehler2[1]
print pos1, hoch1
print pos2, hoch2

plt.figure(1)
ax = plt.subplot(111)
ax.set_title("Einlinienspektrum")
ax.set_xlabel("Channel")
ax.set_ylabel("Counts")
plt.plot(x,y)
#plt.plot(x,np.full(len(x),halbhohe1))
plt.plot(xfit1,quad(werte1,E1))
plt.plot(xfit2,quad(werte2,E2))

plt.figure(2)
ax = plt.subplot(111)
ax2 = ax.twiny()
ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax.set_ylabel("Counts")
ax.set_xlabel("Energie[neV]")
ax2.errorbar([v[0],v[-1]],[y[0],y[-1]],[err[0],err[-1]],fmt = ',')
ax.errorbar(E,y,err,dE,fmt = '.')
#ax.axis([E[0],E[-1],32000,39000])
#ax.plot(E,np.full(len(E),halbhohe1),color = 'g')
#ax2.plot(v[start-korr:ende-korr],quad(werte1,E1))
ax.plot(Ewerte1,quad(werte1,Ewerte1))
ax.plot(Ewerte2,quad(werte2,Ewerte2))