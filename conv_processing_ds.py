# Title: Code to process data to perform convergence test on the model.
# Author: Stephen Williams
# Notes: Works on a dataset varrying ds, holding dt constant (within CFL).
##

import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

ntests = 5 # Total number of data files.
Smax = 15 # Maximum size calculated.
Tmax = 1 # Maximum time calculated.
dt = 0.001 # Time step.
Ntimes = int(Tmax/dt)+1 # Number of timesteps.
# print(Ntimes) # (Optional: output number of timesteps)

# Spatial grid step
ds = np.zeros(5)
ds[0] = 0.005; ds[1] = 0.010
ds[2] = 0.020; ds[3] = 0.025
ds[4] = 0.050

# Store for error calculations
Norm2 = np.zeros(ntests) # L2 norm values.
NormMax = np.zeros(ntests) # L-Max norm values.

for i in range(ntests): # Loop through datafiles

    Nsizes = int(Smax/ds[i])+1 # Get the number of spatial points in the data.
    sizes = np.linspace(0,Smax,num=Nsizes) # Create an array of those sizes.
    data = np.loadtxt('ds_convergence/test_' + str(i) + '.txt') # Load in relevant data.
    n = 1000 # Time-step of comparison.
    Tend = n*dt # Get the associated timepoint value.

    # Analytical solution
    # sol = np.exp(-(sizes-10-Tend)**2) # g(s)=1, mu=0

    # g(s)= exp(-s), mu=s
    # print(np.exp(sizes))
    # epsilon = 1e-10  # Small offset to avoid zero in logarithm
    # p = np.log(np.exp(sizes)-Tend)
    phi = np.exp(-((np.log(np.exp(sizes)-Tend)-0.4)/0.1)**2)
    Y   = np.log(np.exp(sizes)-Tend)
    sol = (phi / (np.exp(Y * (np.exp(Y) - 1)))) * (np.exp(Tend + sizes - (sizes * np.exp(sizes))))

    # print(np.shape(sol))

    # X = sizes
    # Y = np.linspace(0,Tend, n)
    # X, Y = np.meshgrid(X, Y)

    # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # plt.plot(sizes,sol)
    # plt.show()
    # norms
    Norm2[i] =  ((1/Nsizes)*np.sum((data[n,:]-sol[:])**2))**0.5 # L2 error.
    NormMax[i] = np.max(np.abs(data[n,:]-sol[:])) # L-Max error.

    # (Optional: Plot the differences.)
    # plt.plot(sizes,data[n,:]-sol)
    # plt.show()

# Print out the dataset 0 errors, q cannot be defined.
print(Norm2[0])
print(NormMax[0])
print(' ')

# Loop through the remaining datasets.
for i in range(ntests-1):
    print(Norm2[i+1]); print(NormMax[i+1]) # Print out error values.
    print(np.log(Norm2[i+1]/Norm2[i]) / np.log(ds[i+1]/ds[i]) ) # L2 q estimate.
    print(np.log(NormMax[i+1]/NormMax[i]) / np.log(ds[i+1]/ds[i]) ) # L-Max q estimate.
    print(' ')

# # Plot the log-log for the errors.
plt.loglog(Norm2, label='Norm2')
plt.loglog(NormMax, label='NormMax')

# plt.plot(Norm2, label='Norm2')
# plt.plot(NormMax, label='NormMax')

plt.xlabel('ds')
plt.ylabel('Norm')
plt.title('Convergence based on ds')
plt.legend()
plt.show()

