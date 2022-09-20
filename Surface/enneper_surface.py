import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm

points = 100
r = np.linspace(0, 1, points)
theta = np.linspace(-pi, pi, points)

r_arr, t_arr = np.meshgrid(r, theta)

n = 5.0
x = r_arr * np.cos(t_arr) - (r**(2*n - 1))*np.cos((2*n - 1)*t_arr)/(2*n - 1)
y = r_arr * np.sin(t_arr) + (r**(2*n - 1))*np.sin((2*n - 1)*t_arr)/(2*n - 1)
z = (2*r**n)*np.cos(n*t_arr)/n


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))

ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0, antialiased=False)

plt.show()