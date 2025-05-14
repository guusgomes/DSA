import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)

df_dsa = pd.read_csv('C13/dataset.csv')

df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)
print(df_dsa.dtypes)
print('-' * 100)
print(df_dsa.head())
print('-' * 100)

df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
print(df_dsa.head())
print('-' * 100)

df_ex6 = df_dsa.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
print(df_ex6)