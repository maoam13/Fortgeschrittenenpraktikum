# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:29:41 2018

@author: Moritz
"""

import Praktikummo as p
import numpy as np
import scipy.constants as s
import matplotlib.pyplot as plt
import Data as data
import Kalibration_Methode as kal

ein = np.array([21.30,20.66])
einerr = np.array([0.24,0.22])

gamma =  p.gew_mittelwert(ein,einerr)
print "gamma=",np.round(gamma,2)
sig0 = 2*s.pi*(s.c*s.hbar/(14.4*10**3*s.e))**2*1/(1+8.9)*(2*3/2+1)/(2*1/2+1)
gamfaktor = 2.+0.27*0.022*0.85*(25*10**-6)*(8.4*10**22)*(100**3)*sig0
gamecht = gamma[0]/gamfaktor
sgamecht = gamma[1]/gamfaktor
print "gammaecht=",np.round(gamecht,2),np.round(sgamecht,2)
print "gamnatlit=",np.round(s.hbar*np.log(2)/(98*10**-9*s.e)*10**9,2)
print "gamechtlit=",np.round(s.hbar*np.log(2)/(98*10**-9*s.e)*10**9*gamfaktor,2)
tau = s.hbar/(gamecht*10**-9*s.e)* 10**9
stau = s.hbar/(gamecht*10**-9*s.e)**2 * sgamecht*10**-9*s.e * 10**9
print "tau=",np.round(tau,2),np.round(stau,2)
print "taulit =",np.round(98/np.log(2),2)

einiso = np.array([10.77,13.12])
einisoerr = np.array([0.09,0.08])

print "Er=",(14.4*10**3*s.e)**2/(2*9.45*10**-26*s.c**2)/s.e

print "Iso=",np.round(p.gew_mittelwert(einiso,einisoerr),2)

mu_g = -0.0903*3.15*10**-8
print mu_g

Hyper = np.array([30.57,30.47,30.63,30.54])
dHyper = np.array([0.04,0.05,0.05,0.05])
H =  p.gew_mittelwert(Hyper,dHyper)
print "H=",H

mu = np.array([4.91,4.89,4.88,4.83,4.90,4.89,4.87,4.85])
dmu = np.array([0.01,0.02,0.01,0.01,0.01,0.02,0.02,0.01])
print "mu=",p.gew_mittelwert(mu,dmu)

hohe = np.array([1.74,1.60,1.89,1.60])
dhohe = np.array([0.16,0.19,0.24,0.17])
print "rel. Hohe1:",p.gew_mittelwert(hohe,dhohe)
hohe = np.array([2.24,2.03,2.41,2.00])
dhohe = np.array([0.13,0.22,0.29,0.19])
print "rel. Hohe2:",p.gew_mittelwert(hohe,dhohe)
print np.sqrt((0.09/2.16)**2+(1.28/1.69*0.09)**2)

quad = np.array([142.23,142.24])
dquad = np.array([0.32,0.27])
R = 0.42
fak = 35*10**24*100**3
k = 1./(4.*np.pi*s.epsilon_0)
Q = 7.*quad*s.e*10**-9/(4.*(1.-R)*s.e**2*fak*k)#*(10**15)**2
dQ = Q/quad * dquad
print Q
print dQ
print "Q=",p.gew_mittelwert(Q,dQ)
print 4./7.*(1-R)*s.e**2*0.18*10**-24/100**2*fak*k/s.e*10**9
print p.gew_mittelwert(np.array([-50.81,-51.61]),np.array([0.34,0.31]))
print p.gew_mittelwert(np.array([5.90,5.63,4.97,6.88,6.60,5.56]),np.array([0.34,0.29,0.21,0.31,0.30,0.22]))
E = 14.4*10**3*s.e
m = s.electron_mass
Ec = E/(1+2*E/(m*s.c**2))
print (Ec)/s.e*10**-3
print E/(1+(m*s.c**2)/(2*E))/s.e*10**-3

print E*(1-1./(1+(2*E)/(m*s.c**2)))/s.e*10**-3
        
D = 1.89
M = 278/(6.022*10**23)
DM1 = D/M
#print M
print D/M

D = 7.874
M = 55.845*1.66*10**-27*10**3
DM2 = D/M
#print M
print D/M

D = 0.32408
dD = 0.00015
ex = -np.log(D)/(DM2*100**3*25*10**-6)
print ex,dD/(DM2*100**3*25*10**-6*D)

DM2 = 8.4*10**22
D = 0.31549
dD = 0.00015
ex = -np.log(D)/(DM2*100**3*25*10**-6)
print ex,dD/(DM2*100**3*25*10**-6*D)

D = 0.40552
dD = 0.00018
ex = -np.log(D)/(DM1*100**3*25*10**-6)*10**24
print ex,dD/(DM1*100**3*25*10**-6*D)
        
        
        
        
        
        
        
        



