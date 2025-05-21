import random
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('C18/dataset.csv')
print(df.shape)
print('-' * 100)
print(df.head())
print('-' * 100)

fig = go.Figure(data = [go.Candlestick(x = df['Date'],
                open = df['AAPL.Open'],
                high = df['AAPL.High'],
                low = df['AAPL.Low'],
                close = df['AAPL.Close'])])
fig.show()

precos = df['AAPL.Close'].values
print(type(precos))
print('-' * 100)

print('Definindo os Hiperparâmetros do Q-Learning...')
print('-' * 100)
num_episodios = 1000
alfa = 0.1
gama = 0.99
epsilon = 0.1

print('Configurando o Ambiente de Negociação...')
print('-' * 100)
acoes = ['comprar', 'vender', 'manter']
saldo_inicial = 1000
num_acoes_inicial = 0

def executar_acao(estado, acao, saldo, num_acoes, preco):
    ## COMPRAR
    if acao == 0:
        if saldo >= preco:
            num_acoes += 1
            saldo -= preco
    ## VENDER
    elif acao == 1:
        if num_acoes > 0:
            num_acoes -= 1
            saldo += preco
    ## LUCRO
    lucro = saldo + num_acoes * preco - saldo_inicial
    
    return(saldo, num_acoes, lucro)


print('Inicializando a Tabela Q...')
print('-' * 100)
q_tabela = np.zeros((len(precos), len(acoes)))

print('Inicializando o treinamento...')
print('-' * 100)
for _ in range(num_episodios):
    saldo = saldo_inicial
    num_acoes = num_acoes_inicial

    for i, preco in enumerate(precos[:-1]):
        estado = i

        if np.random.random() < epsilon:
            acao = random.choice(range(len(acoes)))
        else:
            acao = np.argmax(q_tabela[estado])
        
        saldo, num_acoes, lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
        prox_estado = i + 1

        q_tabela[estado][acao] += alfa * (lucro + gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])

print('Treinamento concluído.')
print('-' * 100)

saldo = saldo_inicial
num_acoes = num_acoes_inicial

print('Executando o Agente...')
print('-' * 100)
for i, preco in enumerate(precos[:-1]):
    estado = i
    acao = np.argmax(q_tabela[estado])
    saldo, num_acoes, _ = executar_acao(estado, acao, saldo, num_acoes, preco)
print('Execução concluída.')
print('-' * 100)
print(f'Número de ações: {num_acoes}.')
print('-' * 100)
print(f'Último preço: {precos[-1]}')
print('-' * 100)

saldo += num_acoes * precos[-1]
lucro = saldo - saldo_inicial
lucro_final = round(lucro, 2)
print(f'Começamos a negociação com saldo inicial de 1000 e terminamos com {saldo}, ou seja, tivemos lucro de {lucro_final}.')
print('-' * 100)