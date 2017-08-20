import numpy as np
import matplotlib.pyplot as plt
# define your function


def square_component(x, omega, k):
    val = (4.0 / np.pi) * np.sin(2 * np.pi * (2 * k - 1) * omega * x) / (2 * k - 1)
    return val


# create variables
omega = 2
x = np.linspace(0, 1, 500)
ks = [1, 2, 3, 4, 5]
y = np.zeros((5, len(x)))
# for-loop it
for indx, k in enumerate(ks):
    y[indx, :] = square_component(x, omega, k)
    plt.plot(x, y[indx, :], label='k=' + str(k))
plt.legend()
plt.ylabel('$y$')
plt.xlabel('$x$')
plt.show()
print(y)