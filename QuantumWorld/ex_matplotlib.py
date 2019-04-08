import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3.0, 3.0, 500)

y_1 = np.cos(x * 1)
y_2 = np.cos(x * 2)
y_3 = np.cos(x * 3)

plt.plot(x,y_1)
plt.plot(x,y_2)
plt.plot(x,y_3)
plt.show()