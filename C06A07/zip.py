x = [1, 2, 3]
y = [4, 5, 6]
z = list(zip(x, y))

print(z)

a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
c = list(zip(a, b))

print(c)

d1 = {'a' : 1, 'b' : 2}
d2 = {'c' : 4, 'd' : 5}
d3 = list(zip(d1, d2.values()))

print(d3)

def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    
    print(dicTemp)


trocaValores(d1, d2)