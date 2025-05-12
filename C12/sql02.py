import sqlite3
import pandas as pd

con = sqlite3.connect('C12/cap12_dsa.db')
cursor = con.cursor()

query = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados, columns = ['ID_Pedido',
                                    'ID_Cliente',
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])
print(df.head(10))
print('-' * 100)

cursor.close()
con.close()

media_unidades_vendidas = df['Unidades_Vendidas'].mean()
print(media_unidades_vendidas)
print('-' * 100)

media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(media_unidades_vendidas_por_produto.head(10))
print('-' * 100)

registros_valor_unitario_maior_199 = df[df['Valor_Unitario'] > 199]
print(registros_valor_unitario_maior_199)
print('-' * 100)

print(df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean())
print('-' * 100)

print(df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10))
print('-' * 100)

print(df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                                    .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                                    .groupby('Nome_Produto')['Unidades_Vendidas'].mean())