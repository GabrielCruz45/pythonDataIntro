# drillinh basic arrays in numpy
import numpy as np

array_one = np.array([1, 2, 3, 4])
print(array_one)
print(array_one.ndim)
print(type(array_one))
print(array_one * 1000)
print(array_one + 1)
print(array_one - 4)

array_fourDims = np.array([[[[1, 2, 3, 4], [5, 6, 7, 8]],
                            [[9, 10, 11, 12], [13, 14, 15, 16]]],
                           
                           [[[17, 18, 19, 20], [21, 22, 23, 24]],
                            [[25, 26, 27, 28], [29, 30, 31, 32]]]])

print(array_fourDims.ndim)
print(array_fourDims[0, 1, 1, 2])