# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 16:34:19 2018

@author: grldm
"""

import numpy as np
import auswertung_nur_Methoden as AM

def addiere_abstaende(data):
    summe = 0
    for i in range(len(data[:,1]) - 1):
        summe += np.abs(data[i][1] - data[i+1][1])
    return summe/(len(data[:,1]) - 1)

def lese_Profillinie_ein(IGain, vor = 1, alt = 0):
    if alt == 1:
        if vor == 1:
            return np.genfromtxt("Profillinien/{0:1.0f}_alt_vor.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
        else:
            return np.genfromtxt("Profillinien/{0:1.0f}_alt_nach.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
    else:
        if vor == 1:
            return np.genfromtxt("Profillinien/{0:1.0f}_vor.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
        else:
            return np.genfromtxt("Profillinien/{0:1.0f}_nach.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)

#def get_peak_by_approx(x, y, approx, k = 6):
#    xpeak = []
#    for i in range(len(approx)):
#        bla = p.peak(x, (-1)**(i+1) * y, x[approx[i] - k], x[approx[i] + k])
#        xpeak.append(bla)
#    return xpeak

def get_peak_by_approx(x, y, approx, k = 20):
    xpeak = []
    for i in range(len(approx)):
        bla = AM.getmax(x[approx[i] - k : approx[i] + k], (-1)**(i+1) * y[approx[i] - k : approx[i] + k])
        xpeak.append(bla)
    return xpeak