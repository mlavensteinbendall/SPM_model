
import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt
from function_LW2 import LW_SPM2

# Check convergence in s-dimension.

# ds0 = 0.005
# nsamples = 10
# dsvals = np.zeros(nsamples)
# for n in range(nsamples): dsvals[n] = ds0*(n+1)
# dtvals = 0.0025
# filename = 'ds_convergence/'

# for i,dsi in enumerate(dsvals):

#     print('Entering loop ' + str(i))
#     LW_SPM2(dsi,dtvals,i,filename)
#     print('S Loop ' + str(i) + ' Complete.')

# Check convergence in t-dimension

ds0 = 0.005
nsamples = 8
dsvals = np.zeros(nsamples); dt = np.zeros(nsamples)
for n in range(nsamples): dsvals[n] = ds0*(2**(n)); dt[n] = dsvals[n]*0.9

filename = 'dt_convergence/'

for i,dsi in enumerate(dsvals):

    dti = dt[i]
    print('Entering loop ' + str(i))
    LW_SPM2(dsi,dti,i,filename)
    print('T Loop ' + str(i) + ' Complete.')
