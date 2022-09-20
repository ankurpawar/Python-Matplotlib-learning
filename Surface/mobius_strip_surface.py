import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm

points = 50
u, v = np.meshgrid(np.linspace(0, 2*pi, points), np.linspace(-0.8, 0.8, points))

twist = 3

x = np.sin(u)*(2-v*np.sin(twist*u/2))
y = np.cos(u)*(2-v*np.sin(twist*u/2))
z = v*np.cos(twist*u/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.gray)

plt.show()