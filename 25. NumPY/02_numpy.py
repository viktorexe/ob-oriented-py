import numpy as np 
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr *= 10
print(arr)
print("")
print(arr.shape)
print(arr.size)
print(arr.ndim)
print('Sum of array:', arr.sum())
print('Mean of array:', arr.mean())