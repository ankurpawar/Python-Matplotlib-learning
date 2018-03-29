import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

## generalized baravelle spiral
## N = 3 triangle
## N = 4 square
## N = 5 penatgon
## N = 6 hexagon
## N = 7 heptagon
## N = 8 octagon

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(phi, rho)

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

choice = int(input("Enter 3-8"))

iterations = 25
N = choice
phi = pi/N
t = np.linspace(0+phi, 2*pi+phi, N+1)
limb_len = 1
theta = 0
A = np.array([[phi],
              [2*phi],
              [3*phi]])

B = np.array([[np.cos(pi/N)],
              [1],
              [np.cos(pi/N)]])

patches = []

for k in range(0, iterations):
    for n in range(0, N):
        th = t[n] + theta + A
        ro = limb_len * B
        x,y = pol2cart(th, ro)
        poly = np.hstack((x,y))
        polygon = Polygon(poly, True)
        patches.append(polygon)
    theta = theta+phi
    limb_len = limb_len*np.cos(pi/N)

p = PatchCollection(patches,cmap = plt.cm.Blues)

colors = range(N) * iterations
p.set_array(np.array(colors))

fig, ax = plt.subplots()
ax.add_collection(p)
plt.axis('equal')
plt.show()
