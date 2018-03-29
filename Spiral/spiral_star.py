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

# spiral Star
# number of sides of polygon
# N = 3 triangle, N = 4 square, N = 5 penatgon, N = 6 hexagon
poly_type = int(input("Enter 3-6"))
num_poly = int(input("Enter 25-80"))

theta = pi/100
phi = pi/poly_type

t = np.linspace(0,2*pi,poly_type+1).reshape(poly_type+1,1)

cmap = matplotlib.cm.get_cmap('Blues')

Path = mpath.Path
codes = [Path.MOVETO] + [Path.LINETO]*(poly_type-1) + [Path.CLOSEPOLY]


plt.figure(1)
ax1 = plt.gca()
limb_len = 1
x,y = pol2cart(t,1)
for n in range(0, num_poly):
    verts = np.hstack((limb_len*x, limb_len*y))
    path = mpath.Path(verts, codes)
    pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_poly), edgecolor='None', linewidth=0.5)
    ax1.add_patch(pathpatch)

    verts = np.hstack((limb_len*x, -limb_len*y))
    path = mpath.Path(verts, codes)
    pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_poly), edgecolor='None', linewidth=0.5)
    ax1.add_patch(pathpatch)
    
    limb_len = limb_len*np.cos(phi)/np.cos(phi-theta)
    x,y = trans2d(x,y,0,0,theta)

ax1.axis('equal')

plt.figure(2)
ax2 = plt.gca()
limb_len = 1
x,y = pol2cart(t,1)
for n in range(0, num_poly):
    verts = np.hstack((limb_len*x, limb_len*y))
    path = mpath.Path(verts, codes)
    pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_poly), edgecolor='None', linewidth=0.5)
    ax2.add_patch(pathpatch)

    verts = np.hstack((-limb_len*x, -limb_len*y))
    path = mpath.Path(verts, codes)
    pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*n)/num_poly), edgecolor='None', linewidth=0.5)
    ax2.add_patch(pathpatch)
    
    limb_len = limb_len*np.cos(phi)/np.cos(phi-theta)
    x,y = trans2d(x,y,0,0,theta)

ax2.axis('equal')

plt.show()
