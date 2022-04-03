import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D

def get_ferris_wheel(curve_const, curve_range):
    t = np.linspace(curve_range[0], curve_range[1], 1000)

    z = np.exp(complex(0,curve_const[0])*t)      \
        + np.exp(complex(0,curve_const[1])*t)/2  \
        + np.exp(complex(0,curve_const[2])*t)/3
    y = z.real
    x = z.imag

    return (x,y)


curve_const = np.array([1, 7, -17])
curve_range = np.array([0, 2*pi])

x, y = get_ferris_wheel(curve_const, curve_range)

fig = plt.figure()
ax = fig.add_subplot(111)


line = Line2D(x, y)
ax.add_line(line)


ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
plt.axis('equal')
plt.show()
