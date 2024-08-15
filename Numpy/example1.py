import numpy as np

arr = np.array([1, 2, 3])

print(arr)
print(np.__version__)
print(type(arr))


arr2 = np.array([[1, 2], [3, 4], [5, 6]])

print(arr2)

d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr.ndim)
print(d.ndim)
print(arr2.ndim)


arr3 = np.array([1, 2, 3, 4], ndmin=5)

print(arr3)
print('number of dimensions :', arr3.ndim)