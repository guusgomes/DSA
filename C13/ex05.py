import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)
import matplotlib.pyplot as plt

df_dsa = pd.read_csv('C13/dataset.csv')
print(df_dsa.head())
print('-' * 100)

df_ex5 = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False)

print(df_ex5)

plt.pie(df_ex5['Valor_Venda'],
        labels = df_ex5['Segmento'],
        startangle = 90)

centre_circle = plt.Circle((0,0), 0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.annotate(text = f'Total: $ {str(int(sum(df_ex5['Valor_Venda'])))}.', xy = (-0.25, 0))
plt.title('Total de Vendas por Segmento')
plt.show()