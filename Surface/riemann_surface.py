import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

points = 30
X = np.linspace(-2*pi, 2*pi, points)
Y = np.linspace(-2*pi, 2*pi, points)
X, Y = np.meshgrid(X, Y)
Z = X + Y*1j

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(Z.real, Z.imag, np.abs(Z), rstride=1, cstride=1, cmap=cm.viridis)
ax.set_aspect('equal')
plt.show()
