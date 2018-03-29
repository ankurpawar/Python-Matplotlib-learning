import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
##
##%% Baravelle Spiral
##% This spiral is made from three triangle.On each step
##% all triangles are rotated at an angle pi/3 and scaled down
##% by 1/2.
##
##%% Three equilateral Traingles
##% Length is taken as 1.Vertices represent an equilateral triangle.
##% Vertices consist of 7 points. O is the centre of the triangle, 
##% A,B,C are the vertex and D,E,F are the centre of edges. 
##% D,E,F are connected to the O.Coordinates are rotated in polar 
##% coordinates and converted to cartesian before they are drawn.
##l = 1; 
##vertices = [0                0;                           %O
##            0                l/(2*sin(pi/3));             %A
##           -l/2             -l/2*tan(pi/6);               %B
##            l/2             -l/2*tan(pi/6);               %C
##           -l/2*cos(pi/3)    l/(2*sin(pi/3))*cos(pi/3)^2; %D
##            0               -l/2*tan(pi/6);               %E 
##            l/2*cos(pi/3)    l/(2*sin(pi/3))*cos(pi/3)^2];%F
##faces = [1 5 2 7;1 6 3 5;1 6 4 7];
##vert = vertices;
##[theta,r] = cart2pol(vertices(:,1),vertices(:,2));
##
##%% Draw the Spiral
##% On each step , rotate each triangle by pi/3
##for k = 0:pi/3:3*pi
##    [vert(:,1),vert(:,2)] = pol2cart(theta-k,r);
##    patch('Vertices',vert,'Faces',faces,...
##          'facecolor','flat','edgecolor','none',...
##          'FaceVertexCData',[1 2 3]');
##    r = r/2;  
##end
##axis equal off

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(phi, rho)

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

a = np.sin(pi/3)
b = np.cos(pi/3)
c = np.tan(pi/6)

verts = np.array([[0,0],
                  [0,1/(2*a)],
                  [-1/2.0, -c/2],
                  [1/2.0, -c/2],
                  [-b/2,(b*b)/(2*a)],
                  [0.0,-c/2],
                  [b/2,(b*b)/(2*a)]],float)

faces = np.array([[0, 4, 1, 6],
                  [0, 5, 2, 4],
                  [0, 5, 3, 6]])

patches = []

theta,r = cart2pol(verts[:,0],verts[:,1])
m = np.arange(0,4*pi,pi/3)

for n in range(0,m.shape[0]):
    verts[:,0],verts[:,1] = pol2cart(theta-m[n],r)
    
    for i in range(0,faces.shape[0]):
        polys = verts[faces[i,],]
        polygon = Polygon(polys, True)
        patches.append(polygon)

    r = r/2

p = PatchCollection(patches)

colors = [1, 3, 5] * m.size
p.set_array(np.array(colors))

fig, ax = plt.subplots()
ax.add_collection(p)
ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-1.25, 1.25)
plt.axis('equal')
plt.show()
