import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib import colors as mcolors

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(phi, rho)

def trans2d(x,y,tx,ty,phi):
    theta,rad = cart2pol(x,y)
    xx = rad*np.cos(theta+phi)+tx
    yy = rad*np.sin(theta+phi)+ty
    return(xx,yy)

def pytree(x,y,theta,n,fig,ax):
    if n > 0:
        xx,yy = trans2d(x,y,0,0,pi/4)
        pytree(xx*0.707-1,yy*0.707+2,theta+pi/4,n-1,fig,ax)
        xx,yy = trans2d(x,y,0,0,-pi/4)
        pytree(xx*0.707+1,yy*0.707+2,theta+pi/4,n-1,fig,ax)

        verts = [
        (x[0], y[0]), # left, bottom
        (x[1], y[1]), # left, top
        (x[2], y[2]), # right, top
        (x[3], y[3]), # right, bottom
        (x[0], y[0]), # ignored
        ]
        
        codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

        path = Path(verts, codes)

        phi = np.mod(np.arctan2(y[1],x[1])+pi,pi)/pi
        fcolor = mcolors.hsv_to_rgb([phi, 1 ,1])

        patch = patches.PathPatch(path,facecolor=fcolor, lw=0)
        ax.add_patch(patch)
        
x = np.array([-1, 1, 1, -1])
y = np.array([-1, -1, 1, 1])
level = 10
fig = plt.figure()
ax = fig.add_subplot(111)
pytree(x,y,0,level,fig,ax)
ax.set_xlim(-7.5,7.5)
ax.set_ylim(-1.5,8)
ax.set_aspect('equal')
plt.show()
