import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.stack((arr1, arr2))

print(result)

# 2D Array
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.stack((arr1, arr2))

print(result)