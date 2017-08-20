# preloaded
import numpy as np
# exercise
# import ..
import scipy as sp
import scipy.integrate
import scipy.linalg

v = np.array([2.5, 0])
w = np.array([0, 0.45])
x = np.linspace(0, 1, 100)
y = np.cos(x)
A = np.array([[0.8, 0.25], [0.25, 0.7]])
# calculate stuff
vw_dot = np.vdot(v, w)
v_norm = sp.linalg.norm(v)
w_norm = sp.linalg.norm(w)
area_quad, error = sp.integrate.quad(np.cos, 0, 1.0)
area_simps = sp.integrate.simps(y, x)
area_diff = np.abs(area_quad - area_simps)
e_vals = sp.linalg.eigvalsh(A)
