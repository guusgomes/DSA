import numpy as dsa

arr1 = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])

print(arr1)
print(type(arr1))
print(arr1.shape)
print(arr1[4])
print(arr1[1:4])
print(arr1[1:4+1])

indices = [1, 2, 5, 6]

print(arr1[indices])

mask = (arr1 % 2 == 0)

print(arr1[mask])

arr1[0] = 100

print(arr1)

try:
    arr1[0] = 'Novo elemento'
except:
    print('Operação não permitida!')

print('-' * 50)

arr2 = dsa.array([1, 2, 3, 4, 5])

print(arr2)
print(type(arr2))
print(arr2.cumsum())
print(arr2.cumprod())
print('-' * 50)

arr3 = dsa.arange(0, 50, 5)

print(arr3)
print(type(arr3))
print(dsa.shape(arr3))
print(arr3.dtype)
print('-' * 50)

arr4 = dsa.zeros(10)

print(arr4)
print('-' * 50)

arr5 = dsa.eye(3)

print(arr5)
print('-' * 50)

arr6 = dsa.diag(dsa.array([1, 2, 3, 4]))

print(arr6)
print('-' * 50)

arr7 = dsa.array([True, False, False, True])

print(arr7)
print('-' * 50)

arr8 = dsa.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])

print(arr8)
print('-' * 50)

print(dsa.linspace(0, 10))
print('-' * 50)
print(dsa.linspace(0, 10, 15))
print('-' * 50)
print(dsa.logspace(0, 5, 10))
print('-' * 50)

arr9 = dsa.array(([1, 2, 3], [4, 5, 6]))

print(arr9)
print(type(arr9))
print(arr9.shape)
print('-' * 50)

arr10 = dsa.ones((2, 3))

print(arr10)
print('-' * 50)

lista = [[13, 81, 22], [0, 34, 59], [21, 48, 94]]
arr11 = dsa.matrix(lista)

print(arr11)
print(type(arr11))
print(arr11.size)
print(arr11.dtype)
print(arr11[2, 1])
print(arr11[0:2, 2])
print(arr11[1,])
arr11[1,0] = 100
print(arr11)
print('-' * 50)

x = dsa.array([1, 2])
y = dsa.array([1.0, 2.0])
z = dsa.array([1, 2], dtype = dsa.float64)

print(x.dtype, y.dtype, z.dtype)
print('-' * 50)

arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)

print(arr12)
print(arr12.itemsize)
print(arr12.nbytes)
print(arr12.ndim)