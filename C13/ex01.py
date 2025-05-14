import pandas as pd

df_dsa = pd.read_csv('C13/dataset.csv')
print(df_dsa.head())

df_ex1 = df_dsa[df_dsa['Categoria'] == 'Office Supplies']
df_ex1_total = df_ex1.groupby('Cidade')['Valor_Venda'].sum()
cidade_maior_venda = df_ex1_total.idxmax()

print(f'Cidade com maior valor de vendas para "Office Supplies": {cidade_maior_venda}.')