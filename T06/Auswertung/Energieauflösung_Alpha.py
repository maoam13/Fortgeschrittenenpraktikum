# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:35:46 2018

@author: Gerald
"""

import Praktikum as p
import numpy as np
import matplotlib.pyplot as plt
import auswertung_nur_Methoden as AM
import timeit
import Peak_Daten as pD

start_time=timeit.default_timer()

pos,dpos,h,dh,b,db = pD.peakdata()

E_pos = np.array(pos)
e_E_pos = np.array(dpos)
FWH = 2 * np.sqrt(2 * np.log(2)) * np.array(b)
e_FWH = 2 * np.sqrt(2 * np.log(2)) * np.array(db)

k = [4]
for i in range(len(k)):
    E_pos = AM.remelementfromarray(E_pos, k[i])
    e_E_pos = AM.remelementfromarray(e_E_pos, k[i])
    FWH = AM.remelementfromarray(FWH, k[i])
    e_FWH = AM.remelementfromarray(e_FWH, k[i])

####lin reg
sol = p.lineare_regression_xy(np.sqrt(E_pos),FWH,np.abs(e_E_pos /(2*np.sqrt(E_pos))),e_FWH)

#plotte lin reg
plt.close('all')
plt.figure(1)
ax1 = plt.subplot(211)
plt.errorbar(np.sqrt(E_pos), FWH, xerr = np.abs(e_E_pos /(2*np.sqrt(E_pos))), yerr = e_FWH, fmt = '.', color = 'b')
plt.plot(np.sqrt(E_pos), sol[0] * np.sqrt(E_pos) + sol[2], color = 'r')
plt.title('Energieaufloesung')
plt.xlabel('$\Delta$ E')
plt.figtext(0.15,0.7,
            'Model: y = a $\cdot$ x + b \n'
            +'a= ('+ str(np.round(sol[0],5)) + ' $\pm$ '+ str(np.round(sol[1],5)) + ') $\sqrt{eV}$ \n'
            +'b= ('+ str(np.round(sol[2],2)) + ' $\pm$ '+ str(np.round(sol[3],2)) + ') eV \n'
            +'$\chi ^2$/ndof= ' + str(np.round(sol[4], 2)))
ax2=plt.subplot(212,sharex=ax1)
H = np.full(len(np.sqrt(E_pos)), 0.5)
H_err = np.full(len(np.sqrt(E_pos)), 0.5)
for i in range(len(np.sqrt(E_pos))):
    H[i] = FWH[i] - sol[0] * np.sqrt(E_pos)[i] - sol[2]
    H_err[i] = np.sqrt((sol[0] * np.abs(e_E_pos[i] /(2*np.sqrt(E_pos[i]))))**2 + e_FWH[i]**2)
plt.errorbar(np.sqrt(E_pos), H, yerr = H_err, fmt = '.', color = 'b')
x_r = np.array([min(np.sqrt(E_pos)), max(np.sqrt(E_pos))])
y_r = np.array([0, 0])
plt.plot(x_r, y_r, color = 'r')
plt.ylabel('Residuen')
plt.xlabel('$\sqrt{E}$ [$\sqrt{eV}$]')

print("Laufzeit: {0:9.2f} Sekunden".format(timeit.default_timer()-start_time))