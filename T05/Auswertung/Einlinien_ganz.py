# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:22:38 2018

@author: Moritz
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
std = np.std(y[400:700])
fehler = np.std(y[400:700])/np.sqrt(len(y[400:700]))
print fehler
E = kal.Kalibration(1)[0]-14.4*10**12
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

def lorentz(a,x):
    return a[0]*a[3]/((x-a[2])**2+a[3])+a[1]

start = 241-200+versetzung#-200
ende = 241+200+versetzung#+200
xfit1 = np.arange(start,ende,1)
xwerte1 = np.arange(start,ende,0.01)
E1 = E[start-versetzung:ende-versetzung]
Ewerte = np.arange(np.round(E1[-1],1),np.round(E1[0],1),0.01)
yfit1 = y[start:ende]
errfit1 = err[start:ende]
#werte1,fehler1,chi1,m1,m2 = p.fitte_bel_function(E1,yfit1,errfit1,data.gauss,[10,-1,14239,10000])
werte1,fehler1,chi1,m1,m2 = p.fitte_bel_function(E1,yfit1,errfit1,lorentz,[-5000,14000,10,100])

if versetzung!= 0:
    y = y[512:]
    x = x[512:]
    err = err[512:]
    E = E[512:]
    dE = dE[512:]
    v = v[512:]
    dv = dv[512:]
    
hohe1 = min(data.gauss(werte1,Ewerte))
werteu = np.array(werte1)
werteu[2] = werte1[2]-fehler1[2]
werteu[1] = werte1[1]+fehler1[1]
dhu = min(data.gauss(werteu,Ewerte))-hohe1
werteo = np.array(werte1)
werteo[2] = werte1[2]+fehler1[2]
werteo[1] = werte1[1]-fehler1[1]
dho = min(data.gauss(werteo,Ewerte))-hohe1
print dho,dhu
print hohe1
halbhohe1 = mittel-(mittel-hohe1)/2
dhhu = np.sqrt((fehler/2)**2+(dhu/2)**2)
dhho = np.sqrt((fehler/2)**2+(dho/2)**2)
#halbbreite1 = hb_channel(werte1[0],Ewerte,werte1,halbhohe1)
#dhb_unten = hb_channel(werte1[0],Ewerte,werteu,halbhohe1-dhhu)
#dhb_oben = hb_channel(werte1[0],Ewerte,werteo,halbhohe1+dhho)
#print halbbreite1, abs(dhb_unten-halbbreite1), abs(dhb_oben-halbbreite1)
#print 2*np.sqrt(2*np.log(2))*werte1[1], 2*np.sqrt(2*np.log(2))*fehler1[1]

plt.figure(1)
ax = plt.subplot(111)
ax.set_title("Einlinienspektrum")
ax.set_xlabel("Channel")
ax.set_ylabel("Counts")
plt.plot(x,y)
#plt.plot(x,np.full(len(x),halbhohe1))
#plt.plot(xfit1,data.gauss(werte1,E1))

plt.figure(2)
ax = plt.subplot(211)
ax.set_ylabel("Counts")
ax.errorbar(E+14.4*10**12,y,err,dE,fmt = ',')
ax.plot(E+14.4*10**12,np.full(len(E),halbhohe1),color = 'g')
plt.figtext(0.2,0.55,
                'm= '+str(np.round(werte1[0],2))+' +/- '+str(np.round(fehler1[0],2))+'\n'
                +'sig= '+str(np.round(werte1[1],5))+' +/- '+str(np.round(fehler1[1],5))+'\n'
                +'a= '+str(np.round(werte1[2],2))+' +/- '+str(np.round(fehler1[2],2))+'\n'
                +'b= '+str(np.round(werte1[3],2))+' +/- '+str(np.round(fehler1[3],2))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi1, 2)))
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
xw = plt.xlim()
ax2 = ax.twiny()
ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax2.errorbar(v,y,err,dv,fmt = ',')
ax2.plot(v[start-korr:ende-korr],lorentz(werte1,E1))
#ax.plot(E[start-korr:ende-korr],data.gauss(werte1,E1))
ax3=plt.subplot(212)
ax3.set_ylabel("Residuen")
plt.errorbar(E1+14.4*10**12,yfit1-lorentz(werte1,E1),errfit1,fmt = '.')
x_r = np.array(xw)
y_r = np.array([0, 0])
ax3.axis([xw[0],xw[1],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x_r, y_r, color='r')
ax3.set_xlabel("Energie[neV]")

plt.figure(3)
ax = plt.subplot(111)
ax.set_ylabel("Counts")
ax.errorbar(E+14.4*10**12,y,err,dE,fmt = ',')
#ax.plot(E+14.4*10**12,np.full(len(E),halbhohe1),color = 'g')
xw = plt.xlim()
ax2 = ax.twiny()
ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax.set_xlabel("Energie[neV]")
ax2.errorbar(v,y,err,dv,fmt = ',')
#ax2.plot(v[start-korr:ende-korr],data.gauss(werte1,E1))

plt.figure(4)
ax = plt.subplot(111)
ax.set_ylabel("Counts")
ax.hist(y[400:700])
axen =[plt.xlim()[0],plt.xlim()[1],plt.ylim()[0],plt.ylim()[1]]
plt.vlines(mittel,0,plt.ylim()[1],linestyle = '--',color = 'r')
plt.figtext(0.2,0.55,'mean= '+str(np.round(mittel,2))+'\n'+'sig= '+str(np.round(std,2))+'\n')
plt.axis(axen)