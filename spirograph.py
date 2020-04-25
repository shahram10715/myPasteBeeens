import numpy as np
from matplotlib import pyplot as plt


l = np.random.uniform(0.3, 0.7)
k = np.random.uniform(0.3, 0.7)
xlist = []
ylist = []


for cnt in range(20000):
    xt = (1-k)*np.cos(np.radians(cnt))+l*k*np.cos(np.radians((l-k)/k*cnt))
    yt = (1-k)*np.sin(np.radians(cnt))-l*k*np.sin(np.radians((l-k)/k*cnt))
    xlist.append(xt)
    ylist.append(yt)
    

plt.plot(xlist, ylist)
plt.show()


"""
this is a better solution but still needs some work




from matplotlib import pyplot as plt
import numpy as np


l = np.random.rand()
k = np.random.rand()

xlist = []
ylist = []


x0 = (1-k)*np.cos(np.radians(0))+l*k*np.cos(np.radians((l-k)/k*0))
y0 = (1-k)*np.sin(np.radians(0))-l*k*np.sin(np.radians((l-k)/k*0))

xlist.append(x0)
ylist.append(y0)

xt = (1-k)*np.cos(np.radians(1))+l*k*np.cos(np.radians((l-k)/k*1))
yt = (1-k)*np.sin(np.radians(1))-l*k*np.sin(np.radians((l-k)/k*1))

xlist.append(xt)
ylist.append(yt)

angdeg = 2

while ((np.around(xt, 5) != np.around(x0, 5)) 
       and (np.around(yt, 5) != np.around(y0, 5))):
    xt = (1-k)*np.cos(np.radians(angdeg))+l*k*np.cos(np.radians((l-k)/k*angdeg))
    yt = (1-k)*np.sin(np.radians(angdeg))-l*k*np.sin(np.radians((l-k)/k*angdeg))
    #xlist.append(xt)
    #ylist.append(yt)
    print(xt)
    print(yt)
    angdeg = angdeg + 1
    plt.plot(xt, yt)
    plt.show()


plt.plot(xlist, ylist)
plt.show()
"""
