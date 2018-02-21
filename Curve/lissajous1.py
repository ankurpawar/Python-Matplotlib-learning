import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# take user input
choice = int(input('Enter choice(1-10):'))

if choice == 1:
    t = np.arange(0, 432, 0.05)
    a = 1.33   #frequency 1
    b = 1.35   #frequency 2
    phi = pi/4 #phase difference
elif choice == 2:
    t = np.arange(300, 500, 0.05)
    a = 2.4    #frequency 1
    b = 3      #frequency 2
    phi = pi/4 #phase difference
elif choice == 3:
    t = np.arange(1, 432, 0.05)
    a = 1.38 #frequency 1
    b = 2.8 #frequency 2
    phi = 0 #phase difference
elif choice == 4:
    t = np.arange(200, 500, 0.05)
    a = 1     #frequency 1
    b = 2.5   #frequency 2
    phi = pi/4 #phase difference
elif choice == 5:
    t = np.arange(80, 499.31, 0.05)
    a = 1   #frequency 1
    b = 2.006   #frequency 2
    phi = pi/4 #phase difference
elif choice == 6:
    t = np.arange(80, 499.31, 0.03)
    a = 1.001   #frequency 1
    b = 3.006   #frequency 2
    phi = pi/4 #phase difference
elif choice == 7:
    t = np.arange(0, 302.31, 0.05)
    a = 1.015   #frequency 1
    b = 2.015   #frequency 2
    phi = pi/10 #phase difference
elif choice == 8:
    t = np.arange(0, 302.31, 0.05)
    a = 2.991   #frequency 1
    b = 2.015   #frequency 2
    phi = pi/4 #phase difference
elif choice == 9:
    t = np.arange(0, 400.31, 0.05)
    a = 1.999   #frequency 1
    b = 1.0001   #frequency 2
    phi = pi/8 #phase difference
elif choice == 10:
    t = np.arange(0, 390, 0.05)
    a = 1.0001   #frequency 1
    b = 2.0001   #frequency 2
    phi = pi/100 #phase difference
    
x = t*np.sin(a*t);
y = t*np.sin(b*t+phi);

plt.plot(x,y)
plt.axis('equal')
plt.show()

