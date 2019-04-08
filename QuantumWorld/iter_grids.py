import numpy as np

# create variables
x = np.linspace(-np.pi, np.pi, 100)
y = np.zeros(len(x))
# use a for-loop
for index, item in enumerate(x):
    y[index] = (np.square(item)) / (index + 1)
print(y)
