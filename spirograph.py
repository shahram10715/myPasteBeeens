"""
for more information read the following page:
https://en.wikipedia.org/wiki/Spirograph
"""

from matplotlib import pyplot as plt
import numpy as np

l = np.random.rand()
k = np.random.rand()
l = np.around(l, 2)
k = np.around(k, 2)
xlist = []
ylist = []

def xtfunc(ang):
    return ((1-k)*np.cos(np.radians(ang)) + l*k*np.cos((1-k)/k*np.radians(ang)))

def ytfunc(ang):
    return ((1-k)*np.sin(np.radians(ang)) - l*k*np.sin((1-k)/k*np.radians(ang)))

x0 = xtfunc(0)
y0 = ytfunc(0)
xlist.append(x0)
ylist.append(y0)

while True:
    ang = len(xlist)
    xt = xtfunc(ang)
    yt = ytfunc(ang)
    xlist.append(xt)
    ylist.append(yt)
    if (ang%360 == 0):
        if (np.around(xt, 3) == np.around(x0, 3)):
            break
    
print('k= ', k)
print('l= ', l)
plt.plot(xlist, ylist)
plt.show()
