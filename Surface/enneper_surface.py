import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

##numPoint = 50;
##z = cplxgrid(100);
##x = real(z);
##y = imag(z);
##r = 1.1*abs(z);
##phi = angle(z);
##n = 5;
##rth = linspace(0,2.01*pi,300);
##rradi = 1.1*ones(1,300);
##
##% Surface
##x = r.* cos(phi)-r.^(2*n - 1).*cos((2*n - 1)*phi)./(2*n - 1);
##y = r.* sin(phi)+r.^(2*n - 1).*sin((2*n - 1)*phi)./(2*n - 1);
##z = 2*r.^n.*cos(n.*phi)./n;
##surf(x,y,z,phi);
##
##shading interp
##colormap(spring);
##
##% peripheral lines
##rx = rradi.* cos(rth)-rradi.^(2*n - 1).*cos((2*n - 1)*rth)./(2*n - 1);
##ry = rradi.* sin(rth)+rradi.^(2*n - 1).*sin((2*n - 1)*rth)./(2*n - 1);
##rz = 2*rradi.^n.*cos(n.*rth)./n;
##
##tubeLines = {[rx' ry' rz']};
##daspect([1 1 1])
##h=streamtube(tubeLines,0.2,[1 70]);
##xt=get(h,'xdata');
##yt=get(h,'ydata');
##zt=get(h,'zdata');
##set(h,'edgecolor','none','facecolor',[0.8 0.8 0.8]);
##
##axis equal off
##lighting phong
##camlight headlight
##axis off
##set(gcf,'color',[1 1 1])
points = 100
r = np.linspace(0, 1, points)
theta = np.linspace(-pi, pi, points)

r_arr, t_arr = np.meshgrid(r, theta)

n = 5.0
x = r_arr * np.cos(t_arr) - (r**(2*n - 1))*np.cos((2*n - 1)*t_arr)/(2*n - 1)
y = r_arr * np.sin(t_arr) + (r**(2*n - 1))*np.sin((2*n - 1)*t_arr)/(2*n - 1)
z = (2*r**n)*np.cos(n*t_arr)/n


fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0, antialiased=False)
ax.set_aspect('equal')
plt.show()
