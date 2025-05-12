import sqlite3

con = sqlite3.connect('C12/cap12_dsa.db')
cursor = con.cursor()
sql_query = '''SELECT name FROM sqlite_master WHERE type = 'table';'''
cursor.execute(sql_query)
print(cursor.fetchall())
print('-' * 100)

query1 = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query1)

nome_colunas = [description[0] for description in cursor.description]
print(nome_colunas)
print('-' * 100)

dados = cursor.fetchall()
print(dados)
print('-' * 100)

query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'
cursor.execute(query2)
print(cursor.fetchall())
print('-' * 100)

query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'
cursor.execute(query3)
print(cursor.fetchall())
print('-' * 100)

query4 = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto'''
cursor.execute(query4)
rst4 = cursor.fetchall()
for v in rst4:
    print(v)

print('-' * 100)

query5 = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            Group by Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10'''
cursor.execute(query5)
rst5 = cursor.fetchall()
for p in rst5:
    print(p)

cursor.close()
con.close()