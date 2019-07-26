# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:58:53 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt

class runge_kutta:
    """consturcor"""
    def __init__(self,tau,m,r0,v0,sigma,S1,S2):
        self.tau = tau
        self.v0 = np.array(v0)
        self.r0 = np.array(r0)
        self.m = m
        self.sigma = sigma
        self.S1 = S1
        self.S2 = S2
        """arrays to save relevant data"""
        self.pos = []
        self.period = 0
    
    """function for acceleration"""
    a = lambda self,r: -4*np.pi**2/(r[0]**2+r[1]**2)**1.5 * r
    
    """Runge Kutta terms"""
    kx1 = lambda self,r,v,tau: tau * v
    kv1 = lambda self,r,v,tau: tau * self.a(r)
    
    kx2 = lambda self,r,v,tau: tau * (v+0.5*self.kv1(r,v,tau))
    kv2 = lambda self,r,v,tau: tau * self.a(r+0.5*self.kx1(r,v,tau))
    
    kx3 = lambda self,r,v,tau: tau * (v+0.5*self.kv2(r,v,tau))
    kv3 = lambda self,r,v,tau: tau * self.a(r+0.5*self.kx2(r,v,tau))
    
    kx4 = lambda self,r,v,tau: tau * (v+self.kv3(r,v,tau))
    kv4 = lambda self,r,v,tau: tau * self.a(r+self.kx3(r,v,tau))
    
    """calculation of r(t+tau) and v(t+tau)"""
    def step(self,r,v,tau):
        r_next = r + 1./6 * (self.kx1(r,v,tau) + 2*self.kx2(r,v,tau) 
            + 2*self.kx3(r,v,tau) + self.kx4(r,v,tau))
        
        v_next = v + 1./6 * (self.kv1(r,v,tau) + 2*self.kv2(r,v,tau) 
            + 2*self.kv3(r,v,tau) + self.kv4(r,v,tau))
        return (r_next,v_next)
    
    """execute simulation"""
    def execute(self):
        r = self.r0
        v = self.v0
        t = 0
        self.pos.append(r)
        stop = 0
        for i in range(self.m):
            """calculate one step with tau"""
            r_new,v_new = self.step(r,v,self.tau)
            
            """calculate two steps with tau/2"""
            r_new2,v_new2 = self.step(r,v,self.tau/2)
            r_new2,v_new2 = self.step(r_new2,v_new2,self.tau/2)
            
            """local error of r, v and maximum of errors"""
            r_err = np.sqrt(np.abs(r_new2-r_new)[0]**2\
                + np.abs(r_new2-r_new)[1]**2)
            v_err = np.sqrt(np.abs(v_new2-v_new)[0]**2\
                + np.abs(v_new2-v_new)[1]**2)
            err = max([r_err,v_err])
            """check for acceptance (errors < sigma)"""
            if r_err < self.sigma and v_err < self.sigma:
                r = r_new
                v = v_new
                t += self.tau
                self.pos.append(r)
                
                """break condition: if the new point completes a full orbit, 
                then end the calculation"""
                if r_new[0] < 0:
                    stop = True
                if stop and r_new[1] > 0 and r_new[0]>0:
                    self.period = t
                    break
            
            """calculation of tau_new"""
            tau_prime = (self.sigma/err)**0.2 * self.tau
            if self.tau/self.S2 < self.S1*tau_prime:
                if self.S1*tau_prime < self.S2 * self.tau:
                    self.tau = self.S1 * tau_prime
                else:
                    self.tau = self.S2 * self.tau
            else:
                self.tau = self.tau/self.S2
                
        return np.array(self.pos)
    
    """calculate relevant values"""
    def values(self):
        pos = np.array(self.pos)
        
        """specific energy of the system 
        (calculated with the starting values)"""
        energy = -4.*np.pi**2/np.sqrt(self.r0[0]**2+self.r0[1]**2)\
            +(self.v0[0]**2+self.v0[1]**2)/2
        
        perihelion = np.abs(min(pos[:,0]))
        aphelion = np.abs(max(pos[:,0]))
        """eccentricity"""
        e = (aphelion - perihelion)/ (aphelion + perihelion)
        """semi major axis"""
        a = (aphelion + perihelion)/2
        return e,a,self.period,energy


"""run simulation with v_0"""
v_0 = 0.5*np.pi
engine = runge_kutta(0.1,10000,[1,0],[0,v_0],1e-10,0.9,1.3)
pos = engine.execute()
val1 = engine.values()
"""print analytical and numerical eccentricity"""
print(np.sqrt(1.+2.*val1[-1]*(v_0)**2/(4*np.pi**2)**2),val1)

"""plot orbit"""
plt.figure(1)
plt.plot(pos[:,0],pos[:,1])
plt.scatter(0,0)
plt.axis([-1,1,-1,1])
plt.axis('equal')
plt.xlabel("x[AU]")
plt.ylabel("y[AU]")
plt.title("$v_0 = 0.5\pi$")
plt.grid()

"""repeat simulation for other orbits"""
v_0 = 1*np.pi
test = runge_kutta(0.1,10000,[1,0],[0,v_0],1e-10,0.9,1.3)
pos = test.execute()
val2 = test.values()
print(np.sqrt(1.+2.*val2[-1]*(v_0)**2/(4*np.pi**2)**2),val2)

plt.figure(2)
plt.plot(pos[:,0],pos[:,1])
plt.scatter(0,0)
plt.axis([-1,1,-1,1])
plt.axis('equal')
plt.xlabel("x[AU]")
plt.ylabel("y[AU]")
plt.title("$v_0 = 1\pi$")
plt.grid()

v_0 = 2*np.pi
test = runge_kutta(0.1,10000,[1,0],[0,v_0],1e-10,0.9,1.3)
pos = test.execute()
val3 = test.values()
print(np.sqrt(1.+2.*val3[-1]*(v_0)**2/(4*np.pi**2)**2),val3)

plt.figure(3)
plt.plot(pos[:,0],pos[:,1])
plt.scatter(0,0)
plt.axis([-1,1,-1,1])
plt.axis('equal')
plt.xlabel("x[AU]")
plt.ylabel("y[AU]")
plt.title("$v_0 = 2\pi$")
plt.grid()

"""plot Keplers 3rd law"""
a = np.array([val1[1],val2[1],val3[1]])
T = np.array([val1[2],val2[2],val3[2]])
x = np.arange(0,2.1,0.1)
plt.figure(4)
plt.scatter(T**2,a**3)
plt.plot(x,x,color = "red",linestyle = "dashed")
plt.axis([0,2,0,2])
plt.xlabel("$T^2$[YR$^2$]")
plt.ylabel("$a^3$[AU$^3$]")
plt.grid()