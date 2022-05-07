import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy import pi
from matplotlib.lines import Line2D
import matplotlib.animation as animation

#Wheels on Wheels on Wheels-Surprising Symmetry, Frank A. Farris
#https://scholarcommons.scu.edu/cgi/viewcontent.cgi?article=1004&context=math_compsci

r = [12, 6, 4]; angle_abc = [-1,-7,17]; phi = pi/2; nRotation = 1; dtheta = pi / 250; maxTheta = 2*pi*nRotation + dtheta
#r = [12, 6, 3]; angle_abc = [-2,5,19]; phi = 0; nRotation = 1; dtheta = pi / 400; maxTheta = 2*pi*nRotation + dtheta
#r = [12, 6, 4]; angle_abc = [-1.5, 2.25, -3.75]; phi = 0; nRotation = 1.5; dtheta = pi / 150; maxTheta = 2*pi*nRotation
#r = [12, 6, 4]; angle_abc = [-1, 3, -7]; phi = 0; nRotation = 1; dtheta = pi / 150; maxTheta = 2*pi*nRotation
#r = [12, 5, 4]; angle_abc = [-1, 5, -7]; phi = pi/2; nRotation = 1; dtheta = pi / 150; maxTheta = 2*pi*nRotation
#r = [9, 5, 2]; angle_abc = [-1, 7, -16]; phi = pi/4; nRotation = 1; dtheta = pi / 150; maxTheta = 2*pi*nRotation
#r = [13, 7, 3]; angle_abc = [3, -3, 16]; phi = 0; nRotation = 1; dtheta = pi / 300; maxTheta = 2*pi*nRotation + dtheta # rotate upto this much radian
#r = [11, 9, 4]; angle_abc = [-3, 5, -7]; phi = 0; nRotation = 1; dtheta = pi / 150; maxTheta = 2*pi*nRotation
#r = [11, 5, 2]; angle_abc = [-2, 7, -9]; phi = 0; nRotation = 1; dtheta = pi / 150; maxTheta = 2*pi*nRotation
#r = [11, 2, 1]; angle_abc = [-1, 13, -19]; phi = 0; nRotation = 1; dtheta = pi / 150; maxTheta = 2*pi*nRotation

r1 = r[0]
r2 = r[1]
r3 = r[2]

t = np.linspace(0, 2 * pi, 100)
x = np.cos(t)
y = np.sin(t)

#Hide toolbar
mpl.rcParams['toolbar'] = 'None'

fig = plt.figure()
ax = plt.axes()

fig.set_figheight(6)
fig.set_figwidth(10)

c1_fix = Line2D(x*r1, y*r1, color='yellowgreen', linewidth = 1)
ax.add_line(c1_fix)
rad1 = Line2D([0, 0], [r1, 0], color='yellowgreen', linewidth = 1)
ax.add_line(rad1)

c2_roll = Line2D(r2*x, r2*y, color='teal', linewidth = 1)
ax.add_line(c2_roll)
rad2 = Line2D([0, 0], [r2, 0], color='teal', linewidth = 1)
ax.add_line(rad2)

c3_roll = Line2D(r3*x, r3*y, color='crimson', linewidth = 1)
ax.add_line(c3_roll)
rad3 = Line2D([0, 0], [r3, 0], color='crimson', linewidth = 1)
ax.add_line(rad3)

xdata, ydata = [], []
trace = Line2D([], [], color='black', linewidth = 1)
ax.add_line(trace)

ax.axis('equal')
ax.set_aspect('equal', 'box')
ax.set(xlim=(-25, 25), ylim=(-25, 25))

ax.set_title('Wheels on wheels on wheels\n'+
             'r1='+str(r1)+', r2='+str(r2)+', r3='+str(r3)+', '+
              r'$\theta1=$'+str(angle_abc[0])+', '+
              r'$\theta2=$'+str(angle_abc[1])+', '+
              r'$\theta3=$'+str(angle_abc[2])+', '+
              r'$\phi=$'+str(phi/pi)+'*pi')

def trans2d(x,y,tx,ty,phi):
    xx = x*np.cos(phi) - y*np.sin(phi) + tx
    yy = x*np.sin(phi) + y*np.cos(phi) + ty
    return(xx,yy)

def get_pos(theta = 0):
    while theta < maxTheta:
        r1x,r1y = trans2d(np.array([0, 0]),np.array([r1, 0]),0,0,angle_abc[0]*theta)
        x2,y2 = trans2d(np.array([0, 0]),np.array([r2, 0]),0,0,angle_abc[1]*theta)
        r2x,r2y = trans2d(x2+r1x[0],y2+r1y[0],0,0,0)
        
        x3,y3 = trans2d(np.array([0, 0]),np.array([r3, 0]),0,0,angle_abc[2]*theta+phi)
        r3x,r3y = trans2d(x3+r2x[0],y3+r2y[0],0,0,0);
        
        yield r1x, r1y, r2x, r2y, r3x, r3y
        theta += dtheta


def animate(pos):
    r1x, r1y, r2x, r2y, r3x, r3y = pos

    rad1.set_data(r1x, r1y)
    rad2.set_data(r2x, r2y)
    rad3.set_data(r3x, r3y)

    xdata.append(r3x[0])
    ydata.append(r3y[0])
    trace.set_data(xdata, ydata)
    c2_roll.set_data(r2*x+r1x[0], r2*y+r1y[0])
    c3_roll.set_data(r3*x+r2x[0], r3*y+r2y[0])

    return c2_roll, c3_roll, rad1, rad2, rad3, trace

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, get_pos,
                                      interval=20, blit=True, repeat=False, save_count=1000)

plt.show()
