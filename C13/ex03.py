import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_dsa = pd.read_csv('C13/dataset.csv')
print(df_dsa.head())

df_ex3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()

plt.figure(figsize = (16, 6))
sns.barplot(data = df_ex3,
            y = 'Valor_Venda',
            x = 'Estado').set(title = 'Vendas Por Estado')
plt.xticks(rotation = 80)
plt.show()