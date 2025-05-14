import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)
import matplotlib.pyplot as plt

df_dsa = pd.read_csv('C13/dataset.csv')
df_ex10 = df_dsa.groupby(['Categoria',
                          'SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda',
                                                                                ascending = False).head(12)
df_ex10 = df_ex10[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()
print(df_ex10)
print('-' * 100)

df_ex10_cat = df_ex10.groupby('Categoria').sum(numeric_only = True).reset_index()
print(df_ex10_cat)
print('-' * 100)

cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']
cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']

fig, ax = plt.subplots(figsize = (18, 12))

p1 = ax.pie(df_ex10_cat['Valor_Venda'],
            radius = 1,
            labels = df_ex10_cat['Categoria'],
            wedgeprops = dict(edgecolor = 'white'),
            colors = cores_categorias)

p2 = ax.pie(df_ex10['Valor_Venda'],
            radius = 0.9,
            labels = df_ex10['SubCategoria'],
            colors = cores_subcategorias,
            labeldistance = 0.7,
            wedgeprops = dict(edgecolor = 'white'),
            pctdistance = 0.53,
            rotatelabels = True)

centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df_ex10['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas por categoria e Top 12 subcategorias')
plt.show()