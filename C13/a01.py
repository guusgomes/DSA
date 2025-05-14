import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_dsa = pd.read_csv('C13/dataset.csv')

print(df_dsa.shape)
print('-' * 100)
print(df_dsa.head())
print('-' * 100)
print(df_dsa.tail())
print('-' * 100)
print(df_dsa.columns)
print('-' * 100)
print(df_dsa.dtypes)
print('-' * 100)
print(df_dsa['Valor_Venda'].describe())
print('-' * 100)
print(df_dsa[df_dsa.duplicated()])
print('-' * 100)
print(df_dsa.isnull().sum())