import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


##  Baravelle Spiral
##  This spiral is made from four square.On each step
##  all squares are rotated at pi/4 and scaled down
##  by 1/sqrt(2).
##
##  Four Squares
##  Length is taken as 1.All the vertices and faces of the squares,
##  are kept together.Coordinates are rotated in polar coordinates
##  and drawn in cartesian.This makes the rotation easier.

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(phi, rho)

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

theta = 0
xold = 0
yold = 0
total = 15

x = np.array([[1],
             [0],
             [0]])
y = np.array([[0],
              [0],
              [1]])
t,r = cart2pol(x,y)

patches = []

for n in range(0,total):
    x,y = pol2cart(t+theta,r)
    poly1 = np.hstack((x+xold,y+yold))
    poly2 = np.hstack((-x-xold+2,-y-yold+2))

    polygon1 = Polygon(poly1, True)
    polygon2 = Polygon(poly2, True)
    patches.append(polygon1)
    patches.append(polygon2)
    
    xold = x[-1]+xold
    yold = y[-1]+yold
    theta = theta-pi/4
    r = r/np.sqrt(2.0)

p = PatchCollection(patches)

colors = [5, 3] * total
p.set_array(np.array(colors))

fig, ax = plt.subplots()
ax.add_collection(p)
ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-1.25, 1.25)
plt.axis('equal')
plt.show()
