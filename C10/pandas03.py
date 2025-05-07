import pandas as pd

dsa_df = pd.read_csv('C10/dataset.csv')

print(dsa_df.head())
print('-' * 60)
print(dsa_df['ID_Pedido'].head())
print('-' * 60)
print(dsa_df['ID_Pedido'].str.split('-'))
print('-' * 60)
print(dsa_df['ID_Pedido'].str.split('-').str[1].head())
print('-' * 60)

dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]

print(dsa_df.head())
print('-' * 60)

print(dsa_df['Data_Pedido'].head(3))
print('-' * 60)
print(dsa_df['Data_Pedido'].str.lstrip('20'))
print('-' * 60)

dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')

print(dsa_df.head())
print('-' * 60)

dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-')

print(dsa_df.head())