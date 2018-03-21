# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:01:45 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    datei = ["Ba","Ag","Cu","Mo","Rb","Tb","leer"]
    def __init__(self,index):
        self.data = np.genfromtxt("../Daten/Alpha/Kalibration "+self.datei[index]+"_15min.mca", delimiter = ',', skip_header = 12, skip_footer = 37)

def gauss(a,x):#einfache Gaussfunktion: Position in index 0, Höhe in 3
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))

def gauss2(a,x):#doppelte Gaussfunktion: Position in index 0 und 4. Höhe in 3 und 6
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))

def gauss3(a,x):#3fache gaussfunktion
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))+a[9]*np.exp(-(x-a[7])**2/(2*a[8]**2))

def anpassung3(data,err,pos,abstand,hohe,breite = 100):
    data = data[pos-breite:pos+breite]
    err = err[pos-breite:pos+breite]
    channels = np.arange(pos-breite,pos+breite)
    a,da,chi = p.fitte_bel_function(channels,data,err,gauss3,[pos+abstand,8,30,hohe,pos-abstand,8,hohe/2,pos-20,10,1000])
    return channels,err,data,a,da,chi

def anpassung2(data,err,pos,abstand,hohe,breite = 100):
    data = data[pos-breite:pos+breite]
    err = err[pos-breite:pos+breite]
    channels = np.arange(pos-breite,pos+breite)
    a,da,chi = p.fitte_bel_function(channels,data,err,gauss2,[pos+abstand,8,30,hohe,pos-abstand,8,hohe/2])
    return channels,err,data,a,da,chi

def anpassung2_2(data,err,pos,abstand,hohe,breite = 100):#nur für mich
    breite = breite
    data = data[pos-breite+10:pos+breite+30]
    err = err[pos-breite+10:pos+breite+30]
    channels = np.arange(pos-breite+10,pos+breite+30)
    a,da,chi = p.fitte_bel_function(channels,data,err,gauss2,[pos+abstand,8,30,hohe,pos-abstand,8,hohe/2])
    return channels,err,data,a,da,chi

def anpassung1(data,err,pos,abstand,hohe,breite = 50):
    breite = breite
    data = data[pos-breite:pos+breite]
    err = err[pos-breite:pos+breite]
    channels = np.arange(pos-breite,pos+breite)
    a,da,chi = p.fitte_bel_function(channels,data,err,gauss,[pos,9,30,hohe])
    return channels,err,data,a,da,chi

def Peaks(pos,pos1):
    posalt = Peakf(pos1)
    l=0
    index = 0
    peakpos = []
    errpos= []
    peakint = []
    errint= []
    for i in pos:
        k = 0
        for j in i:
            ein = Einlesen(index)
            data = ein.data
            channels = np.arange(len(data))
            err = np.sqrt(data)
            pos = j[0]
            breite = j[4]
            abstand = j[1]
            hohe = j[2]
            if j[3] == 2 and k == 0:
                x,err,y,a,da,chi = anpassung2(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if k == 1:
                x,err,y,a,da,chi = anpassung2_2(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if j[3] == 3:
                x,err,y,a,da,chi = anpassung3(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if j[3] == 1:
                x,err,y,a,da,chi = anpassung1(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            x = np.arange(x[0],x[-1],0.1)
            if j[3] == 2:
                peakpos.append(a[0])
                peakpos.append(a[4])
                errpos.append(max([da[0],abs(a[0]-posalt[l])])+0.2)
                l = l+1
                errpos.append(max([da[4],abs(a[4]-posalt[l])])+0.2)
                l = l+1
                peakint.append(a[3])
                peakint.append(a[6])
                errint.append(da[3])
                errint.append(da[6])
            if j[3] == 3:
                peakpos.append(a[0])
                errpos.append(max([da[0],abs(a[0]-posalt[l])]))
                l = l+1
                peakint.append(max(gauss3(a,channels)))
                errint.append(da[3])
            if j[3] == 1:
                peakpos.append(a[0])
                errpos.append(max([da[0],abs(a[0]-posalt[l])]))
                l = l+1
                peakint.append(a[3])
                errint.append(da[3])
            plt.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
            k = 1
        index = index+1
    return peakpos,errpos,peakint,errint

def Peakf(pos):
    index = 0
    peakpos = []
    errpos= []
    peakint = []
    errint= []
    for i in pos:
        k = 0
        for j in i:
            ein = Einlesen(index)
            data = ein.data
            channels = np.arange(len(data))
            err = np.sqrt(data)
            pos = j[0]
            breite = j[4]
            abstand = j[1]
            hohe = j[2]
            if j[3] == 2 and k == 0:
                x,err,y,a,da,chi = anpassung2(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if k == 1:
                x,err,y,a,da,chi = anpassung2_2(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if j[3] == 3:
                x,err,y,a,da,chi = anpassung3(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            if j[3] == 1:
                x,err,y,a,da,chi = anpassung1(data,np.sqrt(data+1),pos,abstand,hohe,breite)
            x = np.arange(x[0],x[-1],0.1)
            if j[3] == 2:
                peakpos.append(a[0])
                peakpos.append(a[4])
                errpos.append(da[0])
                errpos.append(da[4])
                peakint.append(a[3])
                peakint.append(a[6])
                errint.append(da[3])
                errint.append(da[6])
            if j[3] == 3:
                peakpos.append(a[0])
                errpos.append(da[0])
                peakint.append(max(gauss3(a,channels)))
                errint.append(da[3])
            if j[3] == 1:
                peakpos.append(a[0])
                errpos.append(da[0])
                peakint.append(a[3])
                errint.append(da[3])
            plt.axis([pos-100,pos+100,plt.ylim()[0],plt.ylim()[1]])
            k = 1
        index = index+1
    return peakpos