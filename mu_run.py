# Title: Code to generate data which performs a convergence test on the model.
# Author: Stephen Williams
# Notes: Script that can be used to produce the data needed for conv_processing_ scripts.

##

import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt
from function_LW2 import LW_SPM2

# Check convergence in s-dimension.
# ds0 = 0.005
nsamples = 5 # Number of runs
dsvals = np.zeros(nsamples) # Store for ds values.
dtvals = np.zeros(nsamples) # Store for dt values.

dsi = 0.005
dt = 0.001
## End of ds test section

filename = 'mu_test/' # Folder name for data storage.

print('Entering loop ' + str(11)) # Progress update, loop start.
N = LW_SPM2(dsi,dt,11,filename) # Model - dt run.
print('S Loop ' + str(0) + ' Complete.') # Progress update, loop end.


