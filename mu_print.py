
import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

data = np.loadtxt('mu_test/test_1.txt')

dt = 0.001
Tmax = 1 # End time
Ntimes = int(Tmax/dt)+1 # Total number of time-steps

dsi = 0.005
Smax = 15 # Maximum size to calculate
Nsizes = int(Smax/dsi)+1 # Total number of size-steps

sizes = np.linspace(0,Smax,num=Nsizes) # Grid of size points

sol = np.exp(-(sizes-10)**2) # Initial condition setter

for i in range(0,1000,100):
    # plt.plot(sizes,data[i,:])
    tt = dt*i
    sol = np.exp(-(sizes-tt-10)**2)*np.exp(-tt)
    plt.plot(sizes,sol)
    plt.plot(sizes,data[i,:],'r:')
    plt.show()
