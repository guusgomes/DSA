import matplotlib.pyplot as plt
from pylab import *

x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()
axes = fig.add_axes([0, 0, 0.8, 0.8])

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha');


x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária');


x = linspace(0, 5, 10)
y = x ** 2

fig, axes = plt.subplots(nrows = 1, ncols = 2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')

fig.tight_layout()


x = linspace(0, 5, 10)
y = x ** 2

fig, axes = plt.subplots(1, 2, figsize = (10, 4))

axes[0].plot(x, x ** 2, x, exp(x))
axes[0].set_title('Escala Padrão')

axes[1].plot(x, x ** 2, x, exp(x))
axes[1].set_yscale('log')
axes[1].set_title('Escala Logaritmica (y)');


x = linspace(0, 5, 10)
y = x ** 2

fig, axes = plt.subplots(1, 2, figsize = (10, 3))

axes[0].plot(x, x ** 2, x ** 3, lw = 2)
axes[0].grid(True)

axes[1].plot(x, x ** 2, x ** 3, lw = 2)
axes[1].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8)


