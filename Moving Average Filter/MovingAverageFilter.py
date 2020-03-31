# Two different approaches can be used, in this code they are MovAvgFilter and MovAvgFilter2
# This is exactly they same alogorithm as written by Phil Kim in his book 'Kalman Filter'. He wrote his code
# in Matlab while I converted this for my project to Python.
# The sample data is in txt file named 'sonarAlt.txt' This exact same data can be found in his Github repository as
# well.

import numpy as np
import matplotlib.pyplot as plt

firstRun =  []
firstRun1 = []
file = open('sonarAlt.txt','r')

# def MovAvgFilter(x):
#     x = float(x)
#     global prevAvg
#     global n1
#     global xbuf1
#     
#     if not firstRun1:
#         n1 = 10
#         xbuf1 = x*np.ones(n1+1)
#         k = 1
#         prevAvg = x
#         firstRun1.append(1)
#     
#     for m in range(0,n1-1):
#         xbuf1[m] = xbuf1[m+1]
#         
#     xbuf1[n1-1] = x
#     
#     avg = prevAvg + (x - xbuf1[0])/n1
#     prevAvg = avg
#     return avg
        
def MovAvgFilter2(x):
    x = float(x)
    global n
    global xbuf
    if not firstRun:
        n = 10
        xbuf = x*np.ones(n)
        firstRun.append(1)
    for m in range(0,n-1):
        xbuf[m] = xbuf[m+1]
    xbuf[n-1] = x
    avg = np.sum(xbuf) / n
    
    return avg


def GetSonar():
    line = file.readline()
    return int(float(line))

Nsamples = 500
Xsaved   = []
Xmsaved  = []

for k in range(1,Nsamples):
    xm = GetSonar()
    x  = MovAvgFilter2(xm)
    Xsaved.append(x)
    Xmsaved.append(xm)
 
    
dt = 0.02
t  = np.arange(0,Nsamples*dt-dt,dt)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(Xmsaved,'r.')
ax1.plot(Xsaved,'b')
ax1.set_xlabel('Time[sec]')
ax1.set_ylabel('Altitude[m]')
plt.show()

