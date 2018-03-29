import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def hexaflake(n,x,y,length,patches):
    if n > 0:
        h = length
        t = np.linspace(0,2*pi,6+1)
        
        #generate points around middle hexagon
        offx,offy = pol2cart(t,h*2*0.866)

        for k in range(0,6):
            xx = h*np.sin(t)+offx[k]+x
            yy = h*np.cos(t)+offy[k]+y
            xx = xx.reshape(-1,1)
            yy = yy.reshape(-1,1)

            poly = np.hstack((xx,yy))
            polygon = Polygon(poly, True)

            patches.append(polygon)
            hexaflake(n-1,x+offx[k],y+offy[k],h/3,patches)

        xx = h*np.sin(t)+x
        yy = h*np.cos(t)+y
        xx = xx.reshape(-1,1)
        yy = yy.reshape(-1,1)
        poly = np.hstack((xx,yy))
        polygon = Polygon(poly, True)
        patches.append(polygon)
        hexaflake(n-1,x,y,h/3,patches)
    return patches

fig, ax = plt.subplots()
n = 4
h = 1.0
patches = []

patches = hexaflake(n,0,0,h,patches)

collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3, edgecolor="Black",facecolor="None")
#collection.set_array(np.array(colors))
ax.add_collection(collection)


plt.axis('equal')
plt.tight_layout()

plt.show()
