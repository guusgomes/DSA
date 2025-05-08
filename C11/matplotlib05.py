import matplotlib.pyplot as plt
from pylab import *

x = linspace(0, 5, 10)
xx = np.linspace(-0.75, 1., 100)
n = np.array([0, 1, 2, 3, 4, 5])

fig, axes = plt.subplots(1, 4, figsize = (12, 3))

axes[0].scatter(xx, xx + 0.25 * randn(len(xx)), color = 'black')
axes[0].set_title('SCATTER')

axes[1].step(n, n ** 2, lw = 2, color = 'blue')
axes[1].set_title('STEP')

axes[2].bar(n, n ** 2, align = 'center', width = 0.5, alpha = 0.5, color = 'magenta')
axes[2].set_title('BAR')

axes[3].fill_between(x, x ** 2, x ** 3, alpha = 0.5, color = 'green')
axes[3].set_title('FILL BETWEEN');