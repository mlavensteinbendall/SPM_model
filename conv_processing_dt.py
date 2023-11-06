# Title: Code to process data to perform convergence test on the model.
# Author: Stephen Williams
# Notes: Works on a dataset varrying ds and dt (within CFL).
##

import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

ntests = 5 # Number of data files to process.
Smax = 20 # Maximum size to calculate.
Tmax = 1 # Maximum time to calculate.

# Spatial grid step
ds = np.zeros(ntests)
ds[0] = 0.00125; ds[1] = 0.0025
ds[2] = 0.005; ds[3] = 0.010
ds[4] = 0.020

# Temporal grid step
dt = np.zeros(ntests)
dt[0] = 0.00125/2; dt[1] = 0.00250/2
dt[2] = 0.005/2; dt[3] = 0.010/2
dt[4] = 0.020/2

# Stores for the error calculations
Norm2 = np.zeros(ntests-1)
NormMax = np.zeros(ntests-1)

# Loop through the data files
for i in range(ntests-1):

    Nsizes = int(Smax/ds[i+1])+1 # Get the number of spatial grids in the coarsest dataset.

    # Load in the datasets
    data1 = np.loadtxt('dt_convergence/test_' + str(i) + '.txt') # Finer data.
    data2 = np.loadtxt('dt_convergence/test_' + str(i+1) + '.txt') # Coarser data.

    # Calculate the equivilent 
    tinterest = 0.5 # Define the time where the calculations are compared.
    n1 = int(tinterest/dt[i]) # Get fine-data time-step.
    n2 = int(tinterest/dt[i+1]) # Get corse-data time-step.

    Norm2[i] =  ((1/Nsizes)*np.sum((data1[n1,0::2]-data2[n2,:])**2))**0.5 # L2 norm error.
    NormMax[i] = np.max(np.abs(data1[n1,0::2]-data2[n2,:])) # L-max norm error.

    # NormMax[i] = np.max(np.abs(data1[n1,:]-data2[n2,:]))
    # plt.plot(sizes,data[n,:]-sol)
    # plt.show()

# Output the error between the first two datasets
print(Norm2[0])
print(NormMax[0])
print(' ')

# output the error values between the remaining data for which a q can be calculated.
for i in range(ntests-2):
    print(Norm2[i+1]) # Output L2 error.
    print(NormMax[i+1]) # Output L-Max error.
    print(np.log(Norm2[i+1]/Norm2[i]) / np.log(ds[i+1]/ds[i]) ) # Get the first q-estimate
    print(np.log(NormMax[i+1]/NormMax[i]) / np.log(ds[i+1]/ds[i]) ) # Get the second q-estimate
    print(' ')

plt.loglog(Norm2)
plt.show()

