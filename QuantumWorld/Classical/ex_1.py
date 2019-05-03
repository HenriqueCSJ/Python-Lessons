import numpy as np
import matplotlib.pyplot as plt
import quantumworldX as qw
v = 1.0
dt = 0.001
m = 1
t = np.arange(0,1+dt,dt)
x = np.zeros(len(t))

for i in range(1,len(t)):
    x[i]=x[i-1]+dt*v

qw.time_plot1D(x, t, t_step=30)
plt.show()