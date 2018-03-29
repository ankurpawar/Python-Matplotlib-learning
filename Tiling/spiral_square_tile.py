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

t = np.linspace(0+pi/4,2*pi+pi/4,5).reshape(5,1)
limb_len = 1
x,y = pol2cart(t,1)

num_square = 50
theta = pi/100
phi = pi/4

fig, ax = plt.subplots()
cmap = matplotlib.cm.get_cmap('Blues')

Path = mpath.Path
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]

#Number of rows and columns for tile
num_rows = 4
num_cols = 6

for row in range(0,num_rows):
    for col in range(0,num_cols):
        xoff = col*1.414
        yoff = row*1.414
        limb_len = 1.0
        x,y = pol2cart(t,1)
        for n in range(0, num_square):
            verts = np.hstack((limb_len*x+xoff, limb_len*y+yoff))
            path = mpath.Path(verts, codes)
            pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_square), edgecolor='None', linewidth=0.5)
            ax.add_patch(pathpatch)
            limb_len = limb_len*np.cos(phi)/np.cos(phi-theta)
            x,y = trans2d(x,y,0,0,theta)

ax.axis('equal')
plt.show()
