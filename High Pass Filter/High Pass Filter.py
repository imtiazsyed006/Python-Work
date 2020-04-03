# The Algorithm used is in this code is taken from Phil Kim, "Kalman Filter for Beginner". His code is written in Matlab, so
# I converted that code to Python

import numpy as np
import matplotlib.pyplot as plt
file     = open('sonarAlt.txt','r')
firstRun = []


def HPF(u):
    
    global prevX
    global prevU
    global dt
    global tau
    
    
    if not firstRun:
        prevX = 0
        prevU = 0
        dt    = 0.01
        tau   = 0.0233
        
        firstRun.append(1)
    
    alpha = tau/(tau + dt)
    xhpf  = alpha*prevX + alpha*(u - prevU)
    
    prevX = xhpf

    prevU = u
    
    return xhpf

def GetSonar():
    line = file.readline()
    return int(float(line))

Nsamples = 500
Xsaved   = np.zeros((Nsamples-1,1))
Xmsaved  = np.zeros((Nsamples-1,1))

for k in range(0,Nsamples-1):
    zm = GetSonar()
    x  = HPF(zm)
    
    Xsaved[k,0]  = x
    Xmsaved[k,0] = zm
    
dt = 0.02
t  = np.arange(0,(Nsamples)*dt-dt,dt)

figure_1 = plt.figure()
ax1      = figure_1.add_subplot(111)

ax1.plot ( t, Xmsaved,'r.')  # Both Xmsaved[:,0] and Xmsaved can be used 
ax1.plot ( t, Xsaved, 'b' )

figure_2 = plt.figure()
ax2      = figure_2.add_subplot(111)

ax2.plot( t, Xmsaved,     'r.')
ax2.plot(t, Xmsaved-Xsaved,'b')

plt.show()

