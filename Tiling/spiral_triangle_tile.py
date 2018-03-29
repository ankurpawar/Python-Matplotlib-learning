import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def trans2d(x,y,tx,ty,phi):
    xx = x*np.cos(phi) - y*np.sin(phi) + tx
    yy = x*np.sin(phi) + y*np.cos(phi) + ty
    return(xx,yy)


num_square = 30
theta = pi/100
phi = pi/3

t = np.linspace(0+phi/2,2*pi+phi/2,4).reshape(4,1)
limb_len = 1
x,y = pol2cart(t,1)

fig, ax = plt.subplots()
cmap = matplotlib.cm.get_cmap('Blues')

Path = mpath.Path
codes = [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]

num_rows = 3
num_cols = 6

for row in range(0,num_rows):
    yoff = 3*row
    for col in range(0,num_cols):
        rot = theta
        xoff = 1.732*col
        limb_len = 1
        x2 = np.copy(x)
        y2 = np.copy(y)
        for n in range(0, num_square):
            verts = np.hstack((limb_len*x2+xoff,limb_len*y2+2+yoff))
            path = mpath.Path(verts, codes)
            pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_square), edgecolor='None', linewidth=0.5)
            ax.add_patch(pathpatch)

            verts = np.hstack((-limb_len*x2+xoff,-limb_len*y2+yoff))
            path = mpath.Path(verts, codes)
            pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_square), edgecolor='None', linewidth=0.5)
            ax.add_patch(pathpatch)

            verts = np.hstack((-limb_len*x2+0.866+xoff,-limb_len*y2+1.5+yoff))
            path = mpath.Path(verts, codes)
            pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_square), edgecolor='None', linewidth=0.5)
            ax.add_patch(pathpatch)

            verts = np.hstack((limb_len*x2+0.866+xoff,limb_len*y2+0.5+yoff))
            path = mpath.Path(verts, codes)
            pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_square), edgecolor='None', linewidth=0.5)
            ax.add_patch(pathpatch)

            limb_len = limb_len*np.cos(phi)/np.cos(phi-theta)
            x2,y2 = trans2d(x,y,0,0,rot)
            rot = theta+rot

ax.axis('equal')
plt.show()
