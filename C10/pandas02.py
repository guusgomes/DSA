import pandas as pd

dsa_df = pd.read_csv('C10/dataset.csv')

print(dsa_df.head(5))
print('-' * 60)
print(dsa_df.isna().sum())
print('-' * 60)

moda = dsa_df['Quantidade'].value_counts().index[0]

print(moda)
print('-' * 60)

dsa_df.fillna({'Quantidade': moda}, inplace = True)

print(dsa_df.isna().sum())
print('-' * 60)

print(dsa_df.Valor_Venda.describe())
print('-' * 60)

df2 = dsa_df.query('229 < Valor_Venda < 10000')

print(df2.Valor_Venda.describe())
print('-' * 60)

df3 = df2.query('Valor_Venda > 766')

print(df3.head())
print('-' * 60)

print(dsa_df.shape)
print('-' * 60)

print(dsa_df[dsa_df['Quantidade'].isin([5, 7, 9, 11])])
print('-' * 60)
print(dsa_df[dsa_df['Quantidade'].isin([5, 7, 9, 11])].shape)
print('-' * 60)
print(dsa_df[dsa_df['Quantidade'].isin([5, 7, 9, 11])][:10])
print('-' * 60)

print(dsa_df[(dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South')].head())
print('-' * 60)
print(dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].tail())
print('-' * 60)
print(dsa_df[(dsa_df.Segmento != 'Home Office') & (dsa_df.Regiao != 'South')].sample(5))
print('-' * 60)

print(dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean())
print('-' * 60)
print(dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))
print('-' * 60)

print(dsa_df.head())
print('-' * 60)
print(dsa_df[dsa_df.Segmento.str.startswith('Con')].head())
print('-' * 60)
print(dsa_df[dsa_df.Segmento.str.endswith('mer')].head())