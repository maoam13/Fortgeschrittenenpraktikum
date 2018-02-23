# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:03:25 2018

@author: Gerald
"""
import numpy as np
import scipy.odr


def Offset_Rauschen():
    data = np.genfromtxt("Rauschmessung.txt", delimiter = ',')
    return np.mean(data[:,4]), np.std(data[:,4], ddof = 1)

def Rohdaten(offset, sig_U, sig_tau, j):
    rohdata = np.genfromtxt("T1 alle Daten.txt", delimiter = ',')
    tau = np.genfromtxt("T1 tau Vermutung.txt", delimiter = ',')
    
    data = []
    for i in range(0, len(rohdata) - 4):
        t = (tau[i][2] - tau[i][1]) * 45/2500
        if i < 38:
            sig_t = sig_tau * np.sqrt(2)
        else:
            sig_t = 5 * sig_tau * np.sqrt(2)
        if i < j:
            U_rel = -(rohdata[i][2] * 10**(-5) - offset) / (rohdata[i][1] * 10**(-5) - offset)
        else:
            U_rel = (rohdata[i][2] * 10**(-5) - offset) / (rohdata[i][1] * 10**(-5) - offset)
        #bla = np.sqrt((1/(rohdata[i][1] - offset))**2 + ((rohdata[i][2] - offset)/(rohdata[i][1] - offset)**2)**2)
        sig_U_rel = np.sqrt((sig_U/(rohdata[i][1] - offset))**2 + (sig_U * (rohdata[i][2] - offset)/(rohdata[i][1] - offset)**2)**2)
        #print sig_U, bla, sig_U_rel
        data.append([t, U_rel, sig_t, sig_U_rel])
    return np.array(data) 

def fitte_bel_function(x, y, ex, ey, func, startwerte):
    model  = scipy.odr.Model(func)
    data   = scipy.odr.RealData(x, y, sx=ex, sy=ey)
    odr    = scipy.odr.ODR(data, model, beta0=startwerte)
    output = odr.run()
    return output.beta, output.sd_beta, output.res_var
    
