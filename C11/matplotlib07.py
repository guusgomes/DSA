import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def ColorMap(phi_m, phi_p):
    return (+ alpha - 2 * np.cos(phi_p) * cos(phi_m) - alpha * np.cos(phi_ext - 2 * phi_p))


phi_m = np.linspace(0, 2 * np.pi, 100)
phi_p = np.linspace(0, 2 * np.pi, 100)
X, Y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(X, Y).T

fig = plt.figure(figsize = (14, 6))

ax = fig.add_subplot(1, 2, 1, projection = '3d')
p = ax.plot_surface(X, Y, Z, rstride = 4, cstride = 4, linewidth = 0)
ax = fig.add_subplot(1, 2, 2, projection = '3d')
p = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
cb = fig.colorbar(p, shrink = 0.5)


fig = plt.figure(figsize = (8, 6))

ax = fig.add_subplot(1, 1, 1, projection = '3d')
p = ax.plot_wireframe(X, Y, Z, rstride = 4, cstride = 4)