import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D
import matplotlib.animation as animation

theta = np.linspace(0, 2*pi, 500);
r = np.ones(500)
x = r * np.cos(theta)
y = r * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111)

line = Line2D(x, y)
ax.add_line(line)

radius = Line2D([0, 0], [0, 1])
ax.add_line(radius)

def animate(i):
    radius.set_data([0, x[i]],[0, y[i]])
    return radius,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0, 500, 20), \
                                      interval=20, blit=True, repeat=True)

ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))

plt.axis('equal')
plt.show()
