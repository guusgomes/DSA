import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

df_dsa = pd.read_csv('C14/dataset.csv')
print(df_dsa.shape)
print('-' * 100)
print(df_dsa.columns)
print('-' * 100)
print(df_dsa.head())
print('-' * 100)
print(df_dsa.info())
print('-' * 100)

## ANÁLISE EXPLORATÓRIA - RESUMO ESTATÍSTICO
print(df_dsa.isnull().sum())
print('-' * 100)
print(df_dsa.describe())
print('-' * 100)
print(df_dsa['valor_aluguel'].describe())
print('-' * 100)

sns.histplot(data = df_dsa, x = 'valor_aluguel', kde = True)
plt.show()

print(df_dsa.corr())
print('-' * 100)

sns.scatterplot(data = df_dsa, x = 'area_m2', y = 'valor_aluguel')
plt.show()

y = df_dsa['valor_aluguel']
X = df_dsa['area_m2']
X = sm.add_constant(X)
modelo = sm.OLS(y, X)
resultado = modelo.fit()

print(resultado.summary())

plt.figure(figsize = (12, 8))
plt.xlabel('area_m2', size = 16)
plt.ylabel('valor_aluguel', size = 16)
plt.plot(X['area_m2'], y, 'o', label = 'Dados Reais')
plt.plot(X['area_m2'], resultado.fittedvalues, 'r-', label = 'Linha de Regressão (Previsões do Modelo)')
plt.legend(loc = 'best')
plt.show()