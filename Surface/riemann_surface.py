import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm

points = 30
X = np.linspace(-2*pi, 2*pi, points)
Y = np.linspace(-2*pi, 2*pi, points)
X, Y = np.meshgrid(X, Y)
Z = X + Y*1j

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(Z.real, Z.imag, np.abs(Z), rstride=1, cstride=1, cmap=cm.viridis)

plt.show()