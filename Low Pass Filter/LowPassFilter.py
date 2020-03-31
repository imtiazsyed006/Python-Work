# Change alpha and observe the change

import numpy as np
import matplotlib.pyplot as plt

file = open('sonarAlt.txt','r')
firstRun = []

def LPF(x):
    global prevX
    x = float(x)
    
    if not firstRun:
        prevX = x
        firstRun.append(1)
    
    alpha = 0.9
    xlpf = alpha*prevX + (1 - alpha)*x
    prevX = xlpf
    
    return xlpf

def GetSonar():
    line = file.readline()
    return int(float(line))

Nsamples = 1000
Xsaved = []
Xmsaved = []

for k in range(0,Nsamples-1):
    xm = GetSonar()
    x = LPF(xm)
    
    Xsaved.append(x)
    Xmsaved.append(xm)

dt = 0.02
t = np.arange(0,Nsamples*dt-dt,dt)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(Xmsaved,'r.')
ax1.plot(Xsaved,'b')
ax1.set_xlabel('Time[sec]')
ax1.set_ylabel('Altitude[m]')
plt.show()



plt.show()


        
    