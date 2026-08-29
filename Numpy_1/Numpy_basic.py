import numpy as np
a = np.array([1, 2, 3])
zero_array = np.zeros((3, 4))
ones_array = np.ones((3, 4))
range_array = np.arange(0, 10, 2)
linear_space_array = np.linspace(0, 1, 5)
identity_matrix = np.eye(3)

print(a)
print(zero_array)
print(ones_array)
print(range_array)
print(linear_space_array)
print(identity_matrix)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2, 3)
print(arr.ndim)    # 2
print(arr.dtype)   # int64
print(arr.size)

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(arr[1, 2])       # 60 (row 1, col 2)
print(arr[:, 0])       # [10 40 70] — first column
print(arr[0:2, 1:3])   # sub-matrix

# Boolean indexing — very common in data filtering
print(arr[arr > 50])   # [60 70 80 90]


a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
print(a + b)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]