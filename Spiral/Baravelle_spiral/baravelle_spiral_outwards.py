import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

## Outward square Baravelle spiral
## N = 3 triangle
## N = 4 square

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(phi, rho)

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

choice = int(input("Enter 3-4"))

iterations = 15
N = choice
phi = pi/N
t = np.linspace(0+phi, 2*pi+phi, N+1)

A = np.array([[phi],
              [2*phi],
              [3*phi]])

B = np.array([[np.cos(pi/N)],
              [1],
              [np.cos(pi/N)]])

patches = []

offx = 0.0
offy = 0.0

for n in range(0, N):
    limb_len = 1
    theta = 0
    for k in range(0, iterations):
        th = t[n] + theta + A
        ro = limb_len * B

        x,y = pol2cart(th, ro)

        if k == 0:
            offx = x[1]
            offy = y[1]
        
        
        poly = np.hstack((x-offx,y-offy))
        polygon = Polygon(poly, True)
        patches.append(polygon)
        theta = theta+phi
        limb_len = limb_len*np.cos(pi/N)

p = PatchCollection(patches,cmap = plt.cm.gnuplot)

colors = []
for n in range(0,N):
    colors = colors + [n] * iterations
p.set_array(np.array(colors))

fig, ax = plt.subplots()
ax.add_collection(p)
plt.axis('equal')
plt.show()
