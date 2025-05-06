import numpy as dsa
import os
import matplotlib.pyplot as plt

filename = os.path.join('C09A01/dataset.csv')
arr13 = dsa.loadtxt(filename, delimiter = ',', usecols = (0, 1, 2, 3), skiprows = 1)

print(arr13)
print(type(arr13))

var1, var2 = dsa.loadtxt(filename, delimiter = ',', usecols = (0, 1), skiprows = 1, unpack = True)

plt.show(plt.plot(var1, var2, 'o', markersize = 6, color = 'red'))