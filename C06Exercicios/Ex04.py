# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
#lista = [0, 1, 2, 3, 4]

def quadrado(num):
    return num ** 2

    
def cubo(num):
    return num ** 3


lista = [0, 1, 2, 3, 4]
aoquadrado = list(map(quadrado, lista))
aocubo = list(map(cubo, lista))

print(f'Lista ao quadrado: {aoquadrado}.\nLista ao cubo: {aocubo}.')