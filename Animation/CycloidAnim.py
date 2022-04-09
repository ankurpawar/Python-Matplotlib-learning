import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from fractions import Fraction

theta = np.linspace(0, 2 * pi, 500);
r = np.ones(500)
x = r * np.cos(theta)
y = r * np.sin(theta)

dtheta = pi / 25;

# Distance of point on radius from center.
# P < 1 then trochoid, P >= 1 cycloid
P = 1

fig = plt.figure()
ax = plt.axes()

fig.set_figheight(7)
fig.set_figwidth(14)

xdata, ydata = [], []
trace = Line2D([], [], color='blue', linewidth = 3)
ax.add_line(trace)

rad = Line2D([0, 0], [0, -P], color='red', linewidth = 3)
ax.add_line(rad)

line = Line2D(x, y, color='green', linewidth = 3)
ax.add_line(line)

ax.axis('equal')
ax.set_aspect('equal', 'box')
ax.set(xlim=(-1.5, 14), ylim=(-1, 4))
ax.grid(color='blue', linewidth = 0.5, linestyle = 'dotted')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_title('Cycloid animation')

def format_func(value, tick_number):
    n = Fraction(value / pi).numerator
    d = Fraction(value / pi).denominator
    if n == 0:
        return "0"
    elif n == 1 and d == 1:
        return r"$\pi$"
    elif n == 1 and d != 1:
        return r"$\pi/{0}$".format(d)
    elif n != 1 and d == 1:
        return r"${0}\pi$".format(n)
    else:
        return r"${0}\pi/{1}$".format(n, d)

def trans2d(x,y,tx,ty,phi):
    xx = x*np.cos(phi) - y*np.sin(phi) + tx
    yy = x*np.sin(phi) + y*np.cos(phi) + ty
    return(xx,yy)

def init():
    trace.set_data([], [])
    rad.set_data([0, 0], [0, -P])
    line.set_data([], [])
    return line, rad, trace
    
def get_pos(theta = 0):
    while theta < 4*pi:
        ax = np.array([0, 0])
        by = np.array([0, -P])
        dx,dy = trans2d(ax, by, theta, 1, -theta)
        yield theta, dx, dy
        theta += dtheta

def animate(pos):
    theta, dx, dy = pos
    line.set_data(x + theta, y + 1)
    rad.set_data(dx, dy)
    xdata.append(dx[1])
    ydata.append(dy[1])
    trace.set_data(xdata, ydata)
    return line, rad, trace

ax.xaxis.set_major_locator(plt.MultipleLocator(pi / 2))
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, get_pos,
                                      interval=20, blit=True, repeat=False, init_func=init)

plt.show()
