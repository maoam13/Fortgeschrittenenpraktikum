# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:20:15 2019

@author: morit
"""

import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx
def derivative(f0,h):
    f1 = [0,0,0,0]
    for i in range(4,len(f0[:-4])):
        f1.append((1./280*f0[i-4]-4./105*f0[i-3]+1./5*f0[i-2]-4./5*f0[i-1]-1./280*f0[i+4]+4./105*f0[i+3]-1./5*f0[i+2]+4./5*f0[i+1])/(h))
    
    for i in range(4,len(f0[:-4])):
        f1[i] = np.mean(f1[i-4:i+4])
    return f1

name = "4a5"
subx2 = -4.5
subx1 = -8
R1 = float(25)
R2 = float(225)
data = np.genfromtxt("../Daten/transfer_"+name+".csv",delimiter = ',', skip_header = 1)
plotnumber = 311
V_th_array = []
dV_th_array = []
g_array = []
dg_array =[]
mu_eff_array = []
dmu_eff_array = []
subthresh = []
dsubthresh = []
for i in range(1,4):
    dataset = i

    x = data[:,4*dataset-3]
    y = data[:,4*dataset-2]
    ey = y/y * 10**-10
    h = np.round(x[1]-x[0],5)
    wendepunkt = np.argmax(derivative(y[10:],h))
    
    a = int(wendepunkt-np.round(0.5/h))
    b = int(wendepunkt+np.round(1./h))
    lin = p.linreg(x[a:b],y[a:b],ey[a:b])



    
    
    
    V_th = -lin[2]/lin[0]
    V_th_array.append(V_th)
    dV_th = np.sqrt((V_th/lin[2] * lin[3])**2 + (V_th/lin[0] * lin[1])**2)
    dV_th_array.append(dV_th)
    g = lin[0]
    g_array.append(g)
    dg = lin[1]
    dg_array.append(dg)
    
    
    U = 0.02*dataset+0.01
    y2 = y/np.sqrt(lin[0])
    dy2 = np.sqrt((y2/y * ey)**2+(y2/g * dg)**2)
    x2 = x
    lin2 = p.linreg(x2[a:b],y2[a:b],dy2[a:b])
    
    steigung = lin2[0]
    dsteigung = lin2[1]
    
    
    f = 2*np.pi/np.log(R2/R1)
    C = s.epsilon_0*3.9/(145*10**-9)
    dR = 1*10**-7
    df = 2*np.pi/(np.log(R2/R1)**2) * np.sqrt((dR/R1)**2+(dR/R2)**2)
    mu_eff = lin2[0]**2/(f*C*U)
    mu_eff_array.append(mu_eff)
    dmu_eff = np.sqrt((mu_eff/steigung * dsteigung)**2 + (mu_eff/f*df)**2)
    dmu_eff_array.append(dmu_eff)
    
    b2 = find_nearest(x,subx2)
    a2 = find_nearest(x,subx1)
    ylog = np.log(y)
    linlog = p.linreg(x[a2:b2],np.log(y[a2:b2]),ey[a2:b2]/y[a2:b2])
    print linlog[0],linlog[1]*10
    subthresh.append(linlog[0])
    dsubthresh.append(linlog[1]*10)
    print np.log(10)/linlog[0], np.log(10)/linlog[0]**2 * linlog[1]*10
    
    begin = 0
    end = len(x)-1
    plt.figure("linreg")
    ax1=plt.subplot(111)
    ax1.set_ylabel("$I_d$[A]")
    ax1.set_xlabel("$V_g$[V]")
    plt.plot(x,y,label="$V_d = $"+str(U)+" V" )
    
    #plt.errorbar(x,y,yerr = ey,fmt='.')
    plt.plot(x[begin:],lin[0]*x[begin:]+lin[2],color = 'r',linestyle='dashed')
    plt.axis([-8.,x[end],0,max(y)*1.3])
    plt.figure("res")
    ax2=plt.subplot(plotnumber)
    plotnumber+=1
    ax2.set_xlabel("$V_g$[V]")
    ax2.set_ylabel("residuals[A]")
    res = y-(lin[0]*x+lin[2])
    plt.errorbar(x,res,yerr = ey,fmt='.')
    x_r = np.array([x[0], x[-1]])
    y_r = np.array([0, 0])
    plt.plot(x_r, y_r, color='r')
    plt.axis([x[begin],x[end],min(res[a:b]),max(res[a:b])])
    plt.savefig("../Bilder/"+name+"_linreg.jpg")
    
    plt.figure('mu')
    plt.plot(x2*np.sqrt(U),y/np.sqrt(lin[0]),label="$V_d = $"+str(U)+" V")
    plt.plot(x[begin:]*np.sqrt(U),lin2[0]*x[begin:]+lin2[2],color = 'r',linestyle='dashed')
    plt.axis([-2.,1,0,max(y2)*1.3])
    plt.ylabel("$I_d/\sqrt{g}[\sqrt{V/A}]$")
    plt.xlabel("$V_g \cdot \sqrt{V_d}[V^{3/2}]$")
    plt.legend()
    plt.savefig("../Bilder/"+name+"_mu.jpg")
    
    plt.figure("log")
    ax1.set_ylabel("V[V]")
    plt.plot(x,y,label="$V_d = $"+str(U)+" V")
    plt.plot(x[a2:b2],np.exp(linlog[0]*x[a2:b2]+linlog[2]),color = 'r',linestyle='dashed')
    plt.yscale('log')
    plt.ylabel("$log(I_d)[log(A)]$")
    plt.xlabel("$V_g[V]$")
    plt.legend()
    
    plt.figure("amipol")
    ax1=plt.subplot(111)
    ax1.set_ylabel("$I_d$[A]")
    ax1.set_xlabel("$V_g$[V]")
    plt.plot(x,y,label="$V_d = $"+str(U)+" V" )
    plt.legend()
    
    print str(np.round(U,2))+" & $" + str(np.round(V_th,2)) + "\pm " + str(np.round(dV_th,2)) +"$ & $" + str(np.round(g*10**9*np.sqrt(U),2)) + "\pm " + str(np.round(dg*10**9,2)) +"$ & $" + str(np.round(mu_eff*10**4,2)) + "\pm " + str(np.round(dmu_eff*10**4,2)) + "$\\\\"

V_th,dV1,dV2 = p.gew_mittelwert(np.array(V_th_array),np.array(dV_th_array))
g,dg1,dg2 = p.gew_mittelwert(np.array(g_array),np.array(dg_array))
mu,dmu1,dmu2 = p.gew_mittelwert(np.array(mu_eff_array),np.array(dmu_eff_array))
print name + " & " +str(int(R2-R1)) + " & " + str(int(R1)) + " & " + str(int(R2)) + " & $" + str(np.round(V_th,2)) + "\pm " + str(np.round(max(dV1,dV2),2)) + "$ & $" + str(np.round(mu*100**2,2)) + "\pm " + str(np.round(max(dmu1,dmu2)*100**2,2)) + "$\\\\"
print mu_eff_array

sub,dsub1,dsub2 = p.gew_mittelwert(np.array(subthresh),np.array(dsubthresh))
print name + " & $" + str(np.round(np.log(10)/sub,2)) + "\pm " + str(np.round(np.log(10)/sub**2 * np.sqrt(dsub1**2 + dsub2**2),2)) + "$\\\\"
print "\\hline"
                       
begin = 0
end = len(x)-1
         
plt.figure("linreg")
plt.vlines(V_th,-1,1,label = "$V_{th} = ($"+str(np.round(V_th,2))+"$\pm$" + str(np.round(max(dV1,dV2),2))+") V")
plt.legend()
'''
plt.figure("linreg")
ax1=plt.subplot(211)
ax1.set_ylabel("U[V]")
plt.errorbar(x,y,yerr = ey,fmt=',')
plt.plot(x[begin:b],lin[0]*x[begin:b]+lin[2],color = 'r')
plt.axis([x[begin],x[end],0,max(y)])
ax2=plt.subplot(212,sharex=ax1)
ax2.set_xlabel("t[s]")
ax2.set_ylabel("Residuen")
res = y-(lin[0]*x+lin[2])
plt.errorbar(x,res,yerr = ey,fmt='.')
x_r = np.array([x[0], x[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color='r')
plt.axis([x[begin],x[end],min(res[a:b]),max(res[a:b])])
plt.savefig("../Bilder/"+name+"_linreg.jpg")

plt.figure("log")
ax1=plt.subplot(211)
ax1.set_ylabel("U[V]")
plt.plot(x,y)
plt.plot(x[a2:b2],np.exp(linlog[0]*x[a2:b2]+linlog[2]),color = 'r')

plt.yscale('log')
ax2=plt.subplot(212,sharex=ax1)
ax2.set_xlabel("t[s]")
ax2.set_ylabel("Residuen")
res = ylog-(lin[0]*x+lin[2])
plt.errorbar(x,res,yerr = ey,fmt='.')
x_r = np.array([x[0], x[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color='r')
#plt.axis([x[a],x[b],min(res[a:b]),max(res[a:b])])
plt.savefig("../Bilder/"+name+"_log.jpg")
'''
