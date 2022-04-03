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

theta = 0;
dtheta = pi / 25;

fig, ax = plt.subplots()
plt.plot()

xdata, ydata = [], []
trace, = ax.plot([], [], lw=2)

rad = Line2D([0, 0], [0, -1])
ax.add_line(rad)

line = Line2D(x, y)
ax.add_line(line)

ax.axis('equal')
ax.set_aspect('equal', 'box')
ax.set(xlim=(-0, 15), ylim=(-3, 3))

def trans2d(x,y,tx,ty,phi):
    xx = x*np.cos(phi) - y*np.sin(phi) + tx
    yy = x*np.sin(phi) + y*np.cos(phi) + ty
    return(xx,yy)

def get_pos(theta = 0):
    while theta < 4*pi:
        ax = np.array([0, 0])
        bx = np.array([0, -1])
        dx,dy = trans2d(ax, bx, theta,0, -theta)
        yield theta, dx, dy
        theta += dtheta

def animate(pos):
    theta, dx, dy = pos
    line.set_data(x + theta, y)
    rad.set_data(dx, dy)
    xdata.append(dx[1])
    ydata.append(dy[1])
    trace.set_data(xdata, ydata)
    return line, rad, trace

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, get_pos,
                                      interval=20, blit=True, repeat=False)

#myAnimation.save("cycloidanim.gif", writer=PillowWriter(fps=24))

plt.show()
