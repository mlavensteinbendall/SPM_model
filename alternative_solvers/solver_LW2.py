
# Title: 2st order solver, SPM (age), no mortality/reproduction
# Author: Stephen Williams
# Date: 27th September 2023
# Notes: higher "accuracy" coefficients.

import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

CFL = 0.5 # CFL condition, must be <1
ds = 0.01 # Size grid spacing
dt = CFL*ds # Time gris spacing

Smax = 20 # Maximum size to calculate
Tmax = 15 # End time
Nsizes = int(Smax/ds) # Total number of size-steps
Ntimes = int(Tmax/dt) # Total number of time-steps
sizes = np.linspace(0,Smax,num=Nsizes) # Grid of size points
times = np.linspace(0,Tmax,num=Ntimes) # Grid of times points

# Initial condition
N = np.zeros([Nsizes]) # Store for the current timepoint

# Fitness functions
g = np.ones([Nsizes]) # growth rate
#g[0:int(Nsizes/2)] = np.linspace(0,-1,int(Nsizes/2))
r = np.zeros([Nsizes])  # reproduction
#r[-50:-1] = 1.5*np.exp(-0.1*np.linspace(1,50,49))
mu = np.zeros([Nsizes]) # mortality

# Difference matrices
D1 = np.zeros([Nsizes,Nsizes]) # Store for 1st finite difference matrix
D2 = np.zeros([Nsizes,Nsizes]) # Store for 2nd finite difference matrix

# Set finite difference coefficients.
FFDC1 = np.array([-3/2,2,-1/2])
CFDC1 = np.array([1/12,-2/3,0,2/3,-1/12])
BFDC1 = np.array([1/2,-2,3/2])

FFDC2 = np.array([2,-5,4,-1])
CFDC2 = np.array([-1/12,4/3,-5/2,4/3,-1/12])
BFDC2 = np.array([-1,4,-5,2])

# Start points
D1[0,0:3] = FFDC1[:]/ds;  # Start-point 1st finite difference matrix
D1[1,0:3] = FFDC1[:]/ds;  # Start-point 1st finite difference matrix
#D1[2,0:3] = FFDC1[:]/ds;  # Start-point 1st finite difference matrix
#
D2[0,0:4] = FFDC2[:]/(ds**2); # Start-point 2nd finite difference matrix
D2[1,0:4] = FFDC2[:]/(ds**2); # Start-point 2nd finite difference matrix
#D2[2,0:4] = FFDC2[:]/(ds**2); # Start-point 2nd finite difference matrix
#
# Mid points
for i in range(2,Nsizes-2): # Loop through the diagonals
   D1[i,i-2:i+3] = CFDC1[:]/ds
   D2[i,i-2:i+3] = CFDC2[:]/(ds**2)
#
# End points
D1[-1,-3:] = BFDC1[:]/ds; # End-point 1st finite difference matrix
D1[-2,-3:] = BFDC1[:]/ds; # End-point 1st finite difference matrix
#D1[-3,-3:] = BFDC1[:]/ds; # End-point 1st finite difference matrix
#
D2[-1,-4:] = BFDC2[:]/(ds**2); # End-point 2nd finite difference matrix
D2[-2,-4:] = BFDC2[:]/(ds**2); # End-point 2nd finite difference matrix
#D2[-3,-4:] = BFDC2[:]/(ds**2); # End-point 2nd finite difference matrix

#print(D2[-3:,-5:])

# Difference co-efficients
gp  = D1.dot(g) # Get numerical first derivative of g
gpp = D2.dot(g) # Get numerical second derivative of g

a1 = np.zeros([Nsizes]) # Store for N terms coef
a2 = np.zeros([Nsizes]) # Store for dNds terms coef
a3 = np.zeros([Nsizes]) # Store for d2Nds2 terms coef

a1[:] = 1 - gp[:]*dt + (gp[:]**2 + g[:]*gp[:])*(dt**2)/2
a2[:] = -g[:]*dt + 3*g[:]*gp[:]*(dt**2)/2
a3[:] = (g[:]**2)*(dt**2)/2

# Initial condition
N[:] = np.exp(-(sizes-10)**2) # Initial condition setter

with open('cat.txt', 'w') as file: # Initialise an outputter file (safe)

    for t,T in enumerate(times): # Loop on times

        #N[3] = 0
        #for n,s in enumerate(N):
        #    N[3] += r[n]*s*ds

        # Step 1 - half step time, mortality
        N[:] = N[:]*np.exp(-mu[:]*dt/2)
        # Step 2 - half step time, growth
        N[:] = a1[:]*N[:] + a2[:]*(D1.dot(N)) + a3[:]*(D2.dot(N))
        # Step 3 - half step time, mortality
        N[:] = N[:]*np.exp(-mu[:]*dt/2)

        # Boundary conditions
        #N[0] = 0
        #N[-1] = 0

        for n in N: # Output the current time solution
            file.write(str(n))
            file.write(" ")
        file.write("\n")


