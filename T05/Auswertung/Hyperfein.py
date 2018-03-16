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

ein = data.Spektrum("Hyperfein messung 18h.ws5")

y = ein.x[:1024]
x = np.arange(0,1024,1)
err = np.sqrt(y)
mittel = np.mean(y[115:140])
fehler = np.std(y[115:140])/len(y[115:140])
E = kal.Kalibration(3)[0]-14.4*10**12
dE = kal.Kalibration(3)[1]
v = kal.Kalibration(3)[2]
dv = kal.Kalibration(3)[3]

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
    p1 = 79
    p2 = 166
    p3 = 230
    p4 = 274
    p5 = 337
    p6 = 418
else:
    k = -1
    ver = 512
    p1 = 942
    p2 = 855
    p3 = 792
    p4 = 748
    p5 = 685
    p6 = 601

def quad(a,x):
    return a[0]*(x-a[2])**2+a[1]

start = p1-6#72
ende = p1+6#86
xfit1 = x[start:ende]
E1 = E[start:ende]
xwerte1 = np.arange(xfit1[0],xfit1[-1],0.01)
if k ==1:
    Ewerte1 = np.arange(np.round(E1[-1],1),np.round(E1[0],1),0.01)
else:
    Ewerte1 = np.arange(np.round(E1[0],1),np.round(E1[-1],1),0.01)
yfit1 = y[start:ende]
errfit1 = err[start:ende]
werte1,fehler1,chi1,m1,m2 = p.fitte_bel_function(E1,yfit1,errfit1,quad,[1000,100000,242])

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
werte2,fehler2,chi2,m1,m2 = p.fitte_bel_function(E2,yfit2,errfit2,quad,[1000,100000,144])

start = p3-4#72
ende = p3+4#86
xfit3 = x[start:ende]
E3 = E[start:ende]
xwerte3 = np.arange(xfit3[0],xfit3[-1],0.01)
if k ==1:
    Ewerte3 = np.arange(np.round(E3[-1],1),np.round(E3[0],1),0.01)
else:
    Ewerte3 = np.arange(np.round(E3[0],1),np.round(E3[-1],1),0.01)
yfit3 = y[start:ende]
errfit3 = err[start:ende]
werte3,fehler3,chi3,m1,m2 = p.fitte_bel_function(E3,yfit3,errfit3,quad,[1000,100000,44])

start = p4-4#72
ende = p4+4#86
xfit4 = x[start:ende]
E4 = E[start:ende]
xwerte4 = np.arange(xfit4[0],xfit4[-1],0.01)
if k ==1:
    Ewerte4 = np.arange(np.round(E4[-1],1),np.round(E4[0],1),0.01)
else:
    Ewerte4 = np.arange(np.round(E4[0],1),np.round(E4[-1],1),0.01)
yfit4 = y[start:ende]
errfit4 = err[start:ende]
werte4,fehler4,chi4,m1,m2 = p.fitte_bel_function(E4,yfit4,errfit4,quad,[1000,100000,-30])

start = p5-5#72
ende = p5+5#86
xfit5 = x[start:ende]
E5 = E[start:ende]
xwerte5 = np.arange(xfit5[0],xfit5[-1],0.01)
if k ==1:
    Ewerte5 = np.arange(np.round(E5[-1],1),np.round(E5[0],1),0.01)
else:
    Ewerte5 = np.arange(np.round(E5[0],1),np.round(E5[-1],1),0.01)
yfit5 = y[start:ende]
errfit5 = err[start:ende]
werte5,fehler5,chi5,m1,m2 = p.fitte_bel_function(E5,yfit5,errfit5,quad,[1000,100000,-130])

start = p6-5#72
ende = p6+7#86
xfit6 = x[start:ende]
E6 = E[start:ende]
xwerte6 = np.arange(xfit6[0],xfit6[-1],0.01)
if k ==1:
    Ewerte6 = np.arange(np.round(E6[-1],1),np.round(E6[0],1),0.01)
else:
    Ewerte6 = np.arange(np.round(E6[0],1),np.round(E6[-1],1),0.01)
yfit6 = y[start:ende]
errfit6 = err[start:ende]
werte6,fehler6,chi6,m1,m2 = p.fitte_bel_function(E6,yfit6,errfit6,quad,[1000,100000,-230])


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
pos3 = werte3[2],fehler3[2]
pos4 = werte4[2],fehler4[2]
pos5 = werte5[2],fehler5[2]
pos6 = werte6[2],fehler6[2]
hoch1 = werte1[1]-mittel,fehler1[1]
hoch2 = werte2[1]-mittel,fehler2[1]
hoch3 = werte3[1]-mittel,fehler3[1]
hoch4 = werte4[1]-mittel,fehler4[1]
hoch5 = werte5[1]-mittel,fehler5[1]
hoch6 = werte6[1]-mittel,fehler6[1]
print pos1, hoch1
print pos2, hoch2
print pos3, hoch3
print pos4, hoch4
print pos5, hoch5
print pos6, hoch6

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
#ax2 = ax.twiny()
#ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax.set_ylabel("Counts")
ax.set_xlabel("Energie[neV]")
#ax2.errorbar(v,y,err,dv,fmt = ',')
ax.errorbar(E,y,err,dE,fmt = '.')
#ax.plot(E,np.full(len(E),halbhohe1),color = 'g')
#ax2.plot(v[start-korr:ende-korr],quad(werte1,E1))
ax.plot(Ewerte1,quad(werte1,Ewerte1))
ax.plot(Ewerte2,quad(werte2,Ewerte2))
ax.plot(Ewerte3,quad(werte3,Ewerte3))
ax.plot(Ewerte4,quad(werte4,Ewerte4))
ax.plot(Ewerte5,quad(werte5,Ewerte5))
ax.plot(Ewerte6,quad(werte6,Ewerte6))