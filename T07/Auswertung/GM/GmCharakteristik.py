# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:40:29 2018

@author: Moritz
"""
import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.odr


file = open("..\..\Daten\GMcharakteristik.csv")
csv_reader = csv.reader(file, delimiter=";")
x = []
y = []
for row in csv_reader:
    wert = row[1]
    wert = float(wert)
    y.append(wert)
    
    wert = row[0]
    wert = float(wert)
    x.append(wert)
file.close()

file = open("..\..\Daten\GMpoisson.csv")
csv_reader = csv.reader(file, delimiter=";")
test = []
for row in csv_reader:
    
    wert = row[0]
    wert = float(wert)
    test.append(wert)
file.close()

offset = np.mean(test)

"""Variablen"""
x = np.array(x)
y = np.array(y)

#Totzeitkorrektur
z = y
y = y-1
ydot =y/10
y = y/(1.-ydot*(0.000318))
logyecht = np.log(z)
logy = np.log(y)
plateau = 32
xplateau = x[plateau:]
yplateau = y[plateau:]
logyplateau = logy[plateau:]
UE = 316
UG = 353


sy = np.sqrt(x)
slogy = 1./y * sy

def f(a,x):
    return a[0]/(x-a[3])+a[1]*x+a[2]

x1 = 11
x2 = 70

var,svar,chi, corr,out= p.fitte_bel_function(x[x1:x2],logy[x1:x2],slogy[x1:x2],f,[-1000,0,7,300])
print var, chi
a,sa,b,sb,chi2,corr2 = p.lineare_regression(xplateau,np.log(yplateau),slogy[plateau:])
xw= np.arange(325,500)
f2 = f(var,xw)
f1 = a*xw + b
df1 = np.sqrt((xw*sa)**2+sb**2+2*corr2*sa*sb)
df2 = np.sqrt((svar[0]/(xw-var[3]))**2 + (xw*svar[1])**2 + svar[2]**2 + (var[0]/(xw-var[3])**2 * svar[3])**2-(xw*sa)**2-sb**2)
df3 = np.sqrt((svar[0]/(xw-var[3]))**2 + (var[0]/(xw-var[3])**2 * svar[3])**2)
sigd = np.sqrt(df2**2)#+df1**2-2*np.corrcoef(f1,f2)[0][1]*df1*df2)
UG = np.argmin(abs(abs((f2)-(f1))-sigd)) + 325
print UG
UGup = np.argmin(abs(abs((f2+df2)-(f1+df1))-sigd)) + 325
UGdown = np.argmin(abs(abs((f2-df2)-(f1-df1))-sigd)) + 325
print UG,UGup,UGdown


if 1:#logplot
    plt.figure(1)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("log(n)")
    ax.axis([300,650,4,8])
    ax.grid(linestyle='--')
    l1, = plt.plot(x,logyecht, label = "Daten")
    l7, = plt.plot(x,logy, label = "Korrektur")
#    l2, = plt.plot(x,a*x+b, label = "Plateaufit")
 #   l3, = plt.plot(x[x1+1:x2],f(var,x[x1+1:x2]), label = "1/x-Fit")
#    l4 = plt.vlines(UE,0,8,linestyle='--',color = 'g', label = "Einsatzspannung")
#    l5 = plt.vlines(UG,0,8,linestyle='--',color = 'r', label = "Geigerspannung")
#    l6 = plt.vlines(UGup,0,8,linestyle='--',color = 'y', label = "Fehlerbereich Geigerspannung")
#    plt.vlines(UGdown,0,8,linestyle='--',color = 'y')
    ax.legend()
    
if 1:
    plt.figure(3)
    ax1=plt.subplot(211)
    ax1.axis([300,650,4,7.5])
    ax1.set_ylabel("U[V]")
    plt.figtext(0.6,0.65,'Modell: y = a*x+b'+
                '\n a= '+str(np.round(a,5))+' +/- '+str(np.round(sa,5))+'\n'
                +' b= '+str(np.round(b,2))+' +/- '+str(np.round(sb,2))+' \n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi2/len(xplateau), 2)))
    plt.errorbar(x[11:],logy[11:],yerr = slogy[11:],fmt='.')
    plt.plot(x,a*x+b,color = 'r')
    ax2=plt.subplot(212,sharex=ax1)
    ax2.set_xlabel("t[s]")
    ax2.set_ylabel("Residuen")
    plt.errorbar(xplateau,logyplateau-(a*xplateau+b),yerr = slogy[plateau:],fmt='.')
    x_r = np.array(plt.xlim())
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r')
    
if 1:
    plt.figure(4)
    ax1=plt.subplot(211)
    ax1.axis([300,650,4,7.5])
    ax1.set_ylabel("U[V]")
    plt.figtext(0.5,0.6,'Modell: y = a/(x-d) + b*x + c \n'+
                'a= '+str(np.round(var[0],2))+' +/- '+str(np.round(svar[0],2))+'\n'
                +'b= '+str(np.round(var[1],5))+' +/- '+str(np.round(svar[1],5))+'\n'
                +'c= '+str(np.round(var[2],2))+' +/- '+str(np.round(svar[2],2))+'\n'
                +'d= '+str(np.round(var[3],2))+' +/- '+str(np.round(svar[3],2))+'\n'
                +'$\chi ^2 / ndof$= ' + str(np.round(chi, 2)))
    plt.errorbar(x[11:],logy[11:],yerr = slogy[11:],fmt='.')
    plt.plot(x[x1+1:x2],f(var,x[x1+1:x2]),color = 'g')
    
    ax2=plt.subplot(212,sharex=ax1)
    ax2.set_xlabel("t[s]")
    ax2.set_ylabel("Residuen")
    plt.errorbar(x[x1+2:x2],logy[x1+2:x2]-f(var,x[x1+2:x2]),yerr = slogy[x1+2:x2],fmt='.')
    x_r = np.array(plt.xlim())
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r')


if 1:#plot
    a,sa,b,sb,chi,rest = p.lineare_regression(xplateau,yplateau,sy[plateau:])
    plt.figure(2)
    ax = plt.subplot(111)
    ax.set_xlabel("U [V]")
    ax.set_ylabel("n")
    ax.grid(linestyle='--')
    ax.axis([250,650,0,1300])
    line1, = plt.plot(x,z,label = "Rohdaten")
    line2, = plt.plot(x,y, label = "Korrektur")
    ax.legend()
    
    #plt.plot(x,a*x+b)
    ##plt.vlines(UE,0,1300,linestyle='--',color = 'g')
    #plt.vlines(UG,0,1300,linestyle='--',color = 'r')
    