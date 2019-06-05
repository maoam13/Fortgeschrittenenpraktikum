import numpy as np
import auswertung_nur_Methoden as AM
import STM_Methoden as STMM
import Temp_kalibration as TK
import matplotlib.pyplot as plt
import Praktikummo2 as p

R_Ohm = 10**4
k = '46'
phi = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH1.csv', delimiter=',', skip_header=18)[:,4]
U = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH2.csv', delimiter=',', skip_header=18)[:,4]
t = np.genfromtxt('../Daten/ALL00' + k + '/F00' + k + 'CH2.csv', delimiter=',', skip_header=18)[:,3]

sig_U = np.full(len(U), np.std(np.genfromtxt('../Daten/ALL0030/F0030CH2.csv', delimiter=',', skip_header=18)[:,4]))/10/np.sqrt(12)
sig_phi = np.full(len(phi), 0.2*10**(-6)/np.sqrt(12))

fig = plt.figure()
plt.errorbar(phi, U, yerr=sig_U, fmt = ',', color = 'b')
#plt.plot(phi,U)
plt.xlabel('$\phi$ [V]')
plt.ylabel('U [V]')
plt.grid()
plt.ylim(-0.06,0.06)
plt.tight_layout()
def f(B, x):
        return B[0]*np.sin(x*B[3]-B[1]) + B[2]

fit,dfit,res = p.fitte_bel_function(t,U,sig_U,f,[0.025,0.01,0.005,2000])

#plt.plot(t,f(fit,t))
print fit,dfit,res

plt.figure("fit")
ax1=plt.subplot(211)
ax1.set_ylabel("U[V]")
plt.plot(t,U)
plt.plot(t,f(fit,t),color = 'r')
plt.grid()

ax2=plt.subplot(212,sharex=ax1)
ax2.set_xlabel("t[s]")
ax2.set_ylabel("residuals[V]")
res = U-f(fit,t)
plt.errorbar(t,res,yerr = sig_U,fmt=',')
x_r = np.array([t[0], t[-1]])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color='r')
plt.grid()
#plt.axis([x[a],x[b],min(res[a:b]),max(res[a:b])])

Ic = 27.79 * 10**-6
dIc = 0.21*10**-6
Rn = 16458./10000
dRn = 54./10000
V = 0.0256*2*10**-4
dv = 0.12 * 10**-6

b = Ic*Rn/V -1
print b
db =  np.sqrt((Rn/V * dIc)**2 + (Ic/V * dRn)**2 + (Ic*Rn/V**2 * dv)**2)
print db

flux = 2*Ic*300*10**-12/b
print flux
print np.sqrt((flux/Ic * dIc)**2 + (flux/b * db)**2)
