# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:57:17 2018

@author: Gerald
"""

import numpy as np
import auswertung_nur_Methoden as AM
import scipy

def fft_cutoff(data):
    """returns abgeschn. Daten, orginal fft, abgeschn. fft"""
    fft = np.fft.fft(data)#fft
    fftoriginal = np.copy(fft)
    fft[600:] = 0#cutoff bei index 600 (nur alles unter 600 verwendet)
    datacutoff = np.fft.ifft(fft)#inverse fft
    return [datacutoff,fftoriginal,fft]

def KalibrationEinlesen(i):
    index = ["Ag", "Cu", "I", "StainlessSteel"]
    data = np.genfromtxt("../Daten/Roentgen/Kalibrierung_"+index[i]+"_5min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
    return data

def gauss(a,x):#einfache Gaussfunktion: Position in index 0, Höhe in 3
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))
def gauss2(a,x):#doppelte Gaussfunktion: Position in index 0 und 4. Höhe in 3 und 6
    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))

def peak_best(data, startwerte, p = 1, b1 = 20, b2 = 80):
    #startwerte = [position, breite, untergrund, höhe]
    k = startwerte[0]
    #def gauss(a,x):#einfache Gaussfunktion: Position in index 0, Höhe in 3
    #    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))
    #def gauss2(a,x):#doppelte Gaussfunktion: Position in index 0 und 4. Höhe in 3 und 6
    #    return a[2]+a[3]*np.exp(-(x-a[0])**2/(2*a[1]**2))+a[6]*np.exp(-(x-a[4])**2/(2*a[5]**2))
    x = np.arange(len(data))
    sx = np.full(len(x), 1./np.sqrt(12))
    sy = np.sqrt(data)
    if p == 1:
        sol1 = AM.fitte_bel_function(x[k-b1:k+b1], data[k-b1:k+b1], sx[k-b1:k+b1], sy[k-b1:k+b1], gauss, startwerte)
        sol2 = AM.fitte_bel_function(x[k-b2:k+b2], data[k-b2:k+b2], sx[k-b2:k+b2], sy[k-b2:k+b2], gauss, startwerte)
        chiq1, chiq2 = sol1[2], sol2[2]
        peak, sig = (sol1[0][0] + sol2[0][0])/2, np.abs(sol1[0][0] - sol2[0][0])
        return peak, sig, chiq1, chiq2, sol2
    if p == 2:
        sol1 = AM.fitte_bel_function(x[k-b1:k+b1], data[k-b1:k+b1], sx[k-b1:k+b1], sy[k-b1:k+b1], gauss2, startwerte)
        sol2 = AM.fitte_bel_function(x[k-b2:k+b2], data[k-b2:k+b2], sx[k-b2:k+b2], sy[k-b2:k+b2], gauss2, startwerte)
        chiq1, chiq2 = sol1[2], sol2[2]
        peak1, sig1 = (sol1[0][0] + sol2[0][0])/2, np.abs(sol1[0][0] - sol2[0][0])
        peak2, sig2 = (sol1[0][3] + sol2[0][3])/2, np.abs(sol1[0][3] - sol2[0][3])
        return peak1, sig1, peak2, sig2, chiq1, chiq2, sol2
    return 0

def fitte_bel_functionx(x, y, ex, func, startwerte):
    """gibt wert,fehler,chi/ndof zurueck"""
    model  = scipy.odr.Model(func)
    data   = scipy.odr.RealData(x, y, sx=ex)
    odr    = scipy.odr.ODR(data, model, beta0=startwerte)
    output = odr.run()
    return output.beta, output.sd_beta, output.res_var