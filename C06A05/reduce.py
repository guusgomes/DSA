from functools import reduce

def soma(a, b):
    x = a + b
    return x
 

lista = [47, 11, 42, 13]

print(reduce(soma, lista))

lst = [47, 11, 42, 13]

print(reduce(lambda x, y: x + y, lst))

maior = lambda a, b: a if (a > b) else b

print(reduce(maior, lst))