import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

choice = int(input('Enter choice(1-4)'))
if choice == 1:
    n = 2
    d = 39
    k = np.arange(0, 121)
elif choice == 2:
    n = 3
    d = 47
    k = np.arange(0, 181)
elif choice == 3:
    n = 2
    d = 29
    k = np.arange(0, 361)
elif choice >= 4:
    n = 3
    d = 17
    k = np.arange(0, 181)

k = k*pi/180
x, y = pol2cart(k*d, np.sin(n*d*k))

fig = plt.figure()
ax = fig.add_subplot(111)

line = Line2D(x, y)
line.set_linewidth(0.5)
ax.add_line(line)
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
plt.axis('equal')
plt.show()
