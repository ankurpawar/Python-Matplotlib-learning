import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = Axes3D(fig)

#golden ratio
phi = (1+np.sqrt(5))/2 

#dodechadron vertices
deodeca_vert = np.array([[1,1,1],
    [1,1,-1],
    [1,-1,1],
    [1,-1,-1],
    [-1,1,1],
    [-1,1,-1],
    [-1,-1,1],
    [-1,-1,-1],
    [0,1/phi,phi],
    [0,1/phi,-phi],
    [0,-1/phi,phi],
    [0,-1/phi,-phi],
    [1/phi,phi,0],
    [1/phi,-phi,0],
    [-1/phi,phi,0],
    [-1/phi,-phi,0],
    [phi,0,1/phi],
    [phi,0,-1/phi],
    [-phi,0,1/phi],
    [-phi,0,-1/phi]])

#dodecahedron faces
dedeca_faces = [[0,12,1,17,16],
    [0,8,4,14,12],
    [12,14,5,9,1],
    [1,9,11,3,17],
    [17,16,2,13,3],
    [0,8,10,2,16],
    [4,8,10,6,18],
    [14,4,18,19,5],
    [5,19,7,11,9],
    [19,18,6,15,7],
    [7,11,3,13,15],
    [10,6,15,13,2]]

polys = [deodeca_vert[r, :] for r in dedeca_faces]

ax.add_collection3d(Poly3DCollection(polys, facecolor=(1,0,1), linewidth=1,
                                     edgecolor=(0,0,0)))

ax.set_xlim3d([-2,2])
ax.set_ylim3d([-2,2])
ax.set_zlim3d([-2,2])
ax.set_aspect('equal')
plt.show()
