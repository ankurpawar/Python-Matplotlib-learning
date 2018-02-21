import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from numpy import pi

def pol2cart(phi, rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

base = np.array([0, pi/2, pi/2, pi/2])

motif = np.array([85, -170, 85])*pi/180

max_iteration = 5

angle_new = np.array([])


# Prepare motif
for n in range(0, max_iteration):
    angle_new = np.hstack((angle_new, motif[0],
        angle_new, motif[1],
        angle_new, motif[2],
        angle_new))

# Prepare base
angle_new = np.hstack((base[0], angle_new,
    base[1], angle_new, base[2], angle_new,
    base[3], angle_new, 0))

len_angle = angle_new.size
x_arr = np.zeros((len_angle,1))
y_arr = np.zeros((len_angle,1))
x = 0
y = 0
xn = 0
yn = 0
motif = 0
#length of each section
limb_len = 1

for n in range(0, len_angle):
    xn,yn = pol2cart(motif, limb_len)
    motif = angle_new[n]+motif
    x = x + xn
    y = y + yn
    x_arr[n] = x
    y_arr[n] = y

fig = plt.figure()
ax = fig.add_subplot(111)
line = Line2D(x_arr, y_arr, linewidth=0.5)
ax.add_line(line)
ax.set_xlim(np.min(x_arr), np.max(x_arr))
ax.set_ylim(np.min(y_arr), np.max(y_arr))
plt.axis('equal')
plt.show()
