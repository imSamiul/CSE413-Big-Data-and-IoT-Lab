#! P:\"CSE413-Big Data and IoT Lab"\myenv\Scripts\python.exe
import numpy as np

# 1-D array
# arr[Start:End:Step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
