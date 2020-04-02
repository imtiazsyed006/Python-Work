# I used the alogorithm developed by Phil Kim in his book 'Kalman Filter for Beginners'. He implemented his algorithm in Matlab
# while I write the sampe alogorithm in Python.
#
# The sample data used in this code is recorded by Phil Kim from Gyroscope and Acceleration.



import numpy as np
import matplotlib.pyplot as plt
import math

firstRun  = []
firstRun1 = []
firstRun2 = []
file  = open('gyro.txt', 'r')
file1 = open('accel.txt','r')

def CompFilterWithPI(p, q, r, ax, ay, dt):
    
    global p_hat
    global q_hat
    global prevPhi
    global prevTheta
    global prevPsi
    
    if not firstRun:
        p_hat = 0
        q_hat = 0
        
        prevPhi   = 0
        prevTheta = 0
        prevPsi   = 0
    
    phi_a, theta_a           = EulerAccel(ax, ay)
    dotPhi, dotTheta, dotPsi = BodyToInertial(p, q, r, prevPhi, prevTheta)
    
    phi      = prevPhi   + dt*(dotPhi - p_hat)
    theta    = prevTheta + dt*(dotTheta - q_hat)
    psi      = prevPsi   + dt*dotPsi
    
    p_hat    = PILawPhi(phi - phi_a)
    q_hat    = PILawTheta(theta - theta_a)
    
    prevPhi  = phi
    preTheta = theta
    prevPsi  = psi
    return phi, theta, psi

        
def BodyToInertial(p, q, r, phi, theta):
    sinPhi   = math.sin(phi)
    cosPhi   = math.cos(phi)
    cosTheta = math.cos(theta)
    tanTheta = math.tan(theta)
    
    dotPhi   = p + q*sinPhi*tanTheta + r*cosPhi*tanTheta
    dotTheta = q*cosPhi              - r*sinPhi
    dotPsi   = q*sinPhi/cosTheta     + r*cosPhi/cosTheta
    
    return dotPhi, dotTheta, dotPsi

def PILawPhi(delPhi):
    
    global prevP
    global prevdelPhi
    
    if not firstRun1:
        prevP      = 0
        prevdelPhi = 0
        
    p_hat      = prevP + 0.1415*delPhi - 0.1414*prevdelPhi
    prevP      = p_hat
    prevdelPhi = delPhi
    
    return p_hat

def PILawTheta(delTheta):
    
    global prevQ
    global prevdelTheta
    
    if not firstRun2:
        prevQ = 0
        prevdelTheta = 0
        
    q_hat = prevQ + 0.1415*delTheta - 0.1414*prevdelTheta
    prevQ = q_hat
    prevdelTheta = delTheta
    
    return q_hat
    
def EulerAccel(ax, ay):
    
    g     = 9.8
    theta = math.asin( ax/g )
    phi   = math.asin(-ay/(g*math.cos(theta)))
    
    return phi, theta

def GetGyro():
    line = file.readline()
    wx,wy,wz = line.split(',')
        
    return float(wx),float(wy),float(wz)

def GetAccel():
    line = file1.readline()
    ax,ay,az = line.split(',')
    
    return float(ax),float(ay)

        
## Test Program

Nsamples = 41500
EulerSaved = np.zeros((Nsamples, 3))
dt = 0.01

for k in range(0, Nsamples-1):
    ax, ay          = GetAccel()
    p, q, r         = GetGyro()
    phi, theta, psi = CompFilterWithPI(p, q, r, ax, ay, dt)
    EulerSaved[k,:] = [phi, theta, psi]
    
PhiSaved   = EulerSaved[:,0]*180/math.pi
ThetaSaved = EulerSaved[:,1]*180/math.pi
PsiSaved   = EulerSaved[:,2]*180/math.pi

t = np.arange(0,(Nsamples+1)*dt-dt,dt)

fig1 = plt.figure()

ax1 = fig1.add_subplot(311)
ax2 = fig1.add_subplot(312)
ax3 = fig1.add_subplot(313)

ax1.set_title('Complementary filter for Pitch and Roll')
ax1.set_ylabel('Roll angle')
ax2.set_ylabel('Pitch angle')
ax3.set_ylabel('Yaw angle')
ax3.set_xlabel('Time')

ax1.plot(t, PhiSaved)
ax2.plot(t, ThetaSaved)
ax3.plot(t, PsiSaved)


plt.show()
