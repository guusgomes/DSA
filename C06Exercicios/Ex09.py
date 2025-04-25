# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for k, v in enumerate(lista):
    if k > 5:
        print(f'{k} - {v}')