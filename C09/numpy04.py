import numpy as dsa

arr14 = dsa.array([15, 23, 63, 94, 75])

print(dsa.mean(arr14))
print(dsa.std(arr14))
print(dsa.var(arr14))
print('-' * 50)

arr15 = dsa.arange(1, 10)

print(arr15)
print(dsa.sum(arr15))
print(dsa.prod(arr15))
print(dsa.cumsum(arr15))
print('-' * 50)

arr16 = dsa.array([3, 2, 1])
arr17 = dsa.array([1, 2, 3])
arr18 = dsa.add(arr16, arr17)

print(arr16)
print('   +')
print(arr17)
print('   =')
print(arr18)
print('-' * 50)

arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])

print(arr19)
print(arr20)
print(arr19.shape)
print(arr20.shape)

arr21 = dsa.dot(arr19, arr20)

print(arr21)
print('-' * 50)

arr21_2 = arr19 @ arr20

print(arr21_2)
print('-' * 50)

arr21_3 = dsa.tensordot(arr19, arr20, axes = ((1), (0)))

print(arr21_3)