# Autho: Syed Imtiaz Ali Shah
# Got help from https://stackoverflow.com/a/4098938

import numpy as np
import matplotlib.pyplot as plt
import math

xp = 1
yp =  3
xpp = 0
ypp = 0
k = 0
d = 4
l1 = 2.5
l2 = 4.0
l3 = 4.0/2
l4 = 2.5
l5 = 4.0/2

CosTh_5 = (xp**2 + yp**2 - l4**2 - l5**2)/(2*l4*l5)
SinTh_5 = -math.sqrt(1-CosTh_5**2)
Th_5 = math.atan2(SinTh_5,CosTh_5)
Th_5*180/3.14

k1 = l4 + l5*CosTh_5
k2 = l5*SinTh_5
Th_4 = math.atan2(yp,xp) - math.atan2(k2,k1)
Th_4*180/3.14
x4 = 0
y4 = 0.0

x5 = l4*math.cos(Th_4)
y5 = l4*math.sin(Th_4)

x6 = x5 + l5*math.cos(Th_5 + Th_4)
y6 = y5 + l5*math.sin(Th_5 + Th_4)

X4 = [x4,x5]
Y4 = [y4,y5]

X5 = [x5,x6]
Y5 = [y5,y6]

SinTh_5 = math.sqrt(1-CosTh_5**2)
Th_5 = math.atan2(SinTh_5,CosTh_5)
Th_5*180/3.14

Phi = Th_4 + math.pi - Th_5
CosTh_2 = ((xp - l3*math.cos(Phi) - d)**2 + (yp - l3*math.sin(Phi))**2 -l1**2-l2**2)/(2*l1*l2)
SinTh_2 = math.sqrt(1-CosTh_2**2)

Th_2 = math.atan2(SinTh_2,CosTh_2)
Th_2*180/3.14

k3 = l1 + l2*CosTh_2
k4 = l2*SinTh_2
Th_1 = math.atan2(yp - l3*math.sin(Phi),xp - l3*math.cos(Phi) - d) - math.atan2(k4,k3)
Th_1*180/3.14
Th_3 = Phi  - Th_1 - Th_2
Th_3*180/3.14

x = [0,4,4,0]
y = [0,0,0.01,0.01]

x0 = d
y0 = 0.0

x1 = d+l1*math.cos(Th_1)
y1 = l1*math.sin(Th_1)

x2 = x1 + l2*math.cos(Th_1+Th_2)
y2 = y1 + l2*math.sin(Th_1+Th_2)

x3 = x2 + l3*math.cos(Phi)
y3 = y2 + l3*math.sin(Phi)



X1 = [x0,x1]
Y1 = [y0,y1]

X2 = [x1,x2]
Y2 = [y1,y2]

X3 = [x2,x3]
Y3 = [y2,y3]

plt.ion()
fig = plt.figure()
ax = fig.add_subplot()
ax.axis('equal')
ax.set(xlim=(-3, 7), ylim=(-3, 7))

p1, = ax.plot(x,y,LineWidth = 5, color = 'black')
p2, = ax.plot(X1,Y1,LineWidth = 3,color = 'green')
p3, = ax.plot(X2,Y2,LineWidth = 3,color = 'green')
p4, = ax.plot(X3,Y3,LineWidth = 3,color = 'green')
p5, = ax.plot(X4,Y4,LineWidth = 3,color = 'red')
p6, = ax.plot(X5,Y5,LineWidth = 3,color = 'red')
p7, = ax.plot(x3,y3,'s',LineWidth = 3, MarkerFaceColor = 'r', MarkerSize = 8, MarkerEdgeColor = 'r')
p8, = ax.plot(x0,y0,'o',LineWidth = 3, MarkerFaceColor = 'r', MarkerSize = 8, MarkerEdgeColor = 'r')
p9, = ax.plot(x2,y2,'o',LineWidth = 3, MarkerFaceColor = 'r', MarkerSize = 8, MarkerEdgeColor = 'r')
p10, = ax.plot(x4,y4,'o',LineWidth = 3, MarkerFaceColor = 'black', MarkerSize = 8, MarkerEdgeColor = 'black')
p11, = ax.plot(x5,y5,'o',LineWidth = 3, MarkerFaceColor = 'black', MarkerSize = 8, MarkerEdgeColor = 'black')
p12, = ax.plot(x1,y1,'o',LineWidth = 3, MarkerFaceColor = 'r', MarkerSize = 8, MarkerEdgeColor = 'r')


for i in np.arange(0,2*math.pi,0.2):
    xp = 1 + math.cos(i)
    yp = 3 + math.sin(i)
    
    
    k = k + 1
    CosTh_5 = (xp**2 + yp**2 - l4**2 - l5**2)/(2*l4*l5)

    SinTh_5 = -math.sqrt(1-CosTh_5**2)
    Th_5 = math.atan2(SinTh_5,CosTh_5)
    Th_5*180/3.14

    k1 = l4 + l5*CosTh_5
    k2 = l5*SinTh_5
    Th_4 = math.atan2(yp,xp) - math.atan2(k2,k1)
    Th_4*180/3.14
    x4 = 0
    y4 = 0.0

    x5 = l4*math.cos(Th_4)
    y5 = l4*math.sin(Th_4)

    x6 = x5 + l5*math.cos(Th_5 + Th_4)
    y6 = y5 + l5*math.sin(Th_5 + Th_4)

    X4 = [x4,x5]
    Y4 = [y4,y5]

    X5 = [x5,x6]
    Y5 = [y5,y6]

    SinTh_5 = math.sqrt(1-CosTh_5**2)
    Th_5 = math.atan2(SinTh_5,CosTh_5)
    Th_5*180/3.14

    Phi = Th_4 + math.pi - Th_5
    CosTh_2 = ((xp - l3*math.cos(Phi) - d)**2 + (yp - l3*math.sin(Phi))**2 -l1**2-l2**2)/(2*l1*l2)
    SinTh_2 = math.sqrt(1-CosTh_2**2)

    Th_2 = math.atan2(SinTh_2,CosTh_2)
    Th_2*180/3.14

    k3 = l1 + l2*CosTh_2
    k4 = l2*SinTh_2
    Th_1 = math.atan2(yp - l3*math.sin(Phi),xp - l3*math.cos(Phi) - d) - math.atan2(k4,k3)
    Th_1*180/3.14
    Th_3 = Phi  - Th_1 - Th_2
    Th_3*180/3.14

    x = [0,4,4,0]
    y = [0,0,0.01,0.01]

    x0 = d
    y0 = 0.0

    x1 = d+l1*math.cos(Th_1)
    y1 = l1*math.sin(Th_1)

    x2 = x1 + l2*math.cos(Th_1+Th_2)
    y2 = y1 + l2*math.sin(Th_1+Th_2)

    x3 = x2 + l3*math.cos(Phi)
    y3 = y2 + l3*math.sin(Phi)



    X1 = [x0,x1]
    Y1 = [y0,y1]

    X2 = [x1,x2]
    Y2 = [y1,y2]

    X3 = [x2,x3]
    Y3 = [y2,y3]
    
    p2.set_xdata(X1)
    p2.set_ydata(Y1)
    p3.set_xdata(X2)
    p3.set_ydata(Y2)
    p4.set_xdata(X3)
    p4.set_ydata(Y3)
    p5.set_xdata(X4)
    p5.set_ydata(Y4)
    p6.set_xdata(X5)
    p6.set_ydata(Y5)
    p7.set_xdata(x3)
    p7.set_ydata(y3)
    p8.set_xdata(x0)
    p8.set_ydata(y0)
    p9.set_xdata(x2)
    p9.set_ydata(y2)
    p10.set_xdata(x4)
    p10.set_ydata(y4)
    p11.set_xdata(x5)
    p11.set_ydata(y5)
    p12.set_xdata(x1)
    p12.set_ydata(y1)
    p13, = ax.plot(xp,yp,'.',color = 'black')
    fig.canvas.draw()
    fig.canvas.flush_events()
plt.pause(2)