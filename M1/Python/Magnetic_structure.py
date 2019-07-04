# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:05:21 2019

@author: morit
"""

import Praktikummo2 as p
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("../Daten/Magnetic Profiles/try2 top.prf.cur", delimiter = '',skip_header = 127)
x = data[:,0]
y = data[:,1]

font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 15}


plt.figure("top")
plt.rc('font', **font)
plt.plot(x,y)
plt.grid()
#plt.ylabel("Phase [$^o$]")
plt.ylabel("Amplitude [nA]", **font)
plt.xlabel("x [$\mu m$]", **font)
plt.title("top", **font)
plt.tight_layout()

data = np.genfromtxt("../Daten/Magnetic Profiles/try2 mid.prf.cur", delimiter = '',skip_header = 127)
x = data[:,0]
y = data[:,1]


plt.figure("mid")
plt.rc('font', **font)
plt.plot(x,y)
plt.grid()
#plt.ylabel("Phase [$^o$]")
plt.ylabel("Amplitude [nA]", **font)
plt.xlabel("x [$\mu m$]", **font)
plt.title("middle", **font)
plt.tight_layout()
data = np.genfromtxt("../Daten/Magnetic Profiles/try2 bot.prf.cur", delimiter = '',skip_header = 127)
x = data[:,0]
y = data[:,1]


plt.figure("bot")
plt.rc('font', **font)
plt.plot(x,y)
plt.grid()
#plt.ylabel("Phase [$^o$]")
plt.ylabel("Amplitude [nA]", **font)
plt.xlabel("x [$\mu m$]", **font)#
plt.title("bottom", **font)
plt.tight_layout()
print np.mean([10.3,9.75,9.42,10.9,10.6,10.3,10,10.6,10.3]), np.std([10.3,9.75,9.42,10.9,10.6,10.3,10,10.6,10.3])
print np.mean([0.032,0.019,0.038]), np.std([0.032,0.019,0.038])