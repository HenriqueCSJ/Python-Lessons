import numpy as np
import matplotlib as plt
import scipy as sp

x = np.arange(0, 5, 1)
print(x)

y = np.zeros((5, 5))
print(y)

z = np.arange(0, 25, 1)
print(z)

for xindex in x:
    y[xindex, :] = range(5)
    print(y)