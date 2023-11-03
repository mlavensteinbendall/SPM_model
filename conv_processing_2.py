
import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

ntests = 5
Smax = 20
Tmax = 1
dt = 0.00005
Ntimes = int(Tmax/dt)+1
print(Ntimes)

ds = np.zeros(5)
ds[0] = 0.005
ds[1] = 0.010
ds[2] = 0.020
ds[3] = 0.025
ds[4] = 0.050

Norm2 = np.zeros(ntests)
NormMax = np.zeros(ntests)

for i in range(ntests):

    Nsizes = int(Smax/ds[i])+1
    sizes = np.linspace(0,Smax,num=Nsizes)
    data = np.loadtxt('ds_convergence/test_' + str(i) + '.txt')
    n = 20000
    Tend = n*dt
    sol = np.exp(-(sizes-10-Tend)**2)
    Norm2[i] =  ((1/Nsizes)*np.sum((data[n,:]-sol[:])**2))**0.5
    NormMax[i] = np.max(np.abs(data[n,:]-sol[:]))
    # plt.plot(sizes,data[n,:]-sol)
    # plt.show()

print(Norm2[0])
print(NormMax[0])
print(' ')

for i in range(ntests-1):
    print(Norm2[i+1])
    print(NormMax[i+1])
    print(np.log(Norm2[i+1]/Norm2[i]) / np.log(ds[i+1]/ds[i]) )
    print(np.log(NormMax[i+1]/NormMax[i]) / np.log(ds[i+1]/ds[i]) )
    print(' ')

plt.loglog(Norm2)
plt.show()

