import numpy as np

arr_1D=np.array([10,20,30])
arr_2D=np.array([[10,20,30],[40,50,60],[70,80,90]])
arr_3D=np.array([[[10,20], [30,40], [50,60], [70,80], [90,10]]])

print(arr_1D.ndim)
print(arr_2D.ndim)
print(arr_3D.ndim)