import Praktikum as p
import os
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import peaks_func as pf


def doping_strain_official(omega_G, omega_D, m_1 = 2.2, m_2 = 0.7):
    omega_GP, omega_DP = 1581.6, 2676.9
    h_bar, v_F = 6.582 * 10**(-16), 1.15 * 10**6

    strain_fac = -23.5 #69.1

    x, y = omega_G - omega_GP, omega_D - omega_DP
    alpha, beta = np.arctan(m_2), np.arctan(m_1)
    
    omega_G_doping = np.cos(alpha) / np.sin(beta - alpha) * np.sin(beta) * x - np.cos(beta) * y
    omega_G_strain = - np.cos(beta) / np.sin(beta - alpha) * np.sin(alpha) * x - np.cos(alpha) * y

    doping = 10**(-12) / np.pi * (omega_G_doping / (42 * h_bar * v_F * 100))**2
    strain = omega_G_strain / strain_fac

    return doping, strain


def doping_strain(x_test, y_test, x = 1582, y = 2677, m_1 = 2.2, m_2 = 0.7): 
    h_bar, v_F = 6.582 * 10**(-16), 1.15 * 10**6
    strain_fac = -23.5

    b_1 = y - m_1 * x
    b_2 = y - m_2 * x
    
    b_test = y_test - m_1 * x_test
    x_schnitt, y_schnitt = AM.geraden_schnittpunkte(m_1, b_test, m_2, b_2)
    omega_G_doping = np.sign(x_schnitt - x) * np.sqrt((x - x_schnitt)**2 + (y - y_schnitt)**2)

    b_test = y_test - m_2 * x_test
    x_schnitt, y_schnitt = AM.geraden_schnittpunkte(m_1, b_1, m_2, b_test)
    omega_G_strain = np.sign(x_schnitt - x) * np.sqrt((x - x_schnitt)**2 + (y - y_schnitt)**2)

    doping = 10**(-12) / np.pi * (omega_G_doping / (42 * h_bar * v_F * 100))**2
    strain = omega_G_strain / strain_fac
    
    return doping, strain


def print_table(data, transpose = False, printout = True):
    if transpose:
        ausgabe = ''
        for i in range(np.shape(data)[1]):
            ausgabe += str(data[0][i])
            for j in range(1, np.shape(data)[0]):
                ausgabe += ' & ' + str(data[j][i])
            ausgabe += '\n'
    else:
        ausgabe = ''
        for i in range(np.shape(data)[0]):
            ausgabe += str(data[i][0])
            for j in range(1, np.shape(data)[1]):
                ausgabe += ' & ' + str(data[i][j])
            ausgabe += '\n'
    if printout:
        print(ausgabe)
    return ausgabe


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

