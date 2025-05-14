import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_dsa = pd.read_csv('C13/dataset.csv')
print(df_dsa.head())
print('-' * 100)

df_ex4 = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)
print(df_ex4)

plt.figure(figsize = (16, 6))
sns.set_palette('coolwarm')
sns.barplot(data = df_ex4,
            y = 'Valor_Venda',
            x = 'Cidade').set(title = '10 cidades com maior Total de Vendas')
plt.xticks(rotation = 70)
plt.show()