import matplotlib.pyplot as plt

plt.plot([1, 3, 5], [2, 4, 7])
plt.show()

x = [2, 3, 5]
y = [2, 5, 7]

plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste plot')
plt.show()

x2 = [1, 2, 3]
y2 = [11, 12, 15]

plt.plot(x2, y2, label = 'Gráfico com Matplotlib')
plt.legend()
plt.show()