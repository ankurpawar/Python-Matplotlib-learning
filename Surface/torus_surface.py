import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

points = 50

U, V = np.meshgrid(np.linspace(-2*pi, 2*pi, points), np.linspace(-2*pi, 2*pi, points))

x = (7+3*np.cos(V))*np.cos(U)
y = (7+3*np.cos(V))*np.sin(U)
z = 3*np.sin(V)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
ax.set_aspect('equal')
plt.show()
