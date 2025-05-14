import numpy as np
import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)
import matplotlib.pyplot as plt
import seaborn as sns

df_dsa = pd.read_csv('C13/dataset.csv')

df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
df_dsa['Mes'] = df_dsa['Data_Pedido'].dt.month
df_ex9 = df_dsa.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
anos = df_ex9.index.get_level_values(0)
meses = df_ex9.index.get_level_values(1)
segmentos = df_ex9.index.get_level_values(2)

plt.figure(figsize = (12, 6))
sns.set_theme()
fig1 = sns.relplot(kind = 'line',
                   data = df_ex9,
                   y = 'mean',
                   x = meses,
                   hue = segmentos,
                   col = anos,
                   col_wrap = 4)
plt.show()