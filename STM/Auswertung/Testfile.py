# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 11:38:33 2018

@author: Gerald
"""
import numpy as np

IGain = 1

if IGain:
    data_index = [1, 3, 8, 11]
    peak_vor_x = [[23.4, 50.1], [36.5, 48.2], [31.5, 45.9], [30.8, 48.6]]
    peak_vor_y = [[0.0, 3.4], [0.0, 2.4], [0.0, 4.4], [0.0, 8.3]]
    peak_nach_x = [[27.5, 44.7], [32.7, 44.7], [28.0, 44.0], [30.8, 41.4]]
    peak_nach_y = [[0.0, 2.9], [0.0, 2.6], [0.1, 3.5], [0.0, 9.4]]

if IGain == 0: #Zeitvariation
    data_index = [52, 80, 100, 200, 400, 600, 2000]
    peak_vor_x = [[33.0, 51.1], [22.2, 54.8], [38.6, 54.2], [18.7, 53.8], [36.5, 53.1], [27.6, 52.7], [43.6, 62.8]]
    peak_vor_y = [[0.0, 3.5], [0.0, 3.6], [0.0, 3.4], [0.0, 4.2], [0.0, 3.1], [0.0, 3.4], [0.0, 3.1]]
    peak_nach_x = [[28.5, 45.3], [20.2, 46.0], [35.2, 50.9], [15.5, 48.4], [33.6, 50.7], [24.6, 48.6], [38.8, 57.0]]
    peak_nach_y = [[0.0, 3.4], [0.0, 3.5], [0.0, 3.7], [0.0, 4.2], [0.0, 3.5], [0.0, 3.3], [0.0, 2.7]]

std = 0.1/np.sqrt(12)

#Steigung
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

steigung_rel_std = np.array(steigung_std)/np.array(steigung)
steigung_mw_rel_std = np.array(steigung_mw_std)/np.array(steigung_mw)

print np.array(steigung_vor) - np.array(steigung_nach), '\n'

print steigung_nach
print steigung_vor
print steigung_nach_std
print steigung_vor_std