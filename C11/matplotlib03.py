import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 5, 6, 8, 4, 8]

plt.scatter(x, y, label = 'Pontos', color = 'black', marker = 'o')
plt.legend()
plt.show()


dias = [1, 2, 3, 4, 5]
dormir = [7, 8, 6, 77, 7]
comer = [2, 3, 4, 5, 3]
trabalhar = [7, 8, 7, 2, 2]
passear = [8, 5, 7, 8, 13]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m', 'c', 'r', 'k', 'b'])
plt.show()


fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']

plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode = (0, 0.2, 0, 0))
plt.show()