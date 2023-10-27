
import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

data1 = np.loadtxt('dt_convergence/test_' + str(0) + '.txt') 

plt.plot(data1[-1,:])
plt.show()
