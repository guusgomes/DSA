import numpy as dsa

arr22 = dsa.diag(dsa.arange(3))

print(arr22)
print(arr22[1, 1])
print(arr22[1])
print(arr22[:,2])
print('-' * 50)

arr23 = dsa.arange(10)

print(arr23)
print(arr23[2:9:3])
print(arr23.min())
print(arr23.max())
print(dsa.array_equal(arr22, arr23))
print('-' * 50)

a = dsa.array([1, 2, 3, 4])
b = dsa.array([4, 2, 2, 4])

print(a == b)
print('-' * 50)

print(dsa.array([1, 2, 3]) + 1.5)
print('-' * 50)

arr24 = dsa.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
arr25 = dsa.around(arr24)

print(arr25)
print('-' * 50)

arr26 = dsa.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr26)
print('-' * 50)

arr27 = arr26.flatten()

print(arr27)
print('-' * 50)

arr28 = dsa.array([1, 2, 3])

print(arr28)
print(dsa.repeat(arr28, 3))
print(dsa.tile(arr28, 3))
print('-' * 50)

arr29 = dsa.array([5, 6])
arr30 = dsa.copy(arr29)

print(arr30)
print('-' * 50)