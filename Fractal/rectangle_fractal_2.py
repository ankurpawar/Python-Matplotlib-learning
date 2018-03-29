import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


##function recursion10
##%Recursion of simple square
##global COLORMAP
##n=7; %level of recursion
##COLORMAP=copper(n);
##rect(0,0,1,1,n);
##rect(1,0,1,1,n);
##axis([-1.5 1.5 -1 2]);
##axis equal off
##end
##
##function rect(x,y,wide,high,n)
##global COLORMAP
##if n>0
##    xx=[x-wide/2 x+wide/2 x+wide/2  x-wide/2];
##    yy=[y-high/2 y-high/2 y+high/2  y+high/2];
##    patch(xx,yy,'k',...
##        'facecolor',1-COLORMAP(n,:),...
##        'edgecolor',COLORMAP(n,:),'linewidth',1);
##    rect(x-wide/4,y-high/4+high,wide/2,high/2,n-1);
##    rect(x+wide/4,y-high/4+high,wide/2,high/2,n-1);
##end
##end

def fractal_rect(x,y,w,h,patches,n):
    if n > 0 and n < 10:
        xx = np.array([[x-w/2], [x+w/2], [x+w/2], [x-w/2]])
        yy = np.array([[y-h/2], [y-h/2], [y+h/2], [y+h/2]])

        poly = np.hstack((xx,yy))
        polygon = Polygon(poly, True)
        patches.append(polygon)

        rect = fractal_rect(x-w/4,y-h/4,w/2,h/2,patches,n-1)
        rect = fractal_rect(x+w/4,y-h/4,w/2,h/2,patches,n-1)
    return patches

fig, ax = plt.subplots()
patches = []

x = 1.0
y = 1.0
w = 1.0
h = 1.0
n = 7 #depth of recursion

patches = fractal_rect(x,y,w,h,patches,n)


collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3, edgecolor="Black")
#collection.set_array(np.array(colors))
ax.add_collection(collection)
#ax.add_line(line)

plt.axis('equal')
#plt.axis('off')
plt.tight_layout()

plt.show()
