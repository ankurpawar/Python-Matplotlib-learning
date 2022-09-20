import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm

points = 50
u, v = np.meshgrid(np.linspace(-2*pi, 2*pi, points), np.linspace(-2*pi, 2*pi, points))

A = 0.5
B = 1.5
C = 1
x = A*np.cos(u)
y = B*np.cos(v)+A*np.sin(u)
z = C*np.sin(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()