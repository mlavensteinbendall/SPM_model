# Title: Code to generate data which performs a convergence test on the model.
# Author: Stephen Williams
# Notes: Script that can be used to produce the data needed for conv_processing_ scripts.

##

import numpy as np # Numpy for numpy
from function_LW import LW_SPM

# Check convergence in s-dimension.
# ds0 = 0.005
nsamples = 5 # Number of runs
dsvals = np.zeros(nsamples) # Store for ds values.
dtvals = np.zeros(nsamples) # Store for dt values.

## Uncomment for ds test
# ds convergence values
# Set the values for ds
dsvals[0] = 0.005; dsvals[1] = 0.010
dsvals[2] = 0.020; dsvals[3] = 0.025
dsvals[4] = 0.050

# dsvals = dsvals/10

# Set the values for dt
dt = 0.001
## End of ds test section

# ds = np.linspace(0.005,0.020,5)

## Uncomment for dt test
# dt convergence values
# # Set the values for ds
# dsvals[0] = 0.00125; dsvals[1] = 0.0025
# dsvals[2] = 0.0050; dsvals[3] = 0.010
# dsvals[4] = 0.020
# # Set the values for dt
# dtvals[0] = 0.00125/2; dtvals[1] = 0.0025/2
# dtvals[2] = 0.005/2; dtvals[3] = 0.01/2
# dtvals[4] = 0.02/2
## End of dt test section

filename = 'ds_convergence/' # Folder name for data storage.
# filename = 'dt_convergence/' # Folder name for data storage.

# Execute the model for each of the set of pairs of values ds/dt.
for i,dsi in enumerate(dsvals):

    print('Entering loop ' + str(i)) # Progress update, loop start.
    # print("CFL " + str(dt) + "<" + str(np.exp(-0.4)*dsi)) # it seems to be meeing the CFL condition
    # LW_SPM(dsi,dtvals[i],i,filename) # Model - ds run.
    LW_SPM(dsi,dt,i,filename) # Model - dt run.
    print('S Loop ' + str(i) + ' Complete.') # Progress update, loop end.
