import numpy as np
import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)

df_dsa = pd.read_csv('C13/dataset.csv')
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)
print(df_dsa.head())
print('-' * 100)

df_dsa['Valor_Venda_Desconto'] = df_dsa['Valor_Venda'] - (df_dsa['Valor_Venda'] * df_dsa['Desconto'])
print(df_dsa.head())
print('-' * 100)

df_ex8_vendas_antes_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda']
df_ex8_vendas_depois_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda_Desconto']
media_vendas_antes_desconto = df_ex8_vendas_antes_desconto.mean()
media_vendas_depois_desconto = df_ex8_vendas_depois_desconto.mean()

print(f'Média das vendas antes do desconto de 15%: {round(media_vendas_antes_desconto, 2)}.')
print(f'Média das vendas depois do desconto de 15%: {round(media_vendas_depois_desconto, 2)}.')