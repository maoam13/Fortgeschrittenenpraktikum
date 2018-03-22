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
    datei = ["Chip_2","Leer_5","Magnet_2","Pb_2"]
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Rontgen/Proben ohne PUR/"+self.datei[index]+"min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
        

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
    #leer = leer*d/l
    #leer[434:532] = (leer[434:532]-leer[532])*0.85+leer[532]
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
    return 6.61537*10**-3*x-22.46*10**-3

def Eerr(x):
    return np.sqrt((6.02*10**-3)**2+(x*0.00191*10**-3)**2)

def anpassung(data,err,pos,abstand,hohe,breite = 50):
    breite = breite
    data = data[pos-breite:pos+breite]
    err = err[pos-breite:pos+breite]
    channels = np.arange(pos-breite,pos+breite)
    a,da,chi = p.fitte_bel_function(channels,data,err,gauss,[pos,5,-30,hohe])
    return channels,err,data,a,da,chi

def fitte(pos,breite,hohe,i):
    if i != 0:
        plt.figure(i)
        ax = plt.subplot(211)
    xfit,errfit,yfit,a,da,chi = anpassung(yecht,yechterr,pos,1,hohe,breite)
    if i!= 0:
        plt.errorbar(E(x),yecht,yerr = yechterr,fmt=',')
        x_r = np.array([plt.xlim()[0],plt.xlim()[1]])
        ax.axis([E(pos-200),E(pos+200),-200,max(gauss(a,xfit))+100])
        plt.plot(E(xfit),gauss(a,xfit))
        ax2 = plt.subplot(212)
        plt.errorbar(E(xfit),(yfit-gauss(a,xfit)),errfit,fmt = '.')
        y_r = np.array([0, 0])
        plt.plot(x_r, y_r, color='r',linestyle = "dashed")
        ax2.axis([E(pos-100),E(pos+100),plt.ylim()[0],plt.ylim()[1]])
        plt.figtext(0.14,0.8,
                'pos1= '+str(np.round(E(a[0]),3))+' +/- '+str(np.round(E(da[0]),3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
        ax.set_ylabel("Counts")
        ax2.set_xlabel("Energie[keV]")
        ax2.set_ylabel("Residuen")
    return a[0],da[0]
    
def fittef(pos,breite,hohe,i):
    if i != 0:
        plt.figure(i)
        ax = plt.subplot(211)
    xfit,errfit,yfit,a,da,chi = met.anpassung1(y,yerr,pos,1,hohe,breite)
    if i!= 0:
        plt.errorbar(E(x),y,yerr = yerr,fmt=',')
        x_r = np.array([plt.xlim()[0],plt.xlim()[1]])
        ax.axis([E(pos-100),E(pos+100),-4,max(gauss(a,xfit))+5])
        plt.plot(E(xfit),gauss(a,xfit))
        ax2 = plt.subplot(212)
        plt.errorbar(E(xfit),(yfit-gauss(a,xfit)),errfit,fmt = '.')
        y_r = np.array([0, 0])
        plt.plot(x_r, y_r, color='r',linestyle = "dashed")
        ax2.axis([E(pos-100),E(pos+100),plt.ylim()[0],plt.ylim()[1]])
        plt.figtext(0.14,0.8,
                'pos1= '+str(np.round(E(a[0]),3))+' +/- '+str(np.round(E(da[0]),3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
        ax.set_ylabel("Counts")
        ax2.set_xlabel("Energie[keV]")
        ax2.set_ylabel("Residuen")
    return a[0],da[0]

plt.close('all')
datal = Einlesen(1).data
leer = fft_cutoff(datal)[0]
ein = Einlesen(0).data
data = fft_cutoff(ein)[0]
err = np.sqrt(data)
corr = leerkorrektur2(leer,data)
correcht = leerkorrektur2(datal,ein)
correrr = np.sqrt(corr)
y = data-corr
yecht = ein-correcht
yechterr = np.sqrt(abs(yecht)+10)
yerr = np.sqrt(abs(y)+10)
x = np.arange(len(y))
Es = E(x)
rausch =0
if 0:
    rausch =1
    y = corr
    yecht = datal
    yechterr = np.sqrt(abs(yecht))
    yerr = np.sqrt(abs(y))

if 1:
    #print E(fitte(1250,70,1))
    #print E(fittef(1405,70,2))
    if 0:#blei
        f1,df1 = fitte(560,50,420,"pb1_1")
        f3,df3 = fitte(555,15,420,"pb1_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        f1,df1 = fitte(1391,50,420,"pb2_1")
        f2,df2 = fitte(1392,15,420,"pb2_2")
        test = [E(f1),E(f2)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df2)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        f1,df1 = fitte(1596,70,20000,"pb3_1")
        f2,df2 = fitte(1596,20,20000,"pb3_2")
        test = [E(f1),E(f2)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df2)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        f1,df1 = fitte(1910,70,20000,"pb4_1")
        f2,df2 = fitte(1910,20,20000,"pb4_2")
        test = [E(f1),E(f2)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df2)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        f1,df1 = fitte(2234,30,420,"pb5_1")
        f2,df2 = fitte(2234,10,420,"pb5_2")
        test = [E(f1),E(f2)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df2)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        f1,df1 = fitte(2296,30,420,"pb6_1")
        f2,df2 = fitte(2296,10,420,"pb6_2")
        test = [E(f1),E(f2)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df2)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        f1,df1 = fitte(3984,100,420,"pb7_1")
        f2,df2 = fitte(3984,20,420,"pb7_2")
        test = [E(f1),E(f2)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df2)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        f1,df1 = fitte(4494,100,420,"pb8_1")
        f2,df2 = fitte(4494,20,420,"pb8_2")
        test = [E(f1),E(f2)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df2)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
    if 1:#chip
        f1,df1 = fitte(560,50,420,"chip1_1")
        f3,df3 = fitte(560,10,420,"chip1_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(970,50,420,"chip2_1")
        f3,df3 = fitte(970,10,420,"chip2_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(1273,20,50,"chip3_1")
        f3,df3 = fitte(1273,10,50,"chip3_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(1468,20,50,"chip4_1")
        f3,df3 = fitte(1468,10,50,"chip4_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(1805,50,400,"chip5_1")
        f3,df3 = fitte(1805,15,400,"chip5_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(1912,50,400,"chip6_1")
        f3,df3 = fitte(1912,15,400,"chip6_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(2015,50,400,"chip7_1")
        f3,df3 = fitte(2015,20,400,"chip7_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(2643,80,4000,"chip8_1")#gross
        f3,df3 = fitte(2643,20,4000,"chip8_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(2970,70,4000,"chip9_1")
        f3,df3 = fitte(2970,20,4000,"chip9_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(3822,100,4000,"chip10_1")
        f3,df3 = fitte(3822,30,4000,"chip10_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)
        
        f1,df1 = fitte(4310,100,4000,"chip11_1")
        f3,df3 = fitte(4310,30,4000,"chip11_2")
        test = [E(f1),E(f3)]
        dtest  =[abs(test[0]-test[1])]#,min([E(df1),E(df3)])]
        print np.round(np.mean(test),3),"\pm",np.round(np.max(dtest),3),"\pm",np.round(Eerr(f1),3)


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
    
    
    

if 0:
    plt.figure("leer_cut")
    ax = plt.subplot(111)
    ax.set_xlabel("Energie[keV]")
    ax.set_ylabel("Counts")
    ax.set_title("Leermessung mit Cutoff")
    plt.tight_layout()
    plt.grid()
    plt.plot(E(x),corr)
    
if 0:
    plt.figure("leer_roh")
    ax = plt.subplot(111)
    ax.set_xlabel("Energie[keV]")
    ax.set_ylabel("Counts")
    ax.set_title("Leermessung Rohdaten")
    plt.tight_layout()
    plt.grid()
    plt.plot(E(x),correcht)
    
if 0:
    plt.figure("blei_cut")
    ax = plt.subplot(111)
    ax.set_xlabel("Energie[keV]")
    ax.set_ylabel("Counts")
    ax.set_title("Blei cut")
    plt.tight_layout()
    plt.grid()
    plt.plot(x,data)
if 0:
    plt.figure("leer_fourier_2")
    ax = plt.subplot(111)
    ax.set_xlabel("Frequenz")
    ax.set_ylabel("Intensitaet")
    ax.set_title("Fourierspektrum Leermessung")
    plt.tight_layout()
    plt.plot(x,fft_cutoff(datal)[1])
    
if 0:
    plt.figure("blei_roh")
    ax = plt.subplot(111)
    ax.set_xlabel("Energie[keV]")
    ax.set_ylabel("Counts")
    ax.set_title("Blei Roh")
    plt.tight_layout()
    plt.grid()
    plt.plot(x,ein)
    
if 1:
    plt.figure("stahl_0")
    ax = plt.subplot(111)
    ax.set_xlabel("Energie[keV]")
    ax.set_ylabel("Counts")
    ax.set_title("Blei bereinigt")
    plt.tight_layout()
    plt.grid()
    plt.plot(x,yecht)
    
    
    
