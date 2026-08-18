import numpy as np


# 1D Array
arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

result = np.concatenate((arr1, arr2))

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
result = np.concatenate((arr1, arr2), axis=0)

print(result)