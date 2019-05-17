import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

list(zip(x, y))
plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Ttitle here")

plt.subplot(1, 2, 1)
plt.plot(x, y, "r")
plt.subplot(1, 2, 2)
plt.plot(y, x, "b")

# OO
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_xlabel("X axis")
axes.set_ylabel("Y axis")
axes.set_title("My title here")


fig = plt.figure()
axis1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axis2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axis1.plot(x, y)
axis2.plot(y, x)
axis1.set_title("My big title")

fig, axes = plt.subplots(nrows=1, ncols=2)
#axes.plot(x, y)
# plt.tight_layout()

# for current_ax in axes:
#     current_ax.plot(x, y)
axes[0].plot(x, y)
axes[0].set_title("First")
axes[0].set_xlabel("X1")
axes[0].set_ylabel("Y1")

axes[1].plot(y, x)
axes[1].set_title("Second")
axes[1].set_xlabel("x2")
axes[1].set_ylabel("y2")

fig