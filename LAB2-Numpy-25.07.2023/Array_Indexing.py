#! P:\"CSE413-Big Data and IoT Lab"\myenv\Scripts\python.exe
import numpy as np

# 1-D array
arr = np.array([1, 2, 3, 4])
print(arr[0])

# 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('2nd element on 1st row: ', arr[0, 1])

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

# Negative Indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element from 2nd dim: ', arr[1, -4])
