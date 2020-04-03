import numpy as np
import matplotlib.pyplot as plt

firstRun = []

def AvgFilter(x):
    global prevAvg
    global k
    
    
    if not firstRun:
        k = 1
        prevAvg = 0
        firstRun.append(1)
    
    alpha = (k-1)/k
    avg = alpha*prevAvg + (1-alpha)*x
    prevAvg = avg
    k = k+1
    return avg

def GetVolt():
    w = 0 + 4*np.random.randn(1)
    z = 14.3 + w
    return z

dt = 0.2
t = np.linspace(0,10,50)
Nsamples = len(t)
Avgsaved = []
Xmsaved  = []

for k in range(Nsamples):
    xm  = GetVolt()
    avg = AvgFilter(xm)
    
    Avgsaved.append(avg)
    Xmsaved.append(xm)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Time[sec]')
ax1.set_ylabel('Volt[V]')
ax1.set_title('Average Filter')
ax1.plot(t,Xmsaved,'r:*')
ax1.plot(t,Avgsaved,'o-')
plt.show()


    
