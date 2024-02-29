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

# ds = ds/10
# ds = np.linspace(0.005,0.020,5)

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
    # sol = np.exp(-(sizes-10-Tend)**2) * np.exp(-Tend) # g(s)=1, mu=1
    # # sol = np.exp(-(sizes-10-Tend)**2) * np.exp(-sizes*Tend) # g(s)=1, mu=s
    # sol = np.exp(-(np.log(np.exp(sizes)-Tend)-10)**2) * np.exp((np.exp(-sizes)-sizes)*Tend) # g(s)=1, mu=s
    # sol = np.exp(-(np.log(np.exp(sizes)-Tend)-10)**2)* np.exp(np.exp(-sizes*Tend)) # g(s)=e(-s), mu=0
    
    # g(s)=e(-s), mu= s
    # Y   = np.log(np.exp(sizes) - Tend)
    Y = np.log(np.clip(np.exp(sizes) - Tend, a_min=1e-15, a_max=None))  
    # phi = np.exp(-((Y-0.4)/0.1)**2)
    phi = np.exp(-((Y-2)/0.1)**2)
    sol = phi * np.exp(Tend + sizes - (sizes * np.exp(sizes)) - (Y * (1 - np.exp(Y))))

    # Y = np.log(np.clip(np.exp(sizes) - Tend, a_min=1e-15, a_max=None))
    # phi = np.exp(-((Y-0.4)/0.1)**2)
    # # sol = (phi / (np.exp(Y * (1 - np.exp(Y))))) * (np.exp(Tend + sizes - (sizes * np.exp(sizes))))
    # denominator = np.exp(Y * (1 - np.exp(Y))) + 1e-15  # Adding a small positive constant
    # sol = (phi / denominator) * np.exp(Tend + sizes - (sizes * np.exp(sizes)))

    # print(Tend)
    # print(np.shape(data))

    # # norms
    Norm2[i] =  ((1/Nsizes)*np.sum((data[n,:]-sol[:])**2))**0.5 # L2 error.
    NormMax[i] = np.max(np.abs(data[n,:]-sol[:])) # L-Max error.

    # print(data[n,:])
    print(sol[:])

    # (Optional: Plot the differences.)
    # plt.plot(sizes,data[n,:]-sol)
    # plt.show()

# Print out the dataset 0 errors, q cannot be defined.
print('For ds ='+ str(ds[0]))
print('Norm2 = ' + str(round(Norm2[0],10)))
print('NormMax = ' + str(round(NormMax[0],10)))
print(' ')


# Loop through the remaining datasets.
for i in range(ntests-1):
    print('For ds =' + str(ds[i+1]))
    print('Norm2 = ' + str(round(Norm2[i+1],10))); print('NormMax = ' + str(round(NormMax[i+1],10))) # Print out error values.
    print('L2 q estimate = ' + str(round(np.log(Norm2[i+1]/Norm2[i]) / np.log(ds[i+1]/ds[i]),10) )) # L2 q estimate.
    print('LMax q estimate = ' + str(round(np.log(NormMax[i+1]/NormMax[i]) / np.log(ds[i+1]/ds[i]),10) )) # L-Max q estimate.
    print(' ')

# Plot the log-log for the errors.
plt.loglog(ds, Norm2, label='Norm2')
plt.loglog(ds, NormMax, label='NormMax')
# plt.loglog(Norm2, label='Norm2')
# plt.loglog(NormMax, label='NormMax')
plt.loglog(ds, ds**2, label='order-2')

plt.xlabel('ds')
plt.ylabel('Norm')
plt.title('Convergence based on ds')
plt.legend()
plt.show()

