import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def get_supershape(curve_const, curve_range):
    t = np.linspace(curve_range[0], curve_range[1], 1000)

    a = curve_const[0]
    b = curve_const[1]
    m = curve_const[2]
    n1 = curve_const[3]
    n2 = curve_const[4]
    n3 = curve_const[5]
    r = 1/((np.abs(1/a*np.cos(0.25*m*t))**n2 \
             + np.abs(1/b*np.sin(0.25*m*t))**n3)**(1/n1))
    
    x, y = pol2cart(t, r)

    return (x,y)


curve_const = np.array([1, 1, 6, 0.4, 0, 6])
curve_range = np.array([0, 2*pi])

x, y = get_supershape(curve_const, curve_range)

fig = plt.figure()
ax = fig.add_subplot(111)


line = Line2D(x, y)
ax.add_line(line)


ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
plt.axis('equal')
plt.show()
