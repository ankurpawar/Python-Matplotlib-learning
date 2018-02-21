import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from numpy import pi

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

base = 'F'
motif = '-F++F-'
phi = pi/4
max_iteration = 10
limb_len = 1.0

new_base = base
for n in range(0, max_iteration):
    new_base = re.sub('[F]',new_base, motif)

base_len = len(new_base)
n_sections = new_base.count('F')
x_arr = np.zeros(n_sections+1)
y_arr = np.zeros(n_sections+1)
xn = 0
yn = 0
turn_angle = 0
m = 1

for n in range(0, base_len):
    if new_base[n] == 'F':
        xn,yn = pol2cart(turn_angle, limb_len)
        x_arr[m] = xn + x_arr[m-1]
        y_arr[m] = yn + y_arr[m-1]
        m += 1
    elif new_base[n] == '-':
        turn_angle -= phi
    elif new_base[n] == '+':    
        turn_angle += phi

fig = plt.figure()
ax = fig.add_subplot(111)
line = Line2D(x_arr, y_arr, linewidth=0.5)
ax.add_line(line)
ax.set_xlim(np.min(x_arr), np.max(x_arr))
ax.set_ylim(np.min(y_arr), np.max(y_arr))
plt.axis('equal')
plt.show()
