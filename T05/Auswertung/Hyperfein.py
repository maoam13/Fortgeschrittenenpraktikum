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
import scipy.constants as s

def hb_channel(peakpos,xwerte,fitwerte,halbhohe):
    split = np.where(xwerte>np.round(peakpos,1))[0][0]
    splitnach = xwerte[split:]
    splitvor = xwerte[:split]
    return splitnach[np.argmin(abs(data.gauss(fitwerte,splitnach)-halbhohe))]-splitvor[np.argmin(abs(data.gauss(fitwerte,splitvor)-halbhohe))]

ein = data.Spektrum("Hyperfein messung 18h.ws5")

y = ein.x[:1024]
x = np.arange(0,1024,1)
err = np.sqrt(y)
E = kal.Kalibration(3)[0]-14.4*10**12
dE = kal.Kalibration(3)[1]
v = kal.Kalibration(3)[2]
dv = kal.Kalibration(3)[3]

ver = 0
korr = 0
k = 1
off = 0
off2 = 0

if 0:
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
    off = 520
    off2 = 10

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
print werte1
print fehler1
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
    
my = np.concatenate((y[115+off2:140+off2],y[190+off2:210+off2]))
my = np.concatenate((my,y[291+off2:315+off2]))
my = np.concatenate((my,y[356+off2:380+off2]))
mittel = np.mean(my)
print mittel
std = np.std(my)
fehler = np.std(my)/len(my)
print fehler

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
print hoch1
print hoch2
print hoch3
print hoch4
print hoch5
print hoch6
print "lablabla"
iso1 = pos3[0]+pos4[0],np.sqrt(pos3[1]**2+pos4[1]**2)
iso2 = pos2[0]+pos5[0],np.sqrt(pos2[1]**2+pos5[1]**2)
iso3 = pos1[0]+pos6[0],np.sqrt(pos1[1]**2+pos6[1]**2)
print iso1
print iso2
print iso3
EH1 = pos3[0]-pos5[0],np.sqrt(pos3[1]**2+pos5[1]**2)
H1 = EH1[0]*10**-9*(1./2)/(-0.0903*3.15*10**-8*(-1./2-1./2)),EH1[1]*10**-9*(1./2)/(-0.0903*3.15*10**-8*(-1./2-1./2))
EH2 = pos2[0]-pos4[0],np.sqrt(pos4[1]**2+pos2[1]**2)
H2 = EH2[0]*10**-9*(1./2)/(-0.0903*3.15*10**-8*(-1./2-1./2)),EH2[1]*10**-9*(1./2)/(-0.0903*3.15*10**-8*(-1./2-1./2))
print EH1
print EH2
print H1
print H2
Emu2 = pos2[0]-pos3[0],np.sqrt(pos3[1]**2+pos2[1]**2)
Emu1 = pos1[0]-pos2[0],np.sqrt(pos2[1]**2+pos1[1]**2)
Emu5 = pos3[0]-pos4[0],np.sqrt(pos3[1]**2+pos4[1]**2)
Emu3 = pos4[0]-pos5[0],np.sqrt(pos4[1]**2+pos5[1]**2)
Emu4 = pos5[0]-pos6[0],np.sqrt(pos5[1]**2+pos6[1]**2)
print " "
print Emu1
print Emu2
print Emu3
print Emu4
H = 30.58
dH = 0.03
mu1 = -Emu1[0]*3./2/H/(-3./2+1./2)
mu2 = -Emu2[0]*3./2/H/(-1./2-1./2)
mu3 = -Emu3[0]*3./2/H/(-1./2-1./2)
mu4 = -Emu4[0]*3./2/H/(1./2-3./2)
print mu1,np.sqrt((mu1/Emu1[0]*Emu1[1])**2+(mu1/H*dH)**2)#6-5
print mu2,np.sqrt((mu2/Emu2[0]*Emu2[1])**2+(mu2/H*dH)**2)#5-4
print mu3,np.sqrt((mu3/Emu3[0]*Emu3[1])**2+(mu3/H*dH)**2)#3-2
print mu4,np.sqrt((mu4/Emu4[0]*Emu4[1])**2+(mu4/H*dH)**2)#2-1


plt.figure(1)
ax = plt.subplot(111)
ax.set_title("Hyperfeinstrukturspektrum")
ax.set_xlabel("Channel")
ax.set_ylabel("Counts")
plt.plot(x,y)
#plt.plot(x,np.full(len(x),halbhohe1))
#plt.plot(xfit1,quad(werte1,E1))
#plt.plot(xfit2,quad(werte2,E2))

plt.figure(2)
ax = plt.subplot(111)
ax2 = ax.twiny()
ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax.set_ylabel("Counts")
ax.set_xlabel("Energie[neV]")
ax2.errorbar([v[0],v[-1]],[y[0],y[-1]],[err[0],err[-1]],fmt = ',')
ax.errorbar(E,y,err,dE,fmt = '.')
#ax.plot(E,np.full(len(E),halbhohe1),color = 'g')
#ax2.plot(v[start-korr:ende-korr],quad(werte1,E1))
#ax.plot(Ewerte1,quad(werte1,Ewerte1))
#ax.plot(Ewerte2,quad(werte2,Ewerte2))
#ax.plot(Ewerte3,quad(werte3,Ewerte3))
##ax.plot(Ewerte4,quad(werte4,Ewerte4))
#ax.plot(Ewerte5,quad(werte5,Ewerte5))
#ax.plot(Ewerte6,quad(werte6,Ewerte6))

plt.figure(3)
ax = plt.subplot(211)
ax.set_ylabel("Counts")
ax.errorbar(E+14.4*10**12,y,err,dE,fmt = ',')
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
xw = plt.xlim()
ax2 = ax.twiny()
ax2.set_xlabel("Geschwindigkeit[mm/s]")
ax2.errorbar(v,y,err,dv,fmt = ',')
ax2.errorbar([v[0],v[-1]],[y[0],y[-1]],[err[0],err[-1]],fmt = ',')
ax.plot(Ewerte1+14.4*10**12,quad(werte1,Ewerte1))
ax.plot(Ewerte2+14.4*10**12,quad(werte2,Ewerte2))
ax.plot(Ewerte3+14.4*10**12,quad(werte3,Ewerte3))
ax.plot(Ewerte4+14.4*10**12,quad(werte4,Ewerte4))
ax.plot(Ewerte5+14.4*10**12,quad(werte5,Ewerte5))
ax.plot(Ewerte6+14.4*10**12,quad(werte6,Ewerte6))
ax3=plt.subplot(212)
ax3.set_ylabel("Residuen")
plt.errorbar(E1,yfit1-quad(werte1,E1),errfit1,fmt = '.')
plt.errorbar(E1+14.4*10**12,yfit1-quad(werte1,E1),errfit1,fmt = '.')
plt.errorbar(E2+14.4*10**12,yfit2-quad(werte2,E2),errfit2,fmt = '.')
plt.errorbar(E3+14.4*10**12,yfit3-quad(werte3,E3),errfit3,fmt = '.')
plt.errorbar(E4+14.4*10**12,yfit4-quad(werte4,E4),errfit4,fmt = '.')
plt.errorbar(E5+14.4*10**12,yfit5-quad(werte5,E5),errfit5,fmt = '.')
plt.errorbar(E6+14.4*10**12,yfit6-quad(werte6,E6),errfit6,fmt = '.')
x_r = np.array(xw)
y_r = np.array([0, 0])
ax3.axis([xw[0],xw[1],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x_r, y_r, color='r')
ax3.set_xlabel("Energie[neV]")

plt.figure(4)
ax = plt.subplot(211)
ax.set_title("Einlinienspektrum")
ax.set_xlabel("Channel")
ax.set_ylabel("Counts")
plt.plot(x,y)
axen =[plt.xlim()[0],plt.xlim()[1],plt.ylim()[0],plt.ylim()[1]]
plt.axis(axen)
plt.vlines(115+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(140+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(190+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(210+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(291+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(315+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(356+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(380+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
ax2 = plt.subplot(212)
ax2.set_ylabel("#")
ax2.set_xlabel("Counts")
ax2.hist(my)
axen =[plt.xlim()[0],plt.xlim()[1],plt.ylim()[0],plt.ylim()[1]]
plt.vlines(mittel,0,plt.ylim()[1],linestyle = '--',color = 'r')
plt.figtext(0.2,0.3,'mean= '+str(np.round(mittel,2))+'\n'+'sig= '+str(np.round(std,2))+'\n')
plt.axis(axen)

if 0:
    print "\begin{tabular}{|c|c|c|c|}"
    print "\hline"
    print "& $",np.round(werte1[0],2),"\pm",np.round(fehler1[0],2),"$ & $",np.round(werte1[1],2),"\pm",np.round(fehler1[1],2),"$ & $",np.round(werte1[2],2),"\pm",np.round(fehler1[2],2),"$ & $",np.round(chi1,3),"$\\"
    print "\hline"
    print "& $",np.round(werte2[0],2),"\pm",np.round(fehler2[0],2),"$ & $",np.round(werte2[1],2),"\pm",np.round(fehler2[1],2),"$ & $",np.round(werte2[2],2),"\pm",np.round(fehler2[2],2),"$ & $",np.round(chi2,3),"$\\"
    print "\hline"
    print "& $",np.round(werte3[0],2),"\pm",np.round(fehler3[0],2),"$ & $",np.round(werte3[1],2),"\pm",np.round(fehler3[1],2),"$ & $",np.round(werte3[2],2),"\pm",np.round(fehler3[2],2),"$ & $",np.round(chi3,3),"$\\"
    print "\hline"
    print "& $",np.round(werte4[0],2),"\pm",np.round(fehler4[0],2),"$ & $",np.round(werte4[1],2),"\pm",np.round(fehler4[1],2),"$ & $",np.round(werte4[2],2),"\pm",np.round(fehler4[2],2),"$ & $",np.round(chi4,3),"$\\"
    print "\hline"
    print "& $",np.round(werte5[0],2),"\pm",np.round(fehler5[0],2),"$ & $",np.round(werte5[1],2),"\pm",np.round(fehler5[1],2),"$ & $",np.round(werte5[2],2),"\pm",np.round(fehler5[2],2),"$ & $",np.round(chi5,3),"$\\"
    print "\hline"
    print "& $",np.round(werte6[0],2),"\pm",np.round(fehler6[0],2),"$ & $",np.round(werte6[1],2),"\pm",np.round(fehler6[1],2),"$ & $",np.round(werte6[2],2),"\pm",np.round(fehler6[2],2),"$ & $",np.round(chi6,3),"$\\"
    print "\hline"