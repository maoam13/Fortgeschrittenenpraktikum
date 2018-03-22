# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:37:40 2018

@author: Moritz
"""

import Praktikummo as p
import Kalibration_Methoden as met
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    datei = ["Stahl","leer","pfennig"]
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Alpha/Probe "+self.datei[index]+"_15min.mca", delimiter = ',', skip_header = 12, skip_footer = 37)
        

def fft_cutoff(data):
    """returns abgeschn. Daten, orginal fft, abgeschn. fft"""
    fft = np.fft.fft(data)#fft
    fftoriginal = np.copy(fft)
    fft[400:] = 0#cutoff bei index 600 (nur alles unter 600 verwendet)
    datacutoff = np.fft.ifft(fft)#inverse fft
    return [np.real((datacutoff)),fftoriginal,fft]

def leerkorrektur2(leer,data):
    l = leer[678]
    l2 = max(leer)
    pl = np.argmax(leer)
    d2 = max(data[pl-5:pl+5])
    d = data[678]
    leer = leer*d/l
    leer[434:532] = (leer[434:532]-leer[532])*0.8+leer[532]
    return leer

def leerkorrektur(leer,data):
    data = leerkorrektur2(leer,data)
    for i in range(len(data)):
        test = data[i]-leer[i]
        if test <0:
            data[i] = 0
        else:
            data[i] = test
    return data
    

def gauss(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))

def gauss2(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))

def E(x):
    return 0.013904*x+0.06003

def fitte(pos,breite,i):
    plt.figure(i)
    ax = plt.subplot(211)
    xfit,errfit,yfit,a,da,chi = met.anpassung1(yecht,yechterr,pos,1,50,breite)
    plt.errorbar(x,yecht,yerr = yechterr,fmt=',')
    x_r = np.array([plt.xlim()[0],plt.xlim()[1]])
    ax.axis([pos-100,pos+100,-10,max(gauss(a,xfit))+50])
    plt.plot(xfit,gauss(a,xfit))
    ax2 = plt.subplot(212)
    plt.errorbar(xfit,(yfit-gauss(a,xfit)),errfit,fmt = '.')
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r',linestyle = "dashed")
    ax2.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
    plt.figtext(0.14,0.8,
                'pos= '+str(np.round(a[0],1))+' +/- '+str(np.round(da[0],1))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
    return a[0]
    
def fittef(pos,breite,i):
    plt.figure(i)
    ax = plt.subplot(211)
    xfit,errfit,yfit,a,da,chi = met.anpassung1(y,yerr,pos,1,50,breite)
    plt.errorbar(x,y,yerr = yerr,fmt=',')
    x_r = np.array([plt.xlim()[0],plt.xlim()[1]])
    ax.axis([pos-100,pos+100,plt.ylim()[0],max(gauss(a,xfit))+50])
    plt.plot(xfit,gauss(a,xfit))
    ax2 = plt.subplot(212)
    plt.errorbar(xfit,(yfit-gauss(a,xfit)),errfit,fmt = '.')
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r',linestyle = "dashed")
    ax2.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
    plt.figtext(0.14,0.8,
                'pos1= '+str(np.round(a[0],1))+' +/- '+str(np.round(da[0],1))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
    return a[0]

plt.close('all')
datal = Einlesen(1).data
lerr = np.sqrt(datal)
leer = fft_cutoff(datal)[0]
ein = Einlesen(0).data
data = fft_cutoff(ein)[0]
err = np.sqrt(data)
corr = leerkorrektur2(leer,data)
correcht = leerkorrektur2(datal,ein)
correrr = np.sqrt(corr)
y = data-corr
yecht = ein-correcht
yechterr = np.sqrt(abs(yecht))
yerr = np.sqrt(abs(y))
x = np.arange(len(y))
rausch =0
if 1:
    rausch =1
    y = corr
    yecht = datal
    yechterr = np.sqrt(abs(yecht))
    yerr = np.sqrt(abs(y))

if 1:
    #print E(fitte(1250,70,1))
    #print E(fittef(1405,70,2))
    if 0:
        print E(fittef(390,10,3))
        print E(fitte(390,20,3))
        print E(fitte(390,100,3))
        print E(fitte(390,17,3))
    if rausch: #Rauschmessung
        print E(fitte(1806,30,1)),E(fitte(1806,20,1)),E(fitte(1811,30,1))#Sn Ka!
        print E(fitte(1886,30,2)),E(fitte(1886,25,2)),E(fitte(1884,10,2))#Sb ka!
        print E(fitte(1969,30,3)),E(fitte(1967,33,3)),E(fitte(1969,20,3))#Te ka? In kb
        print E(fitte(2043,30,4)),E(fitte(2040,30,4)),E(fitte(2043,15,4))#Sn kb?
        print E(fitte(460,30,5)),E(fitte(465,50,5)),E(fitte(460,7,5))#Fe? ka Eu lb
        print E(fitte(503,30,6)),E(fitte(503,30,6)),E(fitte(503,30,6))#Fe? kb Tm la Dy lb 

if 0:
    plt.figure(1)
    ax = plt.subplot(211)
    pos = 1250
    xfit,errfit,yfit,a,da,chi = met.anpassung1(y,yerr,pos,1,50,70)
    plt.errorbar(x,y,yerr = yerr,fmt=',')
    x_r = np.array([plt.xlim()[0],plt.xlim()[1]])
    ax.axis([pos-100,pos+100,plt.ylim()[0],max(gauss(a,xfit))+50])
    plt.plot(xfit,gauss(a,xfit))
    ax2 = plt.subplot(212)
    plt.errorbar(xfit,(yfit-gauss(a,xfit)),errfit,fmt = '.')
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r',linestyle = "dashed")
    ax2.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
    plt.figtext(0.14,0.8,
                'pos1= '+str(np.round(a[0],1))+' +/- '+str(np.round(da[0],1))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
    
    
    

if 1:
    plt.figure("leermessung")
    plt.plot(corr)
    
if 1:
    plt.figure("Cutoff")
    plt.plot(y)
if 1:
    plt.figure("Cutoffecht")
    plt.errorbar(x,yecht,yerr = yechterr,fmt=',')
    
if 0:
    plt.figure("original")
    plt.plot(y+corr)
    
    
