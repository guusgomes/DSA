# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

numeros = [1, 2, 3]
terceirapotencia = list(map(lambda x: x ** 3, numeros))

print(terceirapotencia)