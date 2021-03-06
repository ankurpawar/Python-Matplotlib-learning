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

t = np.linspace(0,2*pi,6).reshape(6,1)
limb_len = 1
x,y = pol2cart(t,1)

num_square = 50
theta = pi/num_square
phi = pi/5

fig, ax = plt.subplots()
cmap = matplotlib.cm.get_cmap('hsv')

Path = mpath.Path
codes = [Path.MOVETO] + [Path.LINETO]*4 + [Path.CLOSEPOLY]

for n in range(0, num_square):
    verts = np.hstack((x, y))
    path = mpath.Path(limb_len*verts, codes)
    pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_square), edgecolor='white', linewidth=0.5)
    ax.add_patch(pathpatch)
    limb_len = limb_len*np.cos(phi)/np.cos(phi-theta)
    x,y = trans2d(x,y,0,0,theta)

ax.axis('equal')
plt.show()
