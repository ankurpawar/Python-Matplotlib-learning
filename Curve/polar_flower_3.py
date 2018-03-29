import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

theta = np.linspace(0, 2*pi, 1000);

fig = plt.figure()
ax = fig.add_subplot(111)

for rad in range(5, 60, 4):
    r = rad*8.0+(16*np.sin(theta*6+rad*pi/4))
    x,y = pol2cart(theta,r)
    line = Line2D(x, y)
    ax.add_line(line)

ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))

plt.axis('equal')
plt.show()
