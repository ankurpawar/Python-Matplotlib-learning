import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

def add_triangle(x,y,ax):
    Path = mpath.Path
    codes = [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
    pitch=0.025
    total=130
    for t in range(0, total):
        verts = np.hstack((x, y))
        path = mpath.Path(verts, codes)
        pathpatch = mpatches.PathPatch(path, facecolor=cmap((1.0*t)/total), edgecolor='none', linewidth=0.5)
        ax.add_patch(pathpatch)
        x[3] = pitch*x[1] + (1-pitch)*x[2]
        y[3] = pitch*y[1] + (1-pitch)*y[2]
        x[2] = x[1]
        y[2] = y[1]
        x[1] = x[0]
        y[1] = y[0]
        x[0] = x[3]
        y[0] = y[3]
    return ax

pitch = 0.01
side = 8.0
x = np.array([6, 6+side, 6+side*0.5, 6])
y = np.array([2, 2, 3.0+side*0.5*np.sqrt(3.0), 2])
x1 = 6.0
y1 = 2.0
x2 = x1+side
y2 = 2.0
x3 = x1+side*0.5
y3 = 3.0+side*0.5*np.sqrt(3.0)


fig, ax = plt.subplots()
cmap = matplotlib.cm.get_cmap('Blues')

x_copy = np.copy(x)
y_copy = np.copy(y)
add_triangle(x_copy.reshape(4,1), y_copy.reshape(4,1),ax)

x4 = x[2]+side
y4 = y[2]
add_triangle(np.array([x2, x4, x3, x2]).reshape(4,1)
             ,np.array([y2, y4, y3, y2]).reshape(4,1),ax)

x5 = x2
y5 = y3+side*0.5*np.sqrt(3.0)
add_triangle(np.array([x4, x5, x3, x4]).reshape(4,1)
             ,np.array([y4, y5, y3, y4]).reshape(4,1),ax)

x6 = x1
y6 = y5
add_triangle(np.array([x5, x6, x3, x5]).reshape(4,1)
             ,np.array([y5, y6, y3, y5]).reshape(4,1),ax)

x7 = x3-side
y7 = y3
add_triangle(np.array([x6, x7, x3, x6]).reshape(4,1)
             ,np.array([y6, y7, y3, y6]).reshape(4,1),ax)
add_triangle(np.array([x7, x1, x3, x7]).reshape(4,1)
             ,np.array([y7, y1, y3, y7]).reshape(4,1),ax)

ax.axis('equal')
plt.show()
