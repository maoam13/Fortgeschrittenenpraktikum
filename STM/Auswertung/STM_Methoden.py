# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 16:34:19 2018

@author: grldm
"""

import numpy as np
import auswertung_nur_Methoden as AM
import Praktikum as p

def addiere_abstaende(data):
    summe = 0
    for i in range(len(data[:,1]) - 1):
        summe += np.abs(data[i][1] - data[i+1][1])
    return summe/(len(data[:,1]) - 1)

def lese_Profillinie_ein_IGain(IGain, vor = 1, alt = 0, Strom = 0):
    if Strom == 0:
        if alt == 1:
            if vor == 1:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_alt_vor.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_alt_nach.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
        else:
            if vor == 1:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_vor.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_nach.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
    else:
        if alt == 1:
            if vor == 1:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_alt_vor_Strom.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_alt_nach_Strom.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
        else:
            if vor == 1:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_vor_Strom.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/IGain/{0:1.0f}_nach_Strom.prf.cur".format(IGain), delimiter = ' ', skip_header = 127)

def lese_Profillinie_ein_Zeit(Zeit, vor = 1, alt = 0, Strom = 0):
    if Strom == 0:
        if alt == 1:
            if vor == 1:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_alt_vor.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_alt_nach.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)
        else:
            if vor == 1:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_vor.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_nach.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)
    else:
        if alt == 1:
            if vor == 1:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_alt_vor_Strom.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_alt_nach_Strom.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)
        else:
            if vor == 1:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_vor_Strom.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)
            else:
                return np.genfromtxt("Profillinien/Zeit/{0:1.0f}_nach_Strom.prf.cur".format(Zeit), delimiter = ' ', skip_header = 127)

def lese_Profillinie_ein_Kante(Kante, vor = 1, alt = 0):
    if vor == 1:
        if Kante / 1000 == 0:
            return np.genfromtxt("Profillinien/Kante/neu8000/0{0:1.0f}_vor.prf.cur".format(Kante), delimiter = ' ', skip_header = 127)
        else:
            return np.genfromtxt("Profillinien/Kante/neu8000/{0:1.0f}_vor.prf.cur".format(Kante), delimiter = ' ', skip_header = 127)
    else:
        if Kante / 1000 == 0:
            return np.genfromtxt("Profillinien/Kante/neu8000/0{0:1.0f}_nach.prf.cur".format(Kante), delimiter = ' ', skip_header = 127)
        else:
            return np.genfromtxt("Profillinien/Kante/neu8000/{0:1.0f}_nach.prf.cur".format(Kante), delimiter = ' ', skip_header = 127)

#def get_peak_by_approx(x, y, approx, k = 6):
#    xpeak = []
#    for i in range(len(approx)):
#        bla = p.peak(x, (-1)**(i+1) * y, x[approx[i] - k], x[approx[i] + k])
#        xpeak.append(bla)
#    return xpeak

def get_peak_by_approx(x, y, approx, k = 44):
    xpeak = []
    for i in range(len(approx)):
        bla = AM.getmax(x[approx[i] - k : approx[i] + k], (-1)**(i+1) * y[approx[i] - k : approx[i] + k])
        xpeak.append([bla[0], (-1)**(i+1) * bla[1], bla[2]])
    return xpeak

def steigung_bestimmen(peaks_nach, peaks_vor):
    #gibt die Flankensteigung zwischen minimum und maximum als Mittelwert zwischen Vor- und Rückrichtung zurück
    steigung_nach = []
    steigung_vor = []
    for i in range(len(peaks_nach)):
        st = (peaks_nach[i][1][1] - peaks_nach[i][0][1])/(peaks_nach[i][1][0] - peaks_nach[i][0][0])
        steigung_nach.append(st)
        st = (peaks_vor[i][1][1] - peaks_vor[i][0][1])/(peaks_vor[i][1][0] - peaks_vor[i][0][0])
        steigung_vor.append(st)

    steigung = []
    for i in range(len(steigung_vor)):
        steigung.append((steigung_vor[i] + steigung_nach[i])/2)
    return steigung

def peak_abstaende(peaks_nach, peaks_vor):
    if len(peaks_nach) != len(peaks_vor):
        return 0
    rueck = []
    for i in range(len(peaks_nach)):
        summe = np.abs(peaks_vor[i][0][0] - peaks_nach[i][0][0])
        summe += np.abs(peaks_vor[i][1][0] - peaks_nach[i][1][0])
        rueck.append(summe)
    return rueck

def alt_steigung(peak_vor_x, peak_vor_y, peak_nach_x, peak_nach_y, std = 0.1/np.sqrt(12)):
    steigung = []
    steigung_std = []
    steigung_vor = []
    steigung_vor_std = []
    steigung_nach = []
    steigung_nach_std = []
    steigung_mw = []
    steigung_mw_std = []
    for i in range(len(peak_vor_x)):
        st_nach = (peak_nach_y[i][1] - peak_nach_y[i][0])/(peak_nach_x[i][1] - peak_nach_x[i][0])
        st_vor = (peak_vor_y[i][1] - peak_vor_y[i][0])/(peak_vor_x[i][1] - peak_vor_x[i][0])
        st_nach_std = std * np.sqrt(2 * (1/(peak_nach_x[i][1] - peak_nach_x[i][0]))**2 + 2 * ((peak_nach_y[i][1] - peak_nach_y[i][0])/(peak_nach_x[i][1] - peak_nach_x[i][0])**2)**2)
        st_vor_std = std * np.sqrt(2 * (1/(peak_vor_x[i][1] - peak_vor_x[i][0]))**2 + 2 * ((peak_vor_y[i][1] - peak_vor_y[i][0])/(peak_vor_x[i][1] - peak_vor_x[i][0])**2)**2)
        steigung_vor.append(st_vor)
        steigung_vor_std.append(st_vor_std)
        steigung_nach.append(st_nach)
        steigung_nach_std.append(st_nach_std)
        steigung.append((st_nach + st_vor)/2)
        steigung_std.append(0.5 * np.sqrt(st_nach_std**2 + st_vor_std**2))
    
    peak_d_x = (peak_vor_x[i][0] + peak_nach_x[i][0])/2
    peak_d_y = (peak_vor_y[i][0] + peak_nach_y[i][0])/2
    peak_u_x = (peak_vor_x[i][1] + peak_nach_x[i][1])/2
    peak_u_y = (peak_vor_y[i][1] + peak_nach_y[i][1])/2
    peak_std = std * 1./np.sqrt(2)
    st_std = peak_std * np.sqrt(2 * (1/(peak_u_x - peak_d_x))**2 + 2 * ((peak_u_y - peak_d_y)/(peak_u_x - peak_d_x)**2)**2)
    steigung_mw.append((peak_u_y - peak_d_y)/(peak_u_x - peak_d_x))
    steigung_mw_std.append(st_std)
    return steigung_vor, steigung_nach, steigung_vor_std, steigung_nach_std

def multi_lin_reg(data_nach, data_vor, vor_kante_vor, nach_kante_vor, vor_kante_nach, nach_kante_nach, sig_x, sig_y):
    vor_sol_vor = []
    nach_sol_vor = []
    vor_sol_nach = []
    nach_sol_nach = []
    for i in range(len(data_vor)):
        #Daten für linreg bei vorwaertsrichtung
        vor_data_nachkante = data_vor[i][nach_kante_vor[i]:-1]
        vor_data_vorkante = data_vor[i][0:vor_kante_vor[i]]
        vor_std_x_nach = np.full(len(vor_data_nachkante), sig_x)
        vor_std_y_nach = np.full(len(vor_data_nachkante), sig_y)
        vor_std_x_vor = np.full(vor_kante_vor[i], sig_x)
        vor_std_y_vor = np.full(vor_kante_vor[i], sig_y)
        #Daten für linreg bei rueckwaertsrichtung
        nach_data_nachkante = data_nach[i][nach_kante_nach[i]:-1]
        nach_data_vorkante = data_nach[i][0:vor_kante_nach[i]]
        nach_std_x_nach = np.full(len(nach_data_nachkante), sig_x)
        nach_std_y_nach = np.full(len(nach_data_nachkante), sig_y)
        nach_std_x_vor = np.full(vor_kante_nach[i], sig_x)
        nach_std_y_vor = np.full(vor_kante_nach[i], sig_y)
        vor_sol_vor.append(p.lineare_regression_xy(vor_data_vorkante[:,0], vor_data_vorkante[:,1], vor_std_x_vor, vor_std_y_vor))
        nach_sol_vor.append(p.lineare_regression_xy(vor_data_nachkante[:,0], vor_data_nachkante[:,1], vor_std_x_nach, vor_std_y_nach))
        vor_sol_nach.append(p.lineare_regression_xy(nach_data_vorkante[:,0], nach_data_vorkante[:,1], nach_std_x_vor, nach_std_y_vor))
        nach_sol_nach.append(p.lineare_regression_xy(nach_data_nachkante[:,0], nach_data_nachkante[:,1], nach_std_x_nach, nach_std_y_nach))
    return np.array(vor_sol_vor), np.array(nach_sol_vor), np.array(vor_sol_nach), np.array(nach_sol_nach)

def verschiebemethode(nach_sol, vor_sol, data, kante):
    h = []
    nach_steigung_var = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1]
    vor_steigung_var = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
    nach_abschnitt_var = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]
    vor_abschnitt_var = [1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1]
    for i in range(len(nach_steigung_var)):
        a_nach = nach_sol[:,0] + nach_steigung_var[i] * nach_sol[:,1]
        a_vor = vor_sol[:,0] + vor_steigung_var[i] * vor_sol[:,1]
        b_nach = nach_sol[:,2] + nach_abschnitt_var[i] * nach_sol[:,3]
        b_vor = vor_sol[:,2] + vor_abschnitt_var[i] * vor_sol[:,3]
        a_k_nach = -1./a_nach
        b_k = []
        for i in range(len(a_k_nach)):
            b_k.append(data[i][kante[i]][1] - a_k_nach[i] * data[i][kante[i]][0])
        b_k = np.array(b_k)
        x1_nach = (b_k - b_nach)/(a_nach - a_k_nach)
        x2_nach = (b_k - b_vor)/(a_vor - a_k_nach)
        y1_nach = a_k_nach * x1_nach + b_k
        y2_nach = a_k_nach * x2_nach + b_k
        h.append(np.sqrt((x1_nach - x2_nach)**2 + (y1_nach - y2_nach)**2))
    return np.array(h)