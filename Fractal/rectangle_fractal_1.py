import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


##function recursion2
##%recursion2
##global COLORMAP
##n=7 %depth of recursion
##COLORMAP=pink(n)
##x=1
##y=1
##w=1
##h=1
##rect(x,y,w,h,n)
##axis([0 2 0 2])
##axis equal off
##end
##
##function rect(x,y,w,h,n)
##global COLORMAP
##if n>0
##    xx=[x-w/2 x+w/2 x+w/2  x-w/2]
##    yy=[y-h/2 y-h/2 y+h/2  y+h/2]
##
##    rect(x-w/2,y-h/2,w/2,h/2,n-1)
##    rect(x-w/2,y+h/2,w/2,h/2,n-1)
##    rect(x+w/2,y-h/2,w/2,h/2,n-1)
##    rect(x+w/2,y+h/2,w/2,h/2,n-1)
##    
##    patch(xx,yy,n*ones(size(yy))*0,'k',...
##         'facecolor',COLORMAP(n,:),'edgecolor','none')
##end
##end

def fractal_rect(x,y,w,h,patches,n):
    if n > 0:
        xx = np.array([[x-w/2], [x+w/2], [x+w/2], [x-w/2]])
        yy = np.array([[y-h/2], [y-h/2], [y+h/2], [y+h/2]])

        rect = fractal_rect(x-w/2,y-h/2,w/2,h/2,patches,n-1)
        rect = fractal_rect(x-w/2,y+h/2,w/2,h/2,patches,n-1)
        rect = fractal_rect(x+w/2,y-h/2,w/2,h/2,patches,n-1)
        rect = fractal_rect(x+w/2,y+h/2,w/2,h/2,patches,n-1)

        poly = np.hstack((xx,yy))
        polygon = Polygon(poly, True)
        patches.append(polygon)

    return patches

fig, ax = plt.subplots()
patches = []

x = 1.0
y = 1.0
w = 1.0
h = 1.0
n = 7 #depth of recursion

patches = fractal_rect(x,y,w,h,patches,n)


collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
#collection.set_array(np.array(colors))
ax.add_collection(collection)
#ax.add_line(line)

plt.axis('equal')
#plt.axis('off')
plt.tight_layout()

plt.show()
