
import numpy as np

# Time constants
T = 100
dt = 0.005
Nsteps = int(T/dt)

# Space constants
Smax = 1
ds = 0.01
Nsizes = int(Smax/ds)
alpha = 1

# Preallocation
u = np.zeros([Nsteps,Nsizes])

# Initial condition(s)
u[0,5] = 1
#u[0,1:121] = np.linspace(0,1,120)
#u[0,121:241] = 1-np.linspace(0,1,120)
#u[0,121:240] = 1-np.linspace(0,1,119)

# main loop
for n in range(1,Nsteps):

    # Do BVP on s = [0,end] positions
    u[n,0] = 0
    u[n,Nsizes-1] = 0

    for s in range(1,Nsizes-1):

        f1 = alpha*0.5*(u[n-1,s])**2
        f2 = alpha*0.5*(u[n-1,s+1])**2
        f3 = alpha*0.5*(u[n-1,s-1])**2
        F1 = (ds/(2*dt)) * (u[n-1,s] - u[n-1,s+1]) + 0.5*(f1 + f2)
        F2 = (ds/(2*dt)) * (u[n-1,s-1] - u[n-1,s]) + 0.5*(f3 + f1)
        u[n,s] = u[n-1,s] - (dt/ds)*(F1-F2)

with open('output_burger.txt', 'w') as file:
    for n in range(Nsteps):
        for s in range(Nsizes):
            file.write(str(u[n,s]))
            file.write(" ")
        file.write("\n")