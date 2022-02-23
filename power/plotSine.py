import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
z = np.sin(x+np.pi/2)
w = np.zeros(np.shape(x))

plt.plot(x, y, label = r'Sin$\theta$')
plt.plot(x, z, label = r'Cos$\theta$')
#plt.plot(x, w)

plt.xlabel(r'$\theta(radians)$')
plt.ylabel('Function value')
plt.title(r'Sin$\theta$ & Cos$\theta$')
plt.legend()
plt.show()
