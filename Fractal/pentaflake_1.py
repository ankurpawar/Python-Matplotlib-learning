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

def pentaflake(n,x,y,theta,length,patches):
    if n > 0:
        golden = 1.618033988749894848204586
        d = length /golden
        h = length
        t = np.linspace(0+theta,2*pi+theta,5+1)
        
        #generate points around middle pentagon
        offx,offy = pol2cart(t+18*pi/180,d*(1+golden))

        for k in range(0,5):
            xx = h*np.sin(t)+offx[k]+x
            yy = h*np.cos(t)+offy[k]+y
            xx = xx.reshape(-1,1)
            yy = yy.reshape(-1,1)

            poly = np.hstack((xx,yy))
            polygon = Polygon(poly, True)

            patches.append(polygon)
            pentaflake(n-1,x+offx[k],y+offy[k],theta,length/(golden+1),patches)

        xx = h*np.sin(t)+offx[4]+x
        yy = h*np.cos(t)+offy[4]+y
        xx = xx.reshape(-1,1)
        yy = yy.reshape(-1,1)
        poly = np.hstack((xx,yy))
        polygon = Polygon(poly, True)
        patches.append(polygon)
        pentaflake(n-1,x,y,pi+theta,length/(golden+1),patches)
    return patches

fig, ax = plt.subplots()
n = 4
h = 1.0
patches = []
golden = 1.618033988749894848204586 #golden ratio

patches = pentaflake(n,0,0,36*pi/180,h,patches)

collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3, edgecolor="Black",facecolor="None")
#collection.set_array(np.array(colors))
ax.add_collection(collection)


plt.axis('equal')
plt.tight_layout()

plt.show()
