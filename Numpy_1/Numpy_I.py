import numpy as np

data = np.array([1, 2, 3, 4, 5])

# Instead of a for-loop:
squared = data ** 2
normalized = (data - data.mean()) / data.std()
print(normalized)



matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix.sum())          # 21
print(matrix.sum(axis=0))    # [5 7 9] — column-wise
print(matrix.sum(axis=1))    # [6 15] — row-wise
print(matrix.mean(), matrix.std(), matrix.max())

arr = np.arange(12)
reshaped = arr.reshape(3, 4)
flattened = reshaped.flatten()
transposed = reshaped.T

print(arr)
print(reshaped)
print(flattened)
print(transposed)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))       # matrix multiplication
print(A @ B)               # same, using @ operator
print(np.linalg.inv(A))    # matrix inverse
print(np.linalg.det(A))    # determinant

np.random.seed(42)  # reproducibility — important in ML experiments
random_data = np.random.rand(3, 3)          # uniform [0,1)
normal_data = np.random.randn(3, 3)         # standard normal
random_ints = np.random.randint(0, 100, 5)  # random integers4

print(random_data)
print(normal_data)  
print(random_ints)