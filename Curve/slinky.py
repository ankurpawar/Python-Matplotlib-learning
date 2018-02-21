import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

nPoints = 3000

# Prepare arrays x, y, z
theta = np.linspace(0, pi, nPoints)

x = (16 + 2*np.cos(35*pi*2*theta))*np.cos(2*pi*theta);
y = (16 + 2*np.cos(35*2*pi*theta))*np.sin(2*pi*theta);
z = 10*theta+ 2*np.sin(35*2*pi*theta);

plt.axis('equal')
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()

#TODO: tubeplot and ribbon
