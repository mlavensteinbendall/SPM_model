
import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt
from function_LW2 import LW_SPM2

# Check convergence in s-dimension.
# ds0 = 0.005
nsamples = 5
dsvals = np.zeros(nsamples)
dtvals = np.zeros(nsamples)

dsvals[0] = 0.00125
dsvals[1] = 0.0025
dsvals[2] = 0.0050
dsvals[3] = 0.010
dsvals[4] = 0.020

dtvals[0] = 0.00125/2
dtvals[1] = 0.0025/2
dtvals[2] = 0.005/2
dtvals[3] = 0.01/2
dtvals[4] = 0.02/2

filename = 'dt_convergence/'

for i,dsi in enumerate(dsvals):

    print('Entering loop ' + str(i))
    LW_SPM2(dsi,dtvals[i],i,filename)
    print('S Loop ' + str(i) + ' Complete.')

# Check convergence in t-dimension

# ds0 = 0.005
# nsamples = 8
# dsvals = np.zeros(nsamples); dt = np.zeros(nsamples)
# for n in range(nsamples): dsvals[n] = ds0*(2**(n)); dt[n] = dsvals[n]*0.9

# filename = 'dt_convergence/'

# for i,dsi in enumerate(dsvals):

#     dti = dt[i]
#     print('Entering loop ' + str(i))
#     LW_SPM2(dsi,dti,i,filename)
#     print('T Loop ' + str(i) + ' Complete.')
