# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:51:24 2019

@author: Moritz
"""
import numpy as np
import matplotlib.pyplot as plt

class oscillator:
    '''consturctur'''
    def __init__(self,x_boundary,L,tau,m,Omega,sigma,x0):
        '''Delta = 0.03 for our simulations parameters'''
        self.Delta = np.abs(x_boundary[1]-x_boundary[0])/(L-1)
        self.tau = tau
        self.L = L
        self.m = m
        self.x0 = x0
        self.sigma = sigma
        self.Omega = Omega
        self.name = "{0}{1}{2}".format(self.Omega,self.sigma,self.x0)
        
        '''discrete x-values'''
        self.x = np.array([i*self.Delta+x_boundary[0] for i in range(L)])
        '''potential at the discrete values'''
        self.V = np.array(self.potential(self.x))
    
    '''initial gaussian wave function'''
    def psi0(self,x):
        return (np.pi*self.sigma**2)**(-0.25)*np.exp(-(x-self.x0)**2\
            /(2*self.sigma**2))
    
    '''potential at position x'''
    def potential(self,x):
        return self.Omega**2 * x**2 /2
        
    '''calculation of the matrix for a time step
    returns: exp(-i * tau * H)'''
    def matrizes(self):
        L = self.L
        V = self.V
        
        '''exp(-i tau V)'''
        eV=np.full((L,L),0.+0j,dtype=complex)
        
        '''exp(-i tau K1/2)'''
        eK1=np.full((L,L),0.+0j,dtype=complex)
        
        '''exp(-i tau K1/2)'''
        eK2=np.full((L,L),0.+0j,dtype=complex)
        
        c=np.cos(self.tau/(4*self.Delta**2))+0j
        s=np.sin(self.tau/(4*self.Delta**2))+0j
        for i in range(0,L):
            eV[i,i]=np.exp(-1j*self.tau*(V[i]+(self.Delta)**(-2)))
            eK1[i,i]=c
            eK2[i,i]=c
            if i%2==0:
                eK2[i,i-1]=1j*s
                eK2[i-1,i]=1j*s
            else:
                eK1[i,i-1]=1j*s
                eK1[i-1,i]=1j*s
        eK1[L-1,L-1]=1
        eK2[0,0]=1
        eK2[0,-1]=0
        eK2[-1,0]=0
        
        '''calculate  exp(-i * tau * H) by matrix multiplication'''
        eH = np.matmul(eK2,eK1)
        eH = np.matmul(eV,eH)
        eH = np.matmul(eK2,eH)
        eH = np.matmul(eK1,eH)
        return eH
    
    
    
    '''execution of the simulation'''
    def execute(self):
        eH = self.matrizes()
        psi = self.psi0(self.x)
        file_prob = open(self.name+"_prob.txt","w+")
        file_av = open(self.name+"_av.txt","w+")
        for i in range(self.m+1):
            """save <x>, <x^2> and t every 200 steps"""
            if i%200==0:
                av = self.average(psi)
                std = self.derivation(psi)
                t = i*self.tau
                file_av.write("{0},{1},{2}\n".format(av,std,t))
            """save probability at t=0,2,4,...,10"""
            if i*self.tau%2==0:
                p = np.abs(psi*np.conj(psi))*self.Delta
                t = i*self.tau
                for j in p:
                    file_prob.write("{0},".format(j))
                file_prob.write("{0}\n".format(t))
                
            """calculate next time step"""
            psi = np.matmul(eH,psi)
        file_prob.close()
        file_av.close()
    
    '''numerical integration of f*|psi_star*psi| following Spimpson rule
    returns: integrated value'''
    def integrate(self,psi,f):
        psi_star = np.conj(psi)
        h = self.Delta
        S = 0 
        i = 1
        func = f * np.abs(psi_star*psi)
        while i<self.L:
            S += h/3 * (func[i-1] + 4*func[i]+ func[i+1])
            i += 2
        return S
        
    """calculate norm (not used)"""
    def norm(self,psi):
        f = np.full(self.L,1)
        return self.integrate(psi,f)
    
    """calculate <x>"""
    def average(self,psi):
        return self.integrate(psi,self.x)
    
    """calculate <x^2>"""
    def derivation(self,psi):
        return self.integrate(psi,self.x**2)
    
    """calculate analytical value of <x^2>"""
    def analytical2x(self,t):
        return 1./4 *self.sigma**2 + 1./(4 * self.Omega**2 * self.sigma**2)\
            + 1./4 * (self.sigma**2 - 1./(self.Omega**2 * self.sigma**2))\
            * np.cos(2*self.Omega * t)
    
    """calculate analytical value of <x>"""
    def analyticalx(self,t):    
        return self.x0*np.cos(self.Omega*t)    
    
    """plot probability distribution"""
    def plot_probapility(self):
        font = {'weight':'bold','size':13}
        font2 = {'weight':'bold','size':20}
        plt.figure(1)
        plt.rc('font',**font)
        file = np.genfromtxt(self.name+"_prob.txt",delimiter = ",")
        for i in range(len(file)):
            plt.plot(self.x,file[i,:-1],label=r'$t=%.2f$'%(file[i][-1]))
        plt.legend(framealpha=0.5)
        plt.title("$\Omega = {0},\sigma = {1},x_0 = {2}$"\
            .format(self.Omega,self.sigma,self.x0),**font2)
        plt.xlabel("x",**font)
        plt.ylabel("Probability",**font)
        plt.grid()
    
    """plot <x> and <x^2>"""
    def plot_average(self):
        font = {'weight':'bold','size':13}
        font2 = {'weight':'bold','size':20}
        plt.figure(2)
        plt.rc('font',**font)
        file = np.genfromtxt(self.name+"_av.txt",delimiter = ",")
        t = file[:,2]
        av = np.array(file[:,0])
        std = np.array(file[:,1])
        plt.plot(t,av,label="$<x(t)>$",color = "red")
        plt.plot(t,std-av**2,label="$<x(t)^2>-<x(t)>^2$",color = "blue")
        plt.legend(frameon = True, framealpha=0.8)
        plt.title("$\Omega = {0}, \sigma = {1}, x_0 = {2}$"\
            .format(self.Omega,self.sigma,self.x0),**font2)
        plt.xlabel("t",**font)
        plt.ylabel("Difference",**font)
        plt.tight_layout()
        plt.grid()
        
    """plot difference between analytical and numerical solution"""
    def plot_difference(self):
        font = {'weight':'bold','size':13}
        font2 = {'weight':'bold','size':20}
        plt.figure(3)
        plt.rc('font',**font)
        file = np.genfromtxt(self.name+"_av.txt",delimiter = ",")
        t = file[:,2]
        av = np.array(file[:,0])
        std = np.array(file[:,1])
        plt.plot(t, std-av**2 - self.analytical2x(t),color = "blue",\
            label="$<x(t)>$")
        plt.plot(t, av - self.analyticalx(t),color = "red",\
            label="$<x(t)^2>-<x(t)>^2$")
        plt.legend(frameon = True, framealpha=0.8)
        plt.title("$\Omega = {0}, \sigma = {1}, x_0 = {2}$"\
            .format(self.Omega,self.sigma,self.x0),**font2)
        plt.xlabel("t",**font)
        plt.ylabel("Difference",**font)
        plt.tight_layout()
        plt.grid()

'''run simulation with input:
x-range,L,tau,m,Omega,sigma,x_0'''
engine = oscillator((-15,15),1001,0.00025,40000,1,1,0)
engine.execute()
engine.plot_probapility()
engine.plot_average()
engine.plot_difference()