# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:57:17 2018

@author: Gerald
"""

import numpy as np

def fft_cutoff(data):
    """returns abgeschn. Daten, orginal fft, abgeschn. fft"""
    fft = np.fft.fft(data)#fft
    fftoriginal = fft
    fft[600:] = 0#cutoff bei index 600 (nur alles unter 600 verwendet)
    datacutoff = np.fft.ifft(fft)#inverse fft
    return [datacutoff,fftoriginal,fft]

def KalibrationEinlesen(i):
    index = ["Ag", "Cu", "I"]
    data = np.genfromtxt("../Daten/Roentgen/Kalibrierung_"+index[i]+"_5min.mca", delimiter = ',', skip_header = 12, skip_footer = 71)
    return data