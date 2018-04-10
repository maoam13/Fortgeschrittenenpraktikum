# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:01:58 2018

@author: Moritz
"""

import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

class Einlesen:
    data = 0
    def __init__(self,index):
        datei = ["SupraX2","SupraX1_kalibriert","LeermessungX2"]
        self.data = np.genfromtxt("../Daten/Hauptversuch/"+datei[index]+".dat", delimiter = '\t',dtype = np.float)
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx


def diff(x,y,leerx,leery):
    y1 = np.copy(y)
    for i in range(len(x)):
        idx = find_nearest(leerx,x[i])
        y1[i] += leery[idx]
    return y1

def find_max(x,y,xerr,yerr):
    x = np.array(x)
    y = np.array(y)
    xerr = np.array(xerr)
    yerr = np.array(yerr)
    res = []
    resi = []
    b = 10
    i = b
    a = 0
    apos = 0
    steigung = []
    while i+b < len(x):
        ai = p.lineare_regression_xy(x[i-b:i+b],y[i-b:i+b],xerr[i-b:i+b],yerr[i-b:i+b])
        resi.append(sum(((y[i-b:i+b]-(ai[0]*x[i-b:i+b]+ai[2]))/np.sqrt(yerr[i-b:i+b]**2+(xerr[i-b:i+b]*ai[0])**2))**2))
        if ai[0] > a:
            a = ai[0]
            apos = i
        res.append(ai)
        steigung.append(ai[0])
        i +=1
    return apos, steigung,res,b,resi
            
def func(A,x):
    #return A[0]*np.arctan(A[1]*x-A[2])+A[3]+A[4]*1./(x-A[5])
    return A[0]*np.exp(A[1]/(x-A[2]))+A[3]+A[4]*1./(x-A[5])

def xrate(x):
    rate = []
    for i in range(len(x)-4):
        rate.append(x[i+4]-x[i])
    return rate

def constante(x,y):
    start1 = find_nearest(x,82)
    ende1 = find_nearest(x,87)
    start2 = find_nearest(x,107)
    ende2 = find_nearest(x,120)
    U1 = np.mean(y[start1:ende1])
    dU1 = abs(np.min(y[start1:ende1])-np.max(y[start1:ende1]))/np.sqrt(12)
    U2 = np.mean(y[start2:ende2])
    dU2 = abs(np.min(y[start2:ende2])-np.max(y[start2:ende2]))/np.sqrt(12)
    Uint = U2-U1
    print Uint,np.sqrt(dU1**2+dU2**2)
    Vsupra = 14.7*10**-9
    dVsupra = 0.1/np.sqrt(12)*10**-9
    v = 10./(0.5*10**-3)
    C =  Uint/v/Vsupra
    dC = np.sqrt((dU1/v/Vsupra)**2+(dU2/v/Vsupra)**2+(Uint/v/Vsupra**2*dVsupra)**2)
    print C,dC
    
    
    

plt.close("all")
index = 1
data = Einlesen(index).data
               
x = data[:,0]
y = data[:,1]#*-1
xerr = np.full(len(x),np.std(x[:20])/np.sqrt(10))
yerr = np.full(len(y),np.std(y[:20])*np.sqrt(2))
index = 2
data = Einlesen(index).data
leerx = data[:,0]
leery = data[:,1]#*-1
err = np.full(len(leerx),0.0001)
yoff = diff(x,y,leerx,leery)
yecht = (yoff-yoff[-1])*-1
apos,a,res,b,resi = find_max(x,yecht,xerr,yerr)
print x[apos]
constante(x,yecht)


plt.figure("X1roh")
ax = plt.subplot(111)
plt.plot(x,y,label = "Rohdaten")
plt.plot(x,yoff,label = "ohne Untergrund")
#plt.plot(x[10:-10], a)
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.title("X'-Rohdaten")
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1roh")

plt.figure("X1off")
ax = plt.subplot(111)
#plt.plot(leerx,leery)
#plt.errorbar(x,y,xerr = xerr,yerr = yerr,fmt = ".")
#plt.plot(x,yoff)
plt.plot(x[:-4],xrate(x))
#plt.plot(leerx,func(a,leerx))
#plt.axis([0,10000,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1")

plt.figure("X1spiegel")
ax = plt.subplot(111)
#plt.plot(leerx,leery)
#plt.plot(x,yoff)
#plt.errorbar(x,y,xerr = xerr,yerr = yerr,fmt = ".")
plt.plot(x,(yoff-yoff[-1])*-1)
#plt.vlines(82,-3,2,linestyle='--',color = "r")
#plt.vlines(87,-3,2,linestyle='--',color = "r")
#plt.vlines(107,-3,2,linestyle='--',color = "r")
#plt.vlines(120,-3,2,linestyle='--',color = "r")
#plt.plot(x[apos-b:apos+b],res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2], color = 'g')
#plt.plot(leerx,func(a,leerx))
#plt.axis([90,110,plt.ylim()[0],plt.ylim()[1]])
ax.set_xlabel("Temperatur[K]")
ax.set_ylabel("Amplitude[V]")
plt.tight_layout()
plt.grid()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1_spiegel")

plt.figure("X1steigung")
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax = plt.subplot(211)
plt.errorbar(x,yecht,xerr = xerr,yerr = yerr,fmt=".")
plt.plot(x[apos-b:apos+b],res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2], color = 'r')
plt.vlines(x[apos],-3,2,linestyle='--',color = "r")
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax.set_ylabel("Amplitude[V]")
plt.grid()
plt.setp(ax.get_xticklabels(), visible=False)
ax2 = plt.subplot(212,sharex = ax)
ax2.set_ylabel("Residuen[V]")
ax2.set_xlabel("Temperatur[K]")
#plt.axis([x[apos-b-10],x[apos+b+10],-0.04,0.04])
plt.grid()
plt.errorbar(x[apos-b:apos+b],yecht[apos-b:apos+b]-(res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2]),np.sqrt(yerr[apos-b:apos+b]**2+(xerr[apos-b:apos+b]*res[apos-b][0])**2),fmt = '.')
plt.axis([x[apos-b-10],x[apos+b+10],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x, np.zeros(len(x)), color='r')
plt.figtext(0.2,0.75,
                'Modell: y = a * x + b\n'
                +'T_c ='+str(np.round(x[apos],2))+'\n'
                +'a= '+str(np.round(res[apos-b][0],3))+' +/- '+str(np.round(res[apos-b][1],3))+'\n'
                +'b= '+str(np.round(res[apos-b][2],3))+' +/- '+str(np.round(res[apos-b][3],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(res[apos-b][4], 2)))
plt.tight_layout()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1_Steigung")

plt.figure("X1steigung2")
apos-=2
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax = plt.subplot(211)
plt.errorbar(x,yecht,xerr = xerr,yerr = yerr,fmt=".")
plt.plot(x[apos-b:apos+b],res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2], color = 'r')
plt.vlines(x[apos],-3,2,linestyle='--',color = "r")
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax.set_ylabel("Amplitude[V]")
plt.grid()
plt.setp(ax.get_xticklabels(), visible=False)
ax2 = plt.subplot(212,sharex = ax)
ax2.set_ylabel("Residuen[V]")
ax2.set_xlabel("Temperatur[K]")
plt.figtext(0.2,0.75,
                'Modell: y = a * x + b\n'
                +'T_c ='+str(np.round(x[apos],2))+'\n'
                +'a= '+str(np.round(res[apos-b][0],3))+' +/- '+str(np.round(res[apos-b][1],3))+'\n'
                +'b= '+str(np.round(res[apos-b][2],3))+' +/- '+str(np.round(res[apos-b][3],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(res[apos-b][4], 2)))
#plt.axis([x[apos-b-10],x[apos+b+10],-0.04,0.04])
plt.grid()
plt.errorbar(x[apos-b:apos+b],yecht[apos-b:apos+b]-(res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2]),np.sqrt(yerr[apos-b:apos+b]**2+(xerr[apos-b:apos+b]*res[apos-b][0])**2),fmt = '.')
plt.axis([x[apos-b-10],x[apos+b+10],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x, np.zeros(len(x)), color='r')
plt.tight_layout()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1_Steigung2")

plt.figure("X1steigung3")
apos+=1
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax = plt.subplot(211)
plt.errorbar(x,yecht,xerr = xerr,yerr = yerr,fmt=".")
plt.plot(x[apos-b:apos+b],res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2], color = 'r')
plt.vlines(x[apos],-3,2,linestyle='--',color = "r")
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax.set_ylabel("Amplitude[V]")
plt.grid()
plt.setp(ax.get_xticklabels(), visible=False)
ax2 = plt.subplot(212,sharex = ax)
ax2.set_ylabel("Residuen[V]")
ax2.set_xlabel("Temperatur[K]")
plt.figtext(0.2,0.75,
                'Modell: y = a * x + b\n'
                +'T_c ='+str(np.round(x[apos],2))+'\n'
                +'a= '+str(np.round(res[apos-b][0],3))+' +/- '+str(np.round(res[apos-b][1],3))+'\n'
                +'b= '+str(np.round(res[apos-b][2],3))+' +/- '+str(np.round(res[apos-b][3],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(res[apos-b][4], 2)))
#plt.axis([x[apos-b-10],x[apos+b+10],-0.04,0.04])
plt.grid()
plt.errorbar(x[apos-b:apos+b],yecht[apos-b:apos+b]-(res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2]),np.sqrt(yerr[apos-b:apos+b]**2+(xerr[apos-b:apos+b]*res[apos-b][0])**2),fmt = '.')
plt.axis([x[apos-b-10],x[apos+b+10],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x, np.zeros(len(x)), color='r')
plt.tight_layout()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1_Steigung3")

plt.figure("X1steigung4")
apos+=2
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax = plt.subplot(211)
plt.errorbar(x,yecht,xerr = xerr,yerr = yerr,fmt=".")
plt.plot(x[apos-b:apos+b],res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2], color = 'r')
plt.vlines(x[apos],-3,2,linestyle='--',color = "r")
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax.set_ylabel("Amplitude[V]")
plt.grid()
plt.setp(ax.get_xticklabels(), visible=False)
ax2 = plt.subplot(212,sharex = ax)
ax2.set_ylabel("Residuen[V]")
ax2.set_xlabel("Temperatur[K]")
plt.figtext(0.2,0.75,
                'Modell: y = a * x + b\n'
                +'T_c ='+str(np.round(x[apos],2))+'\n'
                +'a= '+str(np.round(res[apos-b][0],3))+' +/- '+str(np.round(res[apos-b][1],3))+'\n'
                +'b= '+str(np.round(res[apos-b][2],3))+' +/- '+str(np.round(res[apos-b][3],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(res[apos-b][4], 2)))
#plt.axis([x[apos-b-10],x[apos+b+10],-0.04,0.04])
plt.grid()
plt.errorbar(x[apos-b:apos+b],yecht[apos-b:apos+b]-(res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2]),np.sqrt(yerr[apos-b:apos+b]**2+(xerr[apos-b:apos+b]*res[apos-b][0])**2),fmt = '.')
plt.axis([x[apos-b-10],x[apos+b+10],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x, np.zeros(len(x)), color='r')
plt.tight_layout()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1_Steigung4")

plt.figure("X1steigung5")
apos+=1
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax = plt.subplot(211)
plt.errorbar(x,yecht,xerr = xerr,yerr = yerr,fmt=".")
plt.plot(x[apos-b:apos+b],res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2], color = 'r')
plt.vlines(x[apos],-3,2,linestyle='--',color = "r")
plt.axis([x[apos-b-10],x[apos+b+10],-1.8,-1])
ax.set_ylabel("Amplitude[V]")
plt.grid()
plt.setp(ax.get_xticklabels(), visible=False)
ax2 = plt.subplot(212,sharex = ax)
ax2.set_ylabel("Residuen[V]")
ax2.set_xlabel("Temperatur[K]")
plt.figtext(0.2,0.75,
                'Modell: y = a * x + b\n'
                +'T_c ='+str(np.round(x[apos],2))+'\n'
                +'a= '+str(np.round(res[apos-b][0],3))+' +/- '+str(np.round(res[apos-b][1],3))+'\n'
                +'b= '+str(np.round(res[apos-b][2],3))+' +/- '+str(np.round(res[apos-b][3],3))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(res[apos-b][4], 2)))
#plt.axis([x[apos-b-10],x[apos+b+10],-0.04,0.04])
plt.grid()
plt.errorbar(x[apos-b:apos+b],yecht[apos-b:apos+b]-(res[apos-b][0]*x[apos-b:apos+b]+res[apos-b][2]),np.sqrt(yerr[apos-b:apos+b]**2+(xerr[apos-b:apos+b]*res[apos-b][0])**2),fmt = '.')
plt.axis([x[apos-b-10],x[apos+b+10],plt.ylim()[0],plt.ylim()[1]])
plt.plot(x, np.zeros(len(x)), color='r')
plt.tight_layout()
plt.savefig("../Protokoll/Bilder/Haupt_Supra/X1_Steigung5")
apos-=5
print "\\begin{tabular}{|c|c|c|c|}"
print "\hline"
print "& $",np.round(x[apos],2),"\pm",np.round(xerr[apos],2),"$ & $",np.round(res[apos-b][0],3),"\pm",np.round(res[apos-b][1],3),"$ & $",np.round(res[apos-b][2],3),"\pm",np.round(res[apos-b][3],3),"$ & $",np.round(resi[apos-b], 2),"$\\\\"
print "\hline"
apos+=1
print "& $",np.round(x[apos],2),"\pm",np.round(xerr[apos],2),"$ & $",np.round(res[apos-b][0],3),"\pm",np.round(res[apos-b][1],3),"$ & $",np.round(res[apos-b][2],3),"\pm",np.round(res[apos-b][3],3),"$ & $",np.round(resi[apos-b], 2),"$\\\\"
print "\hline"
apos+=1
print "& $",np.round(x[apos],2),"\pm",np.round(xerr[apos],2),"$ & $",np.round(res[apos-b][0],3),"\pm",np.round(res[apos-b][1],3),"$ & $",np.round(res[apos-b][2],3),"\pm",np.round(res[apos-b][3],3),"$ & $",np.round(resi[apos-b], 2),"$\\\\"
print "\hline"
apos+=1
print "& $",np.round(x[apos],2),"\pm",np.round(xerr[apos],2),"$ & $",np.round(res[apos-b][0],3),"\pm",np.round(res[apos-b][1],3),"$ & $",np.round(res[apos-b][2],3),"\pm",np.round(res[apos-b][3],3),"$ & $",np.round(resi[apos-b], 2),"$\\\\"
print "\hline"
apos+=1
print "& $",np.round(x[apos],2),"\pm",np.round(xerr[apos],2),"$ & $",np.round(res[apos-b][0],3),"\pm",np.round(res[apos-b][1],3),"$ & $",np.round(res[apos-b][2],3),"\pm",np.round(res[apos-b][3],3),"$ & $",np.round(resi[apos-b], 2),"$\\\\"
print "\hline"
apos+=1
print "& $",np.round(x[apos],2),"\pm",np.round(xerr[apos],2),"$ & $",np.round(res[apos-b][0],3),"\pm",np.round(res[apos-b][1],3),"$ & $",np.round(res[apos-b][2],3),"\pm",np.round(res[apos-b][3],3),"$ & $",np.round(resi[apos-b], 2),"$\\\\"
print "\hline"
apos+=1
print "& $",np.round(x[apos],2),"\pm",np.round(xerr[apos],2),"$ & $",np.round(res[apos-b][0],3),"\pm",np.round(res[apos-b][1],3),"$ & $",np.round(res[apos-b][2],3),"\pm",np.round(res[apos-b][3],3),"$ & $",np.round(resi[apos-b], 2),"$\\\\"
print "\hline"
