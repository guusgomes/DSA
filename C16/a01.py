import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df_dsa = pd.read_csv('C16/dataset.csv')
print(df_dsa.shape)
print('-' * 100)
print(df_dsa.columns)
print('-' * 100)
print(df_dsa.head())
print('-' * 100)
print(df_dsa.tail())
print('-' * 100)

## PRÉ-PROCESSAMENTO DOS DADOS
print(df_dsa['Data'].min())
print(df_dsa['Data'].max())
print('-' * 100)
print(df_dsa.info())
print('-' * 100)

df_dsa['Data'] = pd.to_datetime(df_dsa['Data'])
print(df_dsa.head())
print('-' * 100)
print(df_dsa.info())
print('-' * 100)

serie_temporal = df_dsa.set_index('Data')['Total_Vendas']
print(type(serie_temporal))
print('-' * 100)
print(serie_temporal)
print('-' * 100)

serie_temporal = serie_temporal.asfreq('D')
print(serie_temporal)
print('-' * 100)

## ANÁLISE EXPLORATÓRIA

## GRÁFICO SEM FORMATAÇÃO
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal)
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Série Temporal de Vendas')
plt.grid(True)
plt.show()

## GRÁFICO COM FORMATAÇÃO
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal, color = 'white', linewidth = 2)

    ## CORES/ESTILO
plt.gca().set_facecolor('#2e03a3')
plt.grid(color = 'yellow', linestyle = '--', linewidth = 0.5)

    ## RÓTULOS DOS EIXOS, TÍTULO E LEGENDA
plt.xlabel('Data', color = 'black', fontsize = 14)
plt.ylabel('Vendas', color = 'black', fontsize = 14)
plt.title('Série Temporal de Vendas', color = 'black', fontsize = 18)

    ## CORES DOS EIXOS E TICKS(MARCADORES)
plt.tick_params(axis = 'x', colors = 'black')
plt.tick_params(axis = 'y', colors = 'black')
plt.show()

## CRIAÇÃO DO MODELO DE SUAVIZAÇÃO EXPONENCIAL
modelo = SimpleExpSmoothing(serie_temporal)

    ## AJUSTE
modelo_ajustado = modelo.fit(smoothing_level = 0.2) 

    ## EXTRAÇÃO DOS VALORES PREVISTOS PELO MODELO
suavizacao_exponencial = modelo_ajustado.fittedvalues 

    ## GRÁFICO
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal, label = 'Valores Reais')
plt.plot(suavizacao_exponencial, label = 'Valores Previstos', linestyle = '--')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Modelo de Suavização Exponencial')
plt.legend()
plt.show()

## PREVISÕES
num_previsoes = 1
previsoes = modelo_ajustado.forecast(steps = num_previsoes)
print(f'Previsão do Total de Vendas para Janeiro/2024: {round(previsoes[0], 4)}.')