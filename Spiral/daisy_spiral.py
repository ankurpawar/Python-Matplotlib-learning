import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def get_xy(t, r):
    phi = pi*np.arange(-0.75, 1.25, 0.25)
    x = np.zeros((phi.size,t.size))
    y = np.zeros((phi.size,t.size))
    for n in range(0, phi.size):
        x[n,] = r*np.cos(t+phi[n])
        y[n,] = r*np.sin(t+phi[n])
    return (x, y)


choice = int(input("Enter 1-9"))

if choice == 1:
    t = np.arange(0, 5*pi, np.sqrt(2)/pi)
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 20+8*(x**2+y**2)
    colors = plt.cm.copper
elif choice == 2:
    t = np.arange(0, 5*pi, np.sqrt(pi)/(pi*pi))
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 10+5*(x**2+y**2)
    colors = plt.cm.hsv
elif choice == 3:
    t = np.arange(0, 10*pi, np.sqrt(5*pi)/pi)
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 10+5*(x**2+y**2)
    colors = plt.cm.Pastel2
elif choice == 4:
    t = np.arange(0, 5*pi, 1/np.sqrt(pi))
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 20+15*(x**2+y**2)
    colors = plt.cm.winter
elif choice == 5:
    t = np.arange(0, 5*pi, 1/np.sqrt(pi*pi*pi))
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 10+5*(x**2+y**2)
    colors = plt.cm.RdYlGn
elif choice == 6:
    t = np.arange(0, 5*pi, 1/np.sqrt(2*pi*pi))
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 5+2*(x**2+y**2)
    colors = plt.cm.autumn
elif choice == 7:
    t = np.arange(0, 15*pi, np.exp(1)/np.sqrt(2*pi))
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 5+2*(x**2+y**2)
    colors = plt.cm.PiYG
elif choice == 8:
    golden_ratio = 1.618033988749894848204586
    t = np.arange(0, 10*pi, golden_ratio/np.exp(1))
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 0.5+0.5*(x**2+y**2)
    colors = plt.cm.BrBG
elif choice == 9:
    t = np.arange(0, 20*pi, np.sqrt(2))
    r = np.sqrt(t)
    x, y = get_xy(t, r)
    area = 1+0.5*(x**2+y**2)
    colors = plt.cm.gnuplot

plt.scatter(x, y, s=area, c=area, cmap=colors)
plt.axis('equal')
plt.show()
        
