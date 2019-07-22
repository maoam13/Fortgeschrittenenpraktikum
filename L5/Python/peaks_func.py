import Praktikum as p
import os
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt


def Intensity_G(name):
    data = np.genfromtxt('../Daten/' + name, delimiter = '')
    G, D = peaks(name)
    start = G[0] - G[2]/2
    stop = G[0] + G[2]/2
    start_idx = near(data[:,0], start)
    stop_idx = near(data[:,0], stop)
    G_intensity = np.max(data[:,1][start_idx:stop_idx])
    return G_intensity

def near(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx
def lorentz(A,x):
    return A[0] + A[1]*A[3]/((x**2-A[2]**2)**2 + A[3]**2) + A[4]*x


def peaks(name):
    if not os.path.exists('../Protokoll/Bilder/Peak_fits/' + name.replace(' ', '_').split('/')[0]):
        os.makedirs('../Protokoll/Bilder/Peak_fits/' + name.replace(' ', '_').split('/')[0])
    
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 10}

    data = np.genfromtxt("../Daten/"+name, delimiter = '')
    x = data[:,0]
    y = data[:,1]
    dy = np.full(len(y),np.std(y[near(x,1750):near(x,2250)]))

    w = 1580
    d = 50
    a = near(x,w-d)
    b = near(x,w+d)
    w1 = x[np.argmax(y[a:b])+a]
    start = [850,10000000,w1,15000,1]
    fit = AM.fitte_bel_function(x[a:b],y[a:b],dy[a:b],lorentz,start)
    omega_G, sig_omega_G = fit[0][2],fit[1][2]
    #print(omega_G, sig_omega_G)

    draw = np.arange(w-d,w+d,0.0001)
    yfit = lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw
    halfmax = max(yfit)/2
    h1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
    h2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
    halfmax = max(yfit)/2-max(dy)
    dh1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
    dh2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
    gamma_G, sig_gamma_G = h2-h1, 10*np.abs((dh2-dh1)-(h2-h1))
    #print(gamma_G, sig_gamma_G)

    fig = plt.figure()
    plt.rc('font', **font)
    plt.xlabel('Raman shift [cm$^{-1}$]', **font)
    plt.ylabel('Intensity [a.u.]', **font)
    plt.plot(x,y-fit[0][0]-fit[0][4]*x)
    plt.plot(draw,lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw)
    plt.plot([h1,h2],[halfmax,halfmax])
    plt.grid()
    plt.tight_layout()
    #plt.savefig('test1.png')
    plt.savefig('../Protokoll/Bilder/Peak_fits/' + name.replace(' ', '_').split('/')[0] + '/' + name.split('/')[1].split('.')[0] + '_G.png')
    plt.close(fig)

    w = 2680
    d = 120
    a = near(x,w-d)
    b = near(x,w+d)
    w1 = x[np.argmax(y[a:b])+a]
    start = [850,10000000,w1,15000,1]
    fit = AM.fitte_bel_function(x[a:b],y[a:b],dy[a:b],lorentz,start)
    omega_2D, sig_omega_2D = fit[0][2],fit[1][2]
    #print(omega_2D, sig_omega_2D)

    draw = np.arange(w-d,w+d,0.0001)
    yfit = lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw
    halfmax = max(yfit)/2
    h1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
    h2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
    halfmax = max(yfit)/2-max(dy)
    dh1 = draw[near(yfit[:np.argmax(yfit)],halfmax)]
    dh2 = draw[near(yfit[np.argmax(yfit):],halfmax)+np.argmax(yfit)]
    gamma_2D, sig_gamma_2D = h2-h1, 2*np.abs((dh2-dh1)-(h2-h1))
    #print(gamma_2D, sig_gamma_2D)
    
    fig = plt.figure()
    plt.rc('font', **font)
    plt.xlabel('Raman shift [cm$^{-1}$]', **font)
    plt.ylabel('Intensity [a.u.]', **font)
    plt.plot(x,y-fit[0][0]-fit[0][4]*x)
    plt.plot([h1,h2],[halfmax,halfmax])
    plt.plot(draw,lorentz(fit[0],draw)-fit[0][0]-fit[0][4]*draw)
    plt.grid()
    plt.tight_layout()
    #plt.savefig('test2.png')
    plt.savefig('../Protokoll/Bilder/Peak_fits/' + name.replace(' ', '_').split('/')[0] + '/' + name.split('/')[1].split('.')[0] + '_2D.png')
    plt.close(fig)
    return [omega_G, sig_omega_G, gamma_G, sig_gamma_G], [omega_2D, sig_omega_2D, gamma_2D, sig_gamma_2D]

if __name__ == '__main__':
    name = "2 mono bi tri flake/1.txt"
    G, D = peaks(name)
    print(G)
    print(D)
    