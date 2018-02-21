import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = Axes3D(fig)

#golden ratio
phi = (1+np.sqrt(5))/2 

#icosahedron vertices
icosa_verts = np.array([[0,1,phi],
    [0,1,-phi],
    [0,-1,phi],
    [0,-1,-phi],
    [1,phi,0],
    [1,-phi,0],
    [-1,phi,0],
    [-1,-phi,0],
    [phi,0,1],
    [phi,0,-1],
    [-phi,0,1],
    [-phi,0,-1]])

#icosahedron faces
icosa_face = [[0,4,8],
    [5,2,8],
    [0,2,10],
    [2,0,8],
    [6,1,4],
    [6,0,10],
    [0,6,4],
    [9,5,8],
    [4,9,8],
    [1,9,4],
    [9,3,5],
    [3,9,1],
    [3,7,5],
    [2,7,10],
    [7,2,5],
    [6,11,1],
    [11,3,1],
    [11,6,10],
    [7,11,10],
    [11,7,3]]

polys = [icosa_verts[r, :] for r in icosa_face]

ax.add_collection3d(Poly3DCollection(polys, facecolor=(1,0,1), linewidth=1,
                                     edgecolor=(0,0,0)))

ax.set_xlim3d([-2,2])
ax.set_ylim3d([-2,2])
ax.set_zlim3d([-2,2])
ax.set_aspect('equal')
plt.show()
