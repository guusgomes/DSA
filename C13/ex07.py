import numpy as np
import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)

df_dsa = pd.read_csv('C13/dataset.csv')
print(df_dsa.head())
print('-' * 100)

df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)
print(df_dsa.head())
print('-' * 100)

total = (df_dsa['Desconto'] == 0.15).sum()
print(f'No total {total} vendas receberiam 15% de desconto.')