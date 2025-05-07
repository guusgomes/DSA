from pandas import DataFrame

dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2006, 2007, 2008],
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

df = DataFrame(dados)

print(df.head)
print(type(df))
print(DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano']))
print('-' * 60)

df2 = DataFrame(dados,
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

print(df2.columns)
print(df2['Estado'])
print(df2.values)
print(df2.dtypes)
print(df2[['Taxa Desemprego', 'Ano']])
print(df2.index)
print(df2.filter(items = ['estado3'], axis = 0))
print('-' * 60)

print(df2.describe())
print(df2.isna())
print(df2['Taxa Crescimento'].isna())
print('-' * 60)

import numpy as np

df2['Taxa Crescimento'] = np.arange(5.)

print(df2)
print(df2.describe())
print('-' * 60)

print(df2['estado2':'estado4'])
print(df2[df2['Taxa Desemprego'] < 2])
print(df2[['Estado', 'Taxa Crescimento']])