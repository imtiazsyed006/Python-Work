import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

firstRun = []
Pospp = []
def GetPos():
    global Posp
    global Velp
    if not Pospp:
        Pospp.append(1)
        Posp = 0
        Velp = 0
    dt = 0.1
    w = 0 + 10*np.random.randn()
    print(w)
    v = 0 + 10*np.random.randn()

    z = Posp + Velp*dt + v
    Posp = z - v
    Velp = 80 + w
    return z

def DvKalman(z):
    global A
    global x
    global P
    global H
    global R
    if not firstRun:
        firstRun.append(1)
        dt = 1
        A = [[1 , dt],
             [0 , 1]]
        H = [[1 , 0]]
        Q = [[1 , 0],
             [0 , 3]]
        R = 10
        x = [[0],
             [20]]
        A = np.array(A)
        H = np.array(H)
        Q = np.array(Q)
        R = np.array(R)
        x = np.array(x)
        P = 5*np.eye(2)
    xp = A.dot(x)
    Pp = A.dot(P)
    Pp = Pp.dot(A.transpose())
    H_t = H.transpose()
    sup = H.dot(Pp).dot(H_t) + R
    sup = inv(sup)
    K  = Pp.dot(H.transpose()).dot(sup)
    x  = xp + K.dot(z-H.dot(xp))
    P = Pp - K.dot(H).dot(Pp)
    pos = x[0][0]
    vel = x[1][0]
    return pos,vel



dt = 0.1
t = np.linspace(0,10,100)
Nsamples = len(t)
#Xsaved = np.zeros((Nsamples, 2))
#Zsaved = np.zeros((Nsamples, 1))
Xsaved = []
Zsaved = []


pos = []
vel = []
for i in range(0,Nsamples-1,1):
    z = GetPos()
    poss, vell = DvKalman(z)
    pos.append(poss)
    vel.append(vell)
    Zsaved.append(z)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(pos)
ax1.plot(Zsaved,'.')
ax2 = fig.add_subplot(212)
ax2.plot(vel)

plt.show()
    


    
