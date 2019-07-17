# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:00:01 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("../Daten/5 full sandwich on sio2/Blue laser/Omega2DvsOmegaG.csv", delimiter = '',skip_header = 1)

fig1, ax1 = plt.subplots(2, 1, sharex=True,num = "omegaG_hist")
ax1[0].hist(data[:,0],50,(1540,1600),color = "blue")
plt.xlabel("$\omega_{g}$ [cm$^{-1}$]")
plt.ylabel("#")
plt.title("")

fig2, ax2 = plt.subplots(2, 1, sharex=True,num = "omega2d_hist")
ax2[0].hist(data[:,1],50,color = "blue")
plt.xlabel("$\omega_{2D}$ [cm$^{-1}$]")
print np.mean(data[:,1]),np.std(data[:,1])
plt.ylabel("#")

plt.figure("omega")
plt.scatter(data[:,0],data[:,1],color = "blue")
plt.xlabel("$\omega_G$")
plt.ylabel("$\omega_{2D}$")
data = np.genfromtxt("../Daten/5 full sandwich on sio2/Green laser/Omega2DvsOmegaG.csv", delimiter = '',skip_header = 1)
plt.scatter(data[:,0],data[:,1],color = "green")
plt.xlabel("$\omega_{g}$ [cm$^{-1}$]")
plt.ylabel("$\omega_{2D}$ [cm$^{-1}$]")

ax1[1].hist(data[:,0],50,(1540,1600),color = "green")
ax1[0].set_ylabel("#")

ax2[1].hist(data[:,1],50,color = "green")
ax2[0].set_ylabel("#")
print np.mean(data[:,1]),np.std(data[:,1])

data = np.genfromtxt("../Daten/5 full sandwich on sio2/Blue laser/GammaGvsGamma2D.csv", delimiter = '',skip_header = 1)

fig3, ax3 = plt.subplots(2, 1, sharex=True,num = "gammaG_hist")
ax3[0].hist(data[:,0],50,(0,50),color = "blue")
plt.xlabel("$\Gamma_{g}$ [cm$^{-1}$]")
plt.ylabel("#")

fig4, ax4 = plt.subplots(2, 1, sharex=True,num = "gamma2d_hist")
ax4[0].hist(data[:,1],50,(0,80),color = "blue")
plt.xlabel("$\Gamma_{2D}$ [cm$^{-1}$]")
plt.ylabel("#")

plt.figure("gamma")
plt.scatter(data[:,0],data[:,1],color = "blue")
plt.xlabel("$\Gamma_G$")
plt.ylabel("$\Gamma_{2D}$")
data = np.genfromtxt("../Daten/5 full sandwich on sio2/Green laser/Gamma2DvsGammaG.csv", delimiter = '',skip_header = 1)
plt.scatter(data[:,0],data[:,1],color = "green")

ax3[1].hist(data[:,0],50,(0,50),color = "green")
ax3[0].set_ylabel("#")
ax4[1].hist(data[:,1],50,(0,80),color = "green")
ax4[0].set_ylabel("#")