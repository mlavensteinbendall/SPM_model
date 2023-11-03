
import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

ntests = 5
Smax = 20
Tmax = 1

ds = np.zeros(ntests)
ds[0] = 0.00125
ds[1] = 0.0025
ds[2] = 0.005
ds[3] = 0.010
ds[4] = 0.020

dt = np.zeros(ntests)
dt[0] = 0.00125/2
dt[1] = 0.00250/2
dt[2] = 0.005/2
dt[3] = 0.010/2
dt[4] = 0.020/2

Norm2 = np.zeros(ntests)
NormMax = np.zeros(ntests)

for i in range(ntests-1):

    Nsizes = int(Smax/ds[i+1])+1
    sizes = np.linspace(0,Smax,num=Nsizes)
    data1 = np.loadtxt('dt_convergence/test_' + str(i) + '.txt')
    data2 = np.loadtxt('dt_convergence/test_' + str(i+1) + '.txt')

    n1 = int(0.5/dt[i])
    n2 = int(0.5/dt[i+1])

    Norm2[i] =  ((1/Nsizes)*np.sum((data1[n1,0::2]-data2[n2,:])**2))**0.5
    NormMax[i] = np.max(np.abs(data1[n1,0::2]-data2[n2,:]))

    # NormMax[i] = np.max(np.abs(data1[n1,:]-data2[n2,:]))
    # plt.plot(sizes,data[n,:]-sol)
    # plt.show()

print(Norm2[0])
print(NormMax[0])
print(' ')

for i in range(ntests-2):
    print(Norm2[i+1])
    print(NormMax[i+1])
    print(np.log(Norm2[i+1]/Norm2[i]) / np.log(ds[i+1]/ds[i]) )
    print(np.log(NormMax[i+1]/NormMax[i]) / np.log(ds[i+1]/ds[i]) )
    print(' ')

plt.loglog(Norm2)
plt.show()

