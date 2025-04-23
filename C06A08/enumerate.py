seq = ['a', 'b', 'c', 'd']

print(list(enumerate(seq)))

for i, v in enumerate(seq):
    print(i, v)

for i, v in enumerate(seq):
    if i > len(seq):
        break
    else:
        print(i, v)

lista = ['Marketing', 'Tecnologia', 'Bussiness']

for i, v in enumerate(lista):
    print(f'{i + 1} - {v};')

for i, v in enumerate('Data Science Academy'):
    print(i, v)