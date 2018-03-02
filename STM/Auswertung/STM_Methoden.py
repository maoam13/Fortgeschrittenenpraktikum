# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 16:34:19 2018

@author: grldm
"""

import numpy as np

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