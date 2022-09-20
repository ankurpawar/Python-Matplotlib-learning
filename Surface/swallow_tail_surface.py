import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm

points = 50
u, v = np.meshgrid(np.linspace(-2, 2, points), np.linspace(-0.8, 0.8, points))

x = u*(v**2) + 3*(v**4)
y = -2*u*v - 4*(v**3)
z = u

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.gray)

plt.show()