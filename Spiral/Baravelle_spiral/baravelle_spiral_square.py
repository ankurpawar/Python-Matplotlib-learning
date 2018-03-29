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

verts = np.array([[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1],
                  [-1, 1],
                  [-1, 0],
                  [-1, -1],
                  [0, -1],
                  [1, -1]],float)

faces = np.array([[0, 1, 2, 3],
                  [0, 3, 4, 5],
                  [0, 5, 6, 7],
                  [0, 7, 8, 1]])

patches = []

theta,r = cart2pol(verts[:,0],verts[:,1])
m = np.arange(0,4*pi,pi/4)

for n in range(0,m.shape[0]):
    verts[:,0],verts[:,1] = pol2cart(theta-m[n],r)
    
    for i in range(0,faces.shape[0]):
        polys = verts[faces[i,],]
        polygon = Polygon(polys, True)
        patches.append(polygon)
    r = r/np.sqrt(2.0)

p = PatchCollection(patches)

colors = [1, 3, 5, 7] * m.size
p.set_array(np.array(colors))

fig, ax = plt.subplots()
ax.add_collection(p)
ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-1.25, 1.25)
plt.axis('equal')
plt.show()
