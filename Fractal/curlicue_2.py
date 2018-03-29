import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from numpy import pi

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

s = np.log(2)*0.0185
theta = 0
phi = 0
total = 15000
curx = np.zeros((total,1))
cury = np.zeros((total,1))
xn = 0
yn = 0

for n in range(0,total):
    theta = np.fmod(theta+2*pi*s,2*pi)
    phi = np.fmod(phi,2*pi)+theta
    x,y = pol2cart(phi,1)
    xn = x+xn
    yn = y+yn
    curx[n] = xn
    cury[n] = yn

fig = plt.figure()
ax = fig.add_subplot(111)
line = Line2D(curx, cury, linewidth=0.5)
ax.add_line(line)
ax.set_xlim(np.min(curx), np.max(curx))
ax.set_ylim(np.min(cury), np.max(cury))
plt.axis('equal')
plt.show()
