import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sea

np.random.seed(42)
n = 1000
pct_smokers = 0.2
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não fumante'})

print(dados.shape)
dados.head()

sea.set(style = 'ticks')
sea.lmplot(x = 'altura',
           y = 'peso',
           data = dados,
           hue = 'flag_fumante',
           palette = ['tab:blue', 'tab:orange'],
           height = 7)

plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso de Fumantes e Não fumantes')

sea.despine()
plt.show()  