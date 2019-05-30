import numpy as np
import matplotlib.pyplot as plt


def temp_kalibration(R):
    T_1, T_2 = 293.65, 77
    R_1, R_2 = 107.9, 20.3
    sig_T = 1./np.sqrt(12)
    sig_R = 1./np.sqrt(12)

    a = (T_2 - T_1)/(R_2 - R_1)
    b = T_1 - a * R_1
    sig_a = a * np.sqrt(2 * sig_T**2/(T_2 - T_1)**2 + 2 * sig_R**2/(R_2 - R_1)**2)
    sig_b = np.sqrt(sig_T**2 + (a * sig_R)**2 + + (sig_a * R_1)**2)

    T_out = a * R + b
    sig_T_out = np.sqrt(sig_b**2 + (sig_a * R)**2 + (sig_R * a)**2)
    return T_out, sig_T_out

if __name__ == '__main__':

    T_1, T_2 = 293.65, 77
    R_1, R_2 = 107.9, 20.3
    sig_T = 1./np.sqrt(12)
    sig_R = 1./np.sqrt(12)

    a = (T_2 - T_1)/(R_2 - R_1)
    b = T_1 - a * R_1
    sig_a = a * np.sqrt(2 * sig_T**2/(T_2 - T_1)**2 + 2 * sig_R**2/(R_2 - R_1)**2)
    sig_b = np.sqrt(sig_T**2 + (a * sig_R)**2 + + (sig_a * R_1)**2)
    print(a, sig_a)
    print(b, sig_b)

    lin = lambda x, a, b: a * x + b

    fig = plt.figure()
    plt.errorbar([R_1, R_2], [T_1, T_2], xerr = [sig_R, sig_R], yerr = [sig_T, sig_T], fmt = '.', color = 'b')
    plt.plot(np.array([R_1, R_2]), lin(np.array([R_1, R_2]), a, b), color = 'r')
    plt.xlabel('R [k$\Omega$]')
    plt.ylabel('T [K]')
    #plt.title('Snap-In Curve')
    plt.grid()
    plt.tight_layout()
    plt.savefig('../Protokoll/Bilder/Temp_kalibration.png')
    plt.close(fig)

