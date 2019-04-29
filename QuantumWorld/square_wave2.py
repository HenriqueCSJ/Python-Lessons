import numpy as np
import matplotlib.pyplot as plt
# define your function


def square_component(x, omega, k):
    val = (4.0 / np.pi) * np.sin(2 * np.pi *
                                 (2 * k - 1) * omega * x) / (2 * k - 1)
    return val
# define your function around here


def square_approx(x, omega, n):
    val = np.zeros(len(x))
    for k in range(1, n + 1):
        val = val + square_component(x, omega, k)
    return val


# initial variables
omega = 2
x = np.linspace(0, 1, 500)
ns = [1, 2, 8, 32, 128, 512]
y = np.zeros((6, len(x)))
# for-loop it
for indx, n in enumerate(ns):
    y[indx, :] = square_approx(x, omega, n)
    plt.plot(x, y[indx, :], label='n=' + str(n))

plt.legend()
plt.ylabel('$y$')
plt.xlabel('$x$')
plt.title('Square wave approximated')
plt.show()
