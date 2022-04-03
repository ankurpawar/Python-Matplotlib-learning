import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

theta = np.linspace(0, 2 * pi, 500);
r = np.ones(500)
x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots()
plt.plot()

line = Line2D(x, y)
ax.add_line(line)

radius = Line2D([0, 0], [0, 1])

ax.add_line(radius)
ax.axis('equal')
ax.set_aspect('equal', 'box')
ax.set_xlim(min(x + x * 0.1), max(x + x * 0.1))
ax.set_ylim(min(y + y * 0.1), max(y + y * 0.1))

def animate(i):
    radius.set_data([0, x[i]],[0, y[i]])
    return radius,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0, 500, 20), \
                                      interval=20, blit=True, repeat=True)

myAnimation.save("circleanim.gif", writer=PillowWriter(fps=24))

plt.show()
