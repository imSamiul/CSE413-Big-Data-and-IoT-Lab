#! P:\"CSE413-Big Data and IoT Lab"\myenv\Scripts\python.exe
import numpy as np
# 1-D array


arr = np.array([1, 2, 3, 4, 5])

print("1-D array:", arr)

# 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D array:")
print(arr)

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D array:")
print(arr)

# Check Number of Dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
