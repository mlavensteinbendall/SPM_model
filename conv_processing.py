
import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

testtype = 'dt' # Set the test type

## ds convergance
if (testtype == 'ds'):

    ds0 = 0.005
    nsamples = 10
    ds = np.zeros(nsamples)
    dsvals = np.zeros(nsamples)
    for n in range(nsamples): ds[n] = ds0*(n+1)
    dt = 0.0025

    # print(ds)

    norm2 = np.zeros([nsamples])
    normMax = np.zeros([nsamples])
    integral = np.zeros([nsamples])

    for i in range(nsamples): # File number to load (0-5).

        data = np.loadtxt('ds_convergence/test_' + str(i) + '.txt')

        Ntimes = np.size(data,0) # Number of time steps.
        Nsizes = np.size(data,1) # Number of size steps.

        # Time and size arrays
        tt = np.linspace(0,Ntimes*dt,Ntimes)
        ss = np.linspace(0,Nsizes*ds[i],Nsizes)

        # Uncomment to show the overlay of the distributions at the final time-point.
        # fig,ax = plt.subplots()
        # ax.plot(ss,data[-1,:])
        # ax.plot(ss,np.exp(-(ss-10-tt[-1])**2),'r--')
        # plt.show()

        # Integral
        integral0 = ds[i]*0.5*(data[0,0] + data[0,-1] + 2*np.sum(data[0,1:-2])) # Trapezium rule
        integral[i] = ds[i]*0.5*(data[-1,0] + data[-1,-1] + 2*np.sum(data[-1,1:-2])) # Trapezium rule
        # 2 norm
        norm2[i] = (1/Nsizes*ds[i])*np.sqrt(np.sum( (data[-1,:] - np.exp(-(ss-10-tt[-1])**2))**2 ))
        # max norm
        normMax[i] = np.max(np.abs(data[-1,:] - np.exp(-(ss-10-tt[-1])**2)))

    # fig1,ax1 = plt.subplots()
    # ax1.plot(np.log(ds),np.log(norm2),'k')
    # ax1.plot(np.log(ds),np.log(normMax),'r--')
    # plt.show()

    fig2,ax2 = plt.subplots()
    ax2 = plt.plot(integral/integral0) # Plot the normalised 'leak'
    plt.show()

    print('2-Norm convergence: ' + str((np.log(norm2[-1])-np.log(norm2[0]))/(np.log(ds[-1])-np.log(ds[0]))))
    print('Max-Norm convergence: ' + str((np.log(normMax[-1])-np.log(normMax[0]))/(np.log(ds[-1])-np.log(ds[0]))))


## dt convergence
# Note: this needs to be modified to get the consective type error calculation

if (testtype == 'dt'):

    ds0 = 0.005
    nsamples = 8
    ds = np.zeros(nsamples); dt = np.zeros(nsamples)
    for n in range(nsamples): ds[n] = ds0*(n+1); dt[n] = ds[n]*0.9

    norm2 = np.zeros([nsamples-1])
    normMax = np.zeros([nsamples-1])

    for i in range(nsamples-1): # File number to load (0-5).

        NT = int(21/dt[i])

        data1 = np.loadtxt('dt_convergence/test_' + str(i) + '.txt',skiprows=NT) # Denser dataset
        data2 = np.loadtxt('dt_convergence/test_' + str(i+1) + '.txt',skiprows=NT) # Less dense dataset

        # Ntimes = np.size(data1,0) # Number of time steps.
        #Nsizes = np.size(data2,1) # Number of size steps.
        #print(str(np.size(data1,1)) + " " + str(np.size(data2,1)))

        # assuming that spatial points 0,2,4,6... = 0,1,2,3... and the final timepoint is equal

        # Integral
        #integral[i] = ds[i]*0.5*(data[-1,0] + data[-1,-1] + 2*np.sum(data[-1,1:-2])) # Trapezium rule
        # 2 norm
        norm2[i] = (1/(Nsizes*ds[i]))*np.sqrt(np.sum( (data1[-1,0::2] - data2[-1,:])**2 ))
        # max norm
        normMax[i] = np.max(np.abs(data1[-1,0::2] - data2[-1,:]))

    fig,ax1 = plt.subplots()
    ax1.plot(np.log(dt[1:]),np.log(norm2),'k')
    ax1.plot(np.log(dt[1:]),np.log(normMax),'r--')
    plt.show()

    # fig,ax2 = plt.subplots()
    # ax2 = plt.plot(integral/integral[0]) # Plot the normalised 'leak'
    # plt.show()

    print('2-Norm convergence: ' + str((np.log(norm2[-1])-np.log(norm2[0]))/(np.log(dt[-2])-np.log(dt[0]))))
    print('Max-Norm convergence: ' + str((np.log(normMax[-1])-np.log(normMax[0]))/(np.log(dt[-2])-np.log(dt[0]))))
