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

N = 6
t = np.linspace(0+pi/6,2*pi+pi/6,N+1).reshape(N+1,1)
limb_len = 1
x,y = pol2cart(t,1)

offx1 = 2*np.cos(pi/6)
offx2 = np.cos(pi/6)
offy2 = 1+np.sin(pi/6)

total = 9

fig, ax = plt.subplots()
cmap = matplotlib.cm.get_cmap('Set3_r')

Path = mpath.Path
codes = [Path.MOVETO] + [Path.LINETO]*(N-1) + [Path.CLOSEPOLY]

c = -offx2/2.0
for n in range(0,total):
    c = -c
    for m in range(0,total):
        verts = np.hstack((x+m*offx1+c, y+n*offy2))
        path = mpath.Path(limb_len*verts, codes)
        color_index = ((m+n)%3)/3.0
        pathpatch = mpatches.PathPatch(path, facecolor=cmap(color_index), edgecolor='white', linewidth=1)
        ax.add_patch(pathpatch)
        
ax.axis('equal')
plt.show()
