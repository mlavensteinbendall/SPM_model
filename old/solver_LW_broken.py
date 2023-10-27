## Failed version of Lax-wendroff solver.

## imports
# Public imports
import numpy as np
#import matplotlib.pyplot as plt

# Private imports

## Initialise an outputter file
with open('output.txt', 'w') as file:

    ## Constants
    # System constants
    T = 100
    k = 1/0.9
    dt = 0.05 # Time step size
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
    D0N = np.zeros([Nsizes])
    D0GpN = np.zeros([Nsizes])
    DpmN = np.zeros([Nsizes])
    D0 = np.zeros([Nsizes])

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
    gp = 0*np.ones([Nsizes]) # Growth gradient
    gpp = 0*np.ones([Nsizes]) # Growth gradient

    # Startpoints
    gp[0] = (g[1]-g[0])/ds 
    gpp[0] = (g[0]-2*g[1]+g[2])/(ds**2)
    # Midpoints
    for s in range(1,Nsizes-2):
        gp[s] = (g[s+1]-g[s-1])/(2*ds)
        gpp[s] = (g[s+1]-2*g[s]+g[s-1])/(ds**2)
    # End point
    gp[Nsizes-1] = (g[Nsizes-1]-g[Nsizes-2])/ds 
    gpp[Nsizes-1] = (g[Nsizes-3]-2*g[Nsizes-2]+g[Nsizes-1])/(ds**2)

    #gA = 1 #np.linspace(1,-1,Nsteps)
    #g0 = np.zeros([len(sizes)])
    #g0 = np.zeros([len(sizes)])
    # g0[1:int(len(sizes)/2)] = np.sin(sizes[1:int(len(sizes)/2)]*np.pi/Sadult)
    # g0[1:int(len(sizes)/2)] = np.linspace(1,0,int(len(sizes)/2)-1)
    #g0 = np.linspace(0,10,len(sizes))
    #g0 = np.exp(-g0)

    ## Set inital conditions
    # Loop on the population sizes
    for j,s in enumerate(sizes):
        N[s] = 1*np.exp(-0.1*(s-100*ds)**2) # Initial condition, edit here

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

        # Get DpmN, D0N
        #DpmN[0] = (Nold[0]-2*Nold[1]+Nold[2])/(ds**2) # Startpoint
        #D0N[0] = (Nold[1]-Nold[0])/(ds)
        #for s in range(1,Nsizes-2):
            DpmN[s] = (Nold[s+1]-2*Nold[s]+Nold[s-1])/(ds**2)
            #D0N[s] = (Nold[s+1]-Nold[s-1])/(ds*2)
        DpmN[Nsizes-1] = (Nold[Nsizes-3]-2*Nold[Nsizes-2]+Nold[Nsizes-1])/(ds**2) # End point
        D0N[Nsizes-1] = (Nold[Nsizes-1]-Nold[Nsizes-2])/ds

        # Loop over the remaining sizes and implement C-N algorithm
        for s,Ns in enumerate(N[1:Nsizes-1], start=1):

            # Perform the different steps in the time splitting

            # half step 1 - Death
            #N[s] = N[s]*np.exp(-Mu[s]*dt/2)

            # full step 1 - Growth
            #N[s] = Nold[s] + dt*(-gp[s]*Nold[s] - g[s]*D0N[s])
            if (s!= Nsizes-1):
                N[s] = Nold[s] + dt*(-(Nold[s+1]-Nold[s])/ds)
            #N[s] = N[s] + (dt**2/2)*(g[s]*(2*gp[s]*D0N[s] + g[s]*DpmN[s] + gpp[s]*Nold[s]))

            # half step 2 - Death
            #N[s] = N[s]*np.exp(-Mu[s]*dt/2)
        
        N[Nsizes-1]=0 # Perform s=s_max bdry condition.

        for s,Ns in enumerate(N):
            file.write(str(N[s]))
            file.write(" ")
        file.write("\n")

    ## Junk statements
    #print(Nsteps) # Debugger print
