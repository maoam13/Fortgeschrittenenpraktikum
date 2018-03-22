# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:45:58 2018

@author: Moritz
"""

import Praktikummo as p
import Kalibration_Methoden as met
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    datei = ["Ba","Ag","Cu","Mo","Rb","Tb","leer"]
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Alpha/Kalibration "+self.datei[index]+"_15min.mca", delimiter = ',', skip_header = 12, skip_footer = 37)

def fft_cutoff(data):
    """returns abgeschn. Daten, orginal fft, abgeschn. fft"""
    fft = np.fft.fft(data)#fft
    fftoriginal = fft
    fft[600:] = 0#cutoff bei index 600 (nur alles unter 600 verwendet)
    datacutoff = np.fft.ifft(fft)#inverse fft
    return [datacutoff,fftoriginal,fft]

def gauss(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))

def gauss2(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))

def gauss3(a,x):
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))+a[9]*np.exp(-(x-a[7])**2/(2*a[8]**2))

def test(a,x):
    return a[1]*(x-a[0])**2+a[2]*x+a[3]



index = 0
pos = [[[2295,15,3500,2,20],[2635,25,1000,2,45]],[[1586,5,10000,3,15],[1806,15,2000,2,35]],[[577,2,2500,1,10],[639,20,2500,1,10]],[[1251,3,12000,3,15],[1410,10,1400,2,22]],[[958,3,10000,1,10],[1071,2,1200,1,10]],[[3168,24,2000,2,40],[3662,50,500,2,65]]]
pos = [[[2310,15,3500,2,50],[2635,25,1000,2,70]],[[1588,5,10000,1,70],[1815,10,2000,2,60]],[[575,2,2500,1,50],[639,20,2500,1,40]],[[1251,3,12000,1,60],[1415,10,1400,2,40]],[[955,3,10000,1,60],[1071,2,1200,1,50]],[[3168,24,2000,2,80],[3662,50,500,2,110]]]


plt.close('all')
if 0:
    plt.figure(3)
    ein = Einlesen(6)
    plt.plot(ein.data,label=ein.datei[6])
    plt.legend()
if 0:
    plt.figure(4)
    ax = plt.subplot(111)
    ax.set_title("Fouriertransformierte")
    ax.set_xlabel("Channel")
    ax.set_ylabel("Counts")
    ein = Einlesen(0)
    data = fft_cutoff(ein.data)
    plt.plot(data[0],label=ein.datei[6])
    plt.plot(ein.data,label=ein.datei[6])
    
if 1:#alle Plots
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_title("Kalibrationspektren")
    ax.set_xlabel("Channel")
    ax.set_ylabel("Counts")
    plt.grid()
    for i in range(6):
        ein = Einlesen(i)
        plt.plot(ein.data,label=ein.datei[i])
        plt.legend()

peakpos = []
errpos= []
peakint = []
errint= []
if 1:#
    for i in pos:
        k = 0
        for j in i:
            ein = Einlesen(index)
            data = ein.data
            plt.figure(ein.datei[index]+str(k))
            ax = plt.subplot(211)
            channels = np.arange(len(data))
            err = np.sqrt(data)
            plt.errorbar(channels,data,yerr = err,label=ein.datei[index],fmt=',')
            pos = j[0]
            breite = j[4]
            abstand = j[1]
            hohe = j[2]
            plt.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
            x_r = np.array([plt.xlim()[0],plt.xlim()[1]])
            if j[3] == 2 and k == 0:
                x,err,y,a,da,chi = met.anpassung2(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if k == 1:
                x,err,y,a,da,chi = met.anpassung2_2(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if j[3] == 3:
                x,err,y,a,da,chi = met.anpassung3(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if j[3] == 1:
                x,err,y,a,da,chi = met.anpassung1(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            x2 = x
            x = np.arange(x[0],x[-1],0.1)
            if j[3] == 2:
                ax.axis([pos-100,pos+100,plt.ylim()[0],max(gauss2(a,x))+500])
                ax.plot(x,gauss(a[0:4],x),color='y')
                ax.plot(x,gauss([a[4],a[5],a[2],a[6]],x),color='g')
                ax.plot(x,gauss2(a,x),color='r')
                peakpos.append(a[0])
                peakpos.append(a[4])
                errpos.append(da[0])
                errpos.append(da[4])
                peakint.append(a[3])
                peakint.append(a[6])
                errint.append(da[3])
                errint.append(da[6])
                ax2 = plt.subplot(212)
                plt.errorbar(x2,(y-gauss2(a,x2)),err,fmt = '.')
                y_r = np.array([0, 0])
                plt.plot(x_r, y_r, color='r',linestyle = "dashed")
                ax2.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
                plt.figtext(0.14,0.8,
                'pos1= '+str(np.round(a[0],1))+' +/- '+str(np.round(da[0],1))+'\n'
                +'pos2= '+str(np.round(a[4],1))+' +/- '+str(np.round(da[4],1))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
            if j[3] == 3:
                #ax.plot(x,gauss(a[0:4],x))
                #ax.plot(x,gauss([a[4],a[5],a[2],a[6]],x))
                #plt.plot(x,gauss([a[7],a[8],a[2],a[9]],x))
                ax.axis([pos-100,pos+100,plt.ylim()[0],max(gauss3(a,x))+500])
                ax.plot(x,gauss3(a,x),color='r')
                peakpos.append(a[0])
                errpos.append(da[0])
                peakint.append(max(gauss3(a,channels)))
                errint.append(da[3])
                ax2 = plt.subplot(212)
                plt.errorbar(x2,(y-gauss3(a,x2)),err,fmt = '.')
                y_r = np.array([0, 0])
                plt.plot(x_r, y_r, color='r',linestyle = "dashed")
                ax2.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
                plt.figtext(0.14,0.8,
                'pos1= '+str(np.round(a[0],1))+' +/- '+str(np.round(da[0],1))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
                
            if j[3] == 1:
                #ax.plot(x,gauss(a[0:4],x))
                ax.axis([pos-100,pos+100,plt.ylim()[0],max(gauss(a,x))+500])
                ax.plot(x,gauss(a,x),color='r')
                peakpos.append(a[0])
                errpos.append(da[0])
                peakint.append(a[3])
                errint.append(da[3])
                ax2 = plt.subplot(212)
                plt.errorbar(x2,(y-gauss(a,x2)),err,fmt = '.')
                y_r = np.array([0, 0])
                plt.plot(x_r, y_r, color='r',linestyle = "dashed")
                ax2.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
                plt.figtext(0.14,0.8,
                'pos1= '+str(np.round(a[0],1))+' +/- '+str(np.round(da[0],1))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 3)))
            if k == 0:
                ax.set_title(ein.datei[index]+" "+r'$ K_{\alpha}$')
            else:
                ax.set_title(ein.datei[index]+" "+r'$ K_{\beta}$')
            ax2.set_xlabel("Channel")
            ax.set_ylabel("Energie")
            ax2.set_ylabel("Residuen")
            plt.tight_layout()
            k = 1
        peakpos.append(index)
        index = index+1
    
    