import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = Axes3D(fig)

#octahedron vertices
octa_vert = np.array([[1,0,0],
    [-1,0,0],
    [0,1,0],
    [0,-1,0],
    [0,0,1],
    [0,0,-1]])

#octahedron faces
octa_face = [[2,4,1],
    [4,2,0],
    [5,2,1],
    [2,5,0],
    [3,4,0],
    [4,3,1],
    [3,5,1],
    [5,3,0]]

polys = [octa_vert[r, :] for r in octa_face]

ax.add_collection3d(Poly3DCollection(polys, facecolor=(1,0,1), linewidth=1,
                                     edgecolor=(0,0,0)))

ax.set_xlim3d([-2,2])
ax.set_ylim3d([-2,2])
ax.set_zlim3d([-2,2])
ax.set_aspect('equal')
plt.show()
