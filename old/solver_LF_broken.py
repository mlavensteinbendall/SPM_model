## problematic Lax-friedrichs solver 
# Notes: seems to 'somewhat' work. But, there is an unexpectedly large numerical diffusion.

## imports
# Public imports
import numpy as np
import matplotlib.pyplot as plt

# Private imports

## Initialise an outputter file
with open('output.txt', 'w') as file:

    ## Constants
    # System constants
    T = 50
    k = 2
    dt = 0.005 # Time step size
    ds = k*dt# Size step size
    Nsteps = int(T/dt) # Number of timesteps to calculate
    Smax = 30 # Maximum size. Assume that the minimum size is 0.
    Nsizes = int(Smax/ds) # Number of sizes to calculate
    Sadult = 10 # Size of adult
    M = 0 # Store for population functionals

    ## Preallocation
    N = np.zeros([Nsizes]) # Store for system size at current time
    Nold = np.zeros([Nsizes]) # Store for system size at previous time
    times = np.linspace(0,dt*Nsteps,Nsteps) # Array of system times
    sizes = np.linspace(0,Smax,Nsizes) # Array of organisms sizes

    ## Set the dynamics. Note: might refactor this into functions.
    # Reproduction, function of size
    R = np.zeros([Nsizes])
    for m,s in enumerate(sizes):
        if s > Sadult*0.8:
            R[m] = 0 # Adults have babies
    # Mortality, function of size
    Mu = np.zeros([Nsizes])
    for m,s in enumerate(sizes):
        if s > Sadult*0.8:
            Mu[m] = 0 # Adults can die, and do so at a given rate.

    # Aging rate, function of size
    g = 1*np.ones([Nsizes]) # Growth function
    #gA = 1 #np.linspace(1,-1,Nsteps)
    #g0 = np.zeros([len(sizes)])
    #g0 = np.zeros([len(sizes)])
    # g0[1:int(len(sizes)/2)] = np.sin(sizes[1:int(len(sizes)/2)]*np.pi/Sadult)
    # g0[1:int(len(sizes)/2)] = np.linspace(1,0,int(len(sizes)/2)-1)
    #g0 = np.linspace(0,10,len(sizes))
    #g0 = np.exp(-g0)

    ## Set inital conditions
    # Loop on the population sizes
    for n in range(50):
        N[n] = 1*np.exp(-0.1*n) # Initial condition, edit here

    # Output the results
    for m,Ni in enumerate(N):
        file.write(str(Ni))
        file.write(" ")
    file.write("\n")

    ## Main Loop
    for n, t in enumerate(times):

        # Set time dependent functions
        # g = g0*gA[1] 
        #g = g0*gA

        # Store the old population size distribution
        Nold = np.copy(N)
        N = np.zeros([Nsizes])
        
        # Implement the BVP at s=0 to calculate the new s=0 pop
        # Loop over the sizes, figure out N(t,0) += r(s)*N(t,s) for each
        N[0] = 0
        for m,No in enumerate(Nold):
            N[0] += R[m]*No*ds

        # Loop over the remaining sizes and implement C-N algorithm
        for s,Ns in enumerate(N[1:Nsizes-1], start=1):

            # Perform the different steps in the time splitting

            # Step one (a) - Growth
            f1 = g[s]*Nold[s]
            f3 = g[s]*Nold[s-1]
            f2 = g[s]*Nold[s+1]
            F1 = (ds/(2*dt)) * (Nold[s] - Nold[s+1]) + 0.5*(f1 + f2)
            F2 = (ds/(2*dt)) * (Nold[s-1] - Nold[s]) + 0.5*(f3 + f1)
            N[s] = Nold[s] - (dt/ds)*(F1-F2)

            # Step one (b) - Growth

            # Step two - Death
            N[s] = N[s] - dt*Mu[s]*N[s]
        
        N[Nsizes-1]=0 # Perform s=s_max bdry condition.

        for m,Ni in enumerate(N):
            file.write(str(Ni))
            file.write(" ")
        file.write("\n")

    ## Junk statements
    #print(Nsteps) # Debugger print
