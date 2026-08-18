import numpy as np


 
arr = np.array([1,2,3,4,5,6,7,8,9])

# Even Number
print(arr[arr%2==0])

# Odd number 
print(arr[arr % 2 != 0])

# random condition 
print(arr[arr>3])