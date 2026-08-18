import numpy as np

# 1D array
import numpy as np

arr = np.array([10, 20, 30])

new_arr = np.append(arr, [40,50,60])

print(new_arr)


# 2D array
arr = np.array([
    [1, 2],
    [3, 4]
])
new_arr = np.append(arr, [[5, 6]], axis=0)

print(new_arr)