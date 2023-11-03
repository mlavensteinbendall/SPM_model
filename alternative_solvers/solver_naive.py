
# Title: 1st order naive solver, SPM (age), no mortality/reproduction
# Author: Stephen Williams
# Date: 27th September 2023
# Notes:

import numpy as np # Numpy for cython

CFL = 0.5 # Must be <1
ds = 0.01 # Size grid spacing
dt = CFL*ds # Time gris spacing

Smax = 30 # Maximum size to calculate
Tmax = 20 # End time
Nsizes = int(Smax/ds) # Total number of size-steps
Ntimes = int(Tmax/dt) # Total number of time-steps
sizes = np.linspace(0,Smax,num=Nsizes) # Grid of size points
times = np.linspace(0,Tmax,num=Ntimes) # Grid of times points

# Initial condition
N = np.zeros([Nsizes]) # Store for the current timepoint
#Nold = np.zeros([Nsizes]) # Store for the old timepoint

N[:] = np.exp(-(sizes-10)**2) # Initial condition setter

with open('output_firstOrder.txt', 'w') as file: # Initialise an outputter file (safe)

    for t,T in enumerate(times): # Loop on times

        N[1:] = N[1:] - dt*(N[1:]-N[0:-1])/ds # 1st order differences, vectorized

        for n in N: # Output the current time solution
            file.write(str(n))
            file.write(" ")
        file.write("\n")

