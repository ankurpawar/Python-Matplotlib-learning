import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

points = 75
x, y = np.meshgrid(np.linspace(-5, 5, points), np.linspace(-5, 5, points))

R = np.sqrt(x*x+y*y)
z = (x*np.sin(4*R)+y*np.cos(4*R))/(1+R)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()
