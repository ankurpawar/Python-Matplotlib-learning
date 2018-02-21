import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

choice = int(input('Enter choice(1-4)'))
t = np.arange(0, 2*pi, 0.025)
if choice == 1:
    a = 9
    b = 3
    h = 3
elif choice == 2:
    a = 8
    b = 2
    h = 5
elif choice == 3:
    a = 10
    b = 2
    h = 5
elif choice == 4:
    a = 6
    b = 2
    h = 3
    
x = (a+b)*np.cos(t) - h*np.cos(t*(a+b)/b)
y = (a+b)*np.sin(t) - h*np.sin(t*(a+b)/b)

xc,yc = pol2cart(t,a)


fig = plt.figure()
ax = fig.add_subplot(111)


for n in range(x.shape[0]):
    line = Line2D(np.array([x[n], xc[n]]) , np.array([y[n], yc[n]]))
    line.set_marker('o')
    line.set_markersize(5)
    line.set_markeredgewidth(0)
    line.set_markerfacecolor('#ff00ff')
    ax.add_line(line)


ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
plt.axis('equal')
plt.show()
