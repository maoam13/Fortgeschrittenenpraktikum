import Praktikummo as p
import numpy as np
import matplotlib.pyplot as plt
import Data as data
import Kalibration_Methode as kal
import scipy.constants as s

ein = data.Spektrum("Hyperfein messung 18h.ws5")

y = ein.x[:1024]
x = np.arange(0,1024,1)
err = np.sqrt(y)
E = kal.Kalibration(3)[0]-14.4*10**12
dE = kal.Kalibration(3)[1]
v = kal.Kalibration(3)[2]
dv = kal.Kalibration(3)[3]
off = 0

if 1:
    y = y[:512]
    x = x[:512]
    err = err[:512]
    E = E[:512]
    v = v[:512]
    dE = dE[:512]
    dv = dv[:512]
    p1 = 79
    p2 = 166
    p3 = 230
    p4 = 274
    p5 = 337
    p6 = 418
else:
    k = -1
    ver = 512
    p1 = 942
    p2 = 855
    p3 = 792
    p4 = 748
    p5 = 685
    p6 = 601
    off = 520
    off2 = 10
    
#if ver != 0:
#    y = y[512:]
#    x = x[512:]
#    err = err[512:]
 #   E = E[512:]
  #  dE = dE[512:]
  #  v = v[512:]
 #   dv = dv[512:]
    
my = np.concatenate((y[115+off2:140+off2],y[190+off2:210+off2]))
my = np.concatenate((my,y[291+off2:315+off2]))
my = np.concatenate((my,y[356+off2:380+off2]))
mittel = np.mean(my)
print mittel
std = np.std(my)
fehler = np.std(my)/len(my)
print fehler

Int1 = 0
for i in range(100):
    Int1 = Int1 + (-y[p1-50+i]+mittel)*(abs(E[p1-50+i+1]-E[p1-50+i]))
print (-y[p1-50+50]+mittel)*(abs(E[p1-50+50+1]-E[p1-50+50]))

b2 = 30
Int2 = 0
for i in range(100):
    Int2 = Int2+ (-y[p2-b2+i]+mittel)*(E[p2-b2+i+1]-E[p2-b2+i])
print Int2

b2 = 30
Int2 = 0
for i in range(100):
    Int2 = Int2+ (-y[p2-b2+i]+mittel)*(E[p2-b2+i+1]-E[p2-b2+i])
print Int2

plt.figure(4)
ax = plt.subplot(211)
ax.set_title("Einlinienspektrum")
ax.set_xlabel("Channel")
ax.set_ylabel("Counts")
plt.plot(x,y)
axen =[plt.xlim()[0],plt.xlim()[1],plt.ylim()[0],plt.ylim()[1]]
plt.axis(axen)
plt.vlines(p1-50+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(p1+50+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'g')
plt.vlines(p2-b2+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(p2+b2+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'g')
plt.vlines(p3-50+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(p3+50+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'g')
plt.vlines(p4-50+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'r')
plt.vlines(p4+50+off,plt.ylim()[0],plt.ylim()[1],linestyle="--",color = 'g')
    