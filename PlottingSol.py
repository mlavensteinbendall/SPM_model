import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt


Smax = 15 # Maximum size calculated.
Tmax = 1 # Maximum time calculated.
dt = 0.001 # Time step.

ds = np.zeros(5)
ds[0] = 0.005; ds[1] = 0.010
ds[2] = 0.020; ds[3] = 0.025
ds[4] = 0.050

# ds = ds/10

# ds = np.linspace(0.005,0.020,5)

# Change this value to get different ds indexes
ds_index = 4

# Ntimes = int(Tmax/dt)+1 # Number of timesteps.
Nsizes = int(Smax/ds[ds_index])+1 # Get the number of spatial points in the data.
sizes = np.linspace(0,Smax,num=Nsizes) # Create an array of those sizes.
# times = np.linspace(0,Tmax,num=Ntimes) # Grid of times points

data = np.loadtxt('ds_convergence/test_' + str(ds_index) + '.txt') # Load in relevant data.

row, column = data.shape

time_array = np.linspace(0,row-1, 4)
# print(time_array)

for n in range(4): #4

    time = n/3
    print(time)

    # Analytical Solution
    # Y   = np.log(np.exp(sizes) - time)
    Y = np.log(np.clip(np.exp(sizes) - time, a_min=1e-15, a_max=None))  # at time 1 and size 0 we have a nan value
    # phi = np.exp(-((Y-0.4)/0.1)**2)
    phi = np.exp(-((Y-2)/0.1)**2)
    sol = phi * np.exp(time + sizes - (sizes * np.exp(sizes)) - (Y * (1 - np.exp(Y))))
    # sol = phi * np.exp(np.exp(Y) * (Y-1) - (np.exp(sizes)- time)**(5/6)/5 + (np.exp(sizes))**(5/6)/5 + np.exp(sizes)*(1-sizes))
    # sol = phi + np.exp(np.exp(Y)*(Y-1) - np.exp(Y)**(5/6)/5)

    # print(Y[0])

    # Plot the Analytical and Numerical Solution
    plt.plot(sizes, sol, label='Analytical', linestyle='solid')
    plt.plot(sizes, data[int(time_array[int(n)]),:], label='Numerical', linestyle='--')
    plt.xlabel('Size')
    plt.ylabel('Population')
    plt.title('Population Based on Size at time = ' + str(round(time,2)) + ' for ds = ' + str(ds[ds_index]))
    plt.legend()
    plt.ylim(-.2, 1.1)  # Set y-axis limits from 0 to 12
    plt.show()





# alt code
    # solutions = []

    # # Analytical Solution loop for each time step
    # for t,T in enumerate(times):
    #     Y   = np.log(np.exp(sizes) - t)
    #     phi = np.exp(-((Y-0.4)/0.1)**2)
    #     sol = (phi / (np.exp(Y * (1 - np.exp(Y))))) * (np.exp(t + sizes - (sizes * np.exp(sizes))))
    #     solutions.append(sol)

    # # Convert the solutions list to a NumPy array for easy plotting
    # solutions = np.array(solutions)

    # print(solutions.shape)
    # print(data.shape)

    # plt.plot(sizes, solutions[t,:], label='Analytical', linestyle='solid')