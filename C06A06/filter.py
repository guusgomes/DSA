def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(verificaPar(35))
print(verificaPar(10))

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(list(filter(verificaPar, lista)))
print(list(filter(lambda x: x % 2 == 0, lista)))
print(list(filter(lambda num: num > 8, lista)))