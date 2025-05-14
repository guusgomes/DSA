import pandas as pd
import matplotlib.pyplot as plt

df_dsa = pd.read_csv('C13/dataset.csv')
print(df_dsa.head())

df_ex2 = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()

plt.figure(figsize = (20, 6))
df_ex2.plot(x = 'Data_Pedido',
            y = 'Valor_Venda',
            color = 'green')
plt.title('Total de Vendas por Data do Pedido')
plt.show()