import Praktikum as p
import os
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import peaks_func as pf


def doping_strain(x_test, y_test, x = 1582, y = 2677, m_1 = 2.2, m_2 = 0.7):
    b_1 = y - m_1 * x
    b_2 = y - m_2 * x
    
    b_test = y_test - m_1 * x_test
    x_schnitt, y_schnitt = AM.geraden_schnittpunkte(m_1, b_test, m_2, b_2)
    doping = np.sign(x_schnitt - x) * np.sqrt((x - x_schnitt)**2 + (y - y_schnitt)**2)

    b_test = y_test - m_2 * x_test
    x_schnitt, y_schnitt = AM.geraden_schnittpunkte(m_1, b_1, m_2, b_test)
    strain = np.sign(x_schnitt - x) * np.sqrt((x - x_schnitt)**2 + (y - y_schnitt)**2)
    
    return doping, strain


if __name__ == '__main__':
    #Beispielpunkt für den Strain und Doping berechnet werden soll
    x_test, y_test = 1640, 2840

    #Steigungen der Geraden wie angegeben
    m_1 = 2.2
    m_2 = 0.7

    #Schnittpunkt der Geraden (erstmal abgelesen)
    x, y = 1582, 2677

    #berechne Y-Achsenabschnitt der Geraden
    b_1 = y - m_1 * x
    b_2 = y - m_2 * x

    #Berechne p-Doping durch Verschieben der Geraden mit größerer Steigung in den Messpunkt und Bestimmung des Schnittpunktes mit der anderen, unverschobenen Geraden
    b_test = y_test - m_1 * x_test
    x_schnitt, y_schnitt = AM.geraden_schnittpunkte(m_1, b_test, m_2, b_2)
    doping = np.sign(x_schnitt - x) * np.sqrt((x - x_schnitt)**2 + (y - y_schnitt)**2)
    print(doping)

    #Berechne Strain durch Verschieben der Geraden mit kleinerer Steigung in den Messpunkt und Bestimmung des Schnittpunktes mit der anderen, unverschobenen Geraden
    b_test = y_test - m_2 * x_test
    x_schnitt, y_schnitt = AM.geraden_schnittpunkte(m_1, b_1, m_2, b_test)
    strain = np.sign(x_schnitt - x) * np.sqrt((x - x_schnitt)**2 + (y - y_schnitt)**2)
    print(strain)


    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

    plot = np.arange(1300, 1900, 0.1)

    fig = plt.figure()
    plt.rc('font', **font)
    plt.errorbar(x_test, y_test, fmt='.', color = 'b')
    plt.plot(plot, m_1 * plot + b_1, color = 'r')
    plt.plot(plot, m_2 * plot + b_2, color = 'r')
    plt.xlabel('$\omega _G$ [cm$^{-1}$]', **font)
    plt.ylabel('$\omega _{2D}$ [cm$^{-1}$]', **font)
    #plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig('test.png')
    #plt.savefig('../Protokoll/Bilder/Part_3/omega_2D_vs_G.png')
    plt.close(fig)

