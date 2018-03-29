import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

t = np.linspace(0, 25*2*pi, 3000)
rad = (0.8*t/(2*pi)+3)
r = rad*(8 + np.sin(t*6+rad/3))
x,y = pol2cart(t, r)
        
fig = plt.figure()
ax = fig.add_subplot(111)

line = Line2D(x, y)
ax.add_line(line)

ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))

plt.axis('equal')
plt.show()
