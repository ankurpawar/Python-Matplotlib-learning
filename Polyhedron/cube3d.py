import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d as mplot3

fig = plt.figure()
ax = Axes3D(fig)

cube_verts = np.array([[0,0,0],
    [1,0,0],
    [1,1,0],
    [0,1,0],
    [0,0,1],
    [1,0,1],
    [1,1,1],
    [0,1,1]])

cube_face = [[0,1,2,3],
    [0,1,5,4],
    [1,2,6,5],
    [0,3,7,4],
    [2,6,7,3],
    [4,5,6,7]]


polys = [cube_verts[k, :] for k in cube_face]

ax.add_collection3d(Poly3DCollection(polys, facecolor=(1,0,1), linewidth=0.5,
                                     edgecolor=(0,0,0)))
ax.set_xlim3d([0,2])
ax.set_ylim3d([0,2])
ax.set_zlim3d([0,2])
ax.set_aspect('equal')
plt.show()
