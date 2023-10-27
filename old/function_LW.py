# This code is mysteriously broken and turns the cpu up to 1000%?
print('This code is broken!')

import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

def LW_SPM(ds,dt,ntag,filename):

    Tmax = 21 # End time
    Smax = Tmax + 10 + 5 # Maximum size to calculate
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
    r[int(Nsizes/4):-1] = 0
    mu = np.zeros([Nsizes]) # mortality
    mu[int(Nsizes/2):-1] = 0

    # Difference matrices
    D1 = np.zeros([Nsizes,Nsizes]) # Store for 1st finite difference matrix
    D2 = np.zeros([Nsizes,Nsizes]) # Store for 2nd finite difference matrix

    # Mid points
    for ii in range(1,Nsizes-1): # Loop through the diagonals
        D1[ii,ii-1] = -0.5/ds;   D1[ii,ii+1] = 0.5/ds
        D2[ii,ii-1] = 1/(ds**2); D2[ii,ii] = -2/(ds**2); D2[ii,ii+1] = 1/(ds**2)
    
    # Difference co-efficients
    gp  = D1.dot(g) # Get numerical first derivative of g
    gpp = D2.dot(g) # Get numerical second derivative of g

    a1 = np.zeros([Nsizes]) # Store for N terms coef
    a2 = np.zeros([Nsizes]) # Store for dNds terms coef
    a3 = np.zeros([Nsizes]) # Store for d2Nds2 terms coef

    a1[:] = 1 - gp[:]*dt + (gp[:]**2 + g[:]*gpp[:])*(dt**2)/2
    a2[:] = -g[:]*dt + 3*g[:]*gp[:]*(dt**2)/2
    a3[:] = (g[:]**2)*(dt**2)/2

    # Initial condition
    N[:] = np.exp(-(sizes-10)**2) # Initial condition setter

    with open(filename + 'test_' + str(ntag) + '.txt', 'w') as file: # Initialise an outputter file (safe)
        for t,T in enumerate(times,1): # Loop on times

            for n in N: # Output the current time solution
                file.write(str(n))
                file.write(" ")
            file.write("\n")

            N[0] = 0

            for n,s in enumerate(N):
                N[0] += r[n]*s*ds

                # Step 1 - half step time, mortality
                N[:] = N[:]*np.exp(-mu[:]*dt/2)
                # Step 2 - half step time, growth
                N[:] = a1[:]*N[:] + a2[:]*(D1.dot(N)) + a3[:]*(D2.dot(N))
                # Step 3 - half step time, mortality
                N[:] = N[:]*np.exp(-mu[:]*dt/2)

        # Output final time.
        for n in N: # Output the current time solution
            file.write(str(n))
            file.write(" ")
        file.write("\n")
