import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = Axes3D(fig)

#vertices
vert = np.array([[0,0,2],
    [1,-1,1],
    [1,1,1],
    [-1,1,1],
    [-1,-1,1],
    [2,0,0],
    [0,2,0],
    [-2,0,0],
    [0,-2,0],
    [1,-1,-1],
    [1,1,-1],
    [-1,1,-1],
    [-1,-1,-1],
    [0,0,-2]])

#faces
faces = [[1,0,2,5],
    [8,4,0,1],
    [2,0,3,6],
    [3,0,4,7],
    [8,1,5,9],
    [5,2,6,10],
    [6,3,7,11],
    [7,4,8,12],
    [9,5,10,13],
    [13,10,6,11],
    [13,11,7,12],
    [12,8,9,13]]

polys = [vert[r, :] for r in faces]

ax.add_collection3d(Poly3DCollection(polys, facecolor=(1,0,1), linewidth=1,
                                     edgecolor=(0,0,0)))

ax.set_xlim3d([-4,4])
ax.set_ylim3d([-4,4])
ax.set_zlim3d([-4,4])
ax.set_aspect('equal')
plt.show()
