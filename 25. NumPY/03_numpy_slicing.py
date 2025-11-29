import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[0:5]) # All elements 
print(arr[1:4]) # 2, 3, 4

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr1[:, 0]) # Printing only first column
print(arr1[0,:]) # Only first row 
print(arr1[0:2, 0:2])
