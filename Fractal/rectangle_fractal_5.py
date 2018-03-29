import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


##function recursion12
##%Recursion of simple square
##global COLORMAP
##n=8; %level of recursion
##COLORMAP=1-copper(n);
##rect(0,0,1,1,n);
##axis([-0.75 0.75 -0.75 0.75]);
##axis equal off
##end
##
##function rect(x,y,wide,high,n)
##global COLORMAP
##if n>0
##    xx=[x-wide/2 x+wide/2 x+wide/2  x-wide/2];
##    yy=[y-high/2 y-high/2 y+high/2  y+high/2];
##    patch(xx,yy,'k',...
##         'facecolor',COLORMAP(n,:),...
##         'edgecolor','none','linewidth',1);
##    rect(x-wide/4,y-high/4,wide/2,high/2,n-1);
##    rect(x+wide/4,y+high/4,wide/2,high/2,n-1);
##end
##end

def fractal_rect(x,y,w,h,patches,n):
    if n > 0:
        xx = np.array([[x-w/2], [x+w/2], [x+w/2], [x-w/2]])
        yy = np.array([[y-h/2], [y-h/2], [y+h/2], [y+h/2]])

        poly = np.hstack((xx,yy))
        polygon = Polygon(poly, True)
        patches.append(polygon)

        rect = fractal_rect(x-w/4,y-h/4,w/2,h/2,patches,n-1)
        rect = fractal_rect(x+w/4,y+h/4,w/2,h/2,patches,n-1)
    return patches

fig, ax = plt.subplots()
n = 8
patches = []
patches1 = fractal_rect(0.0,0.0,1.0,1.0,patches,n)

collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
#collection.set_array(np.array(colors))
ax.add_collection(collection)
#ax.add_line(line)

plt.axis('equal')
#plt.axis('off')
plt.tight_layout()

plt.show()
