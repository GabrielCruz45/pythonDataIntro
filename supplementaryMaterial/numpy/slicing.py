#                                                   ---slicing---
#                                               array[start : end : step] -> end is exclusive
import numpy as np

array = np.array([
                    [1, 2, 3, 4, 17, 21], 
                    [5, 6, 7, 8, 18, 22], 
                    [9, 10, 11, 12, 19, 23], 
                    [13, 14, 15, 16, 20, 24],
                    [25, 26, 27, 28, 29, 30],
                    [31, 32, 33, 34, 35, 36]
            ])

# indexing
print("indexing")
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[-1])
print(array[-2])
print(array[-3])
print(array[-4])


# slicing
print("slicing")
print(array[0:3:2, 1:4:2])
print(array[1:, ::2]) # -> selects every row after the first and selects each 2 elements from those rows
print(array[1:, ::-2]) # step can also be negative

print(array[:, 0]) # select from all rows, the first element
print(array[:, 1]) # select from all rows, the second element
print(array[:, 2]) # select from all rows, the third element
print(array[:, 3]) # select from all rows, the fourth element
print(array[:, 4]) # select from all rows, the ✨fifth element✨
print(array[:, 5]) # select from all rows, the sixth element

print("\nadvanced slicing\n")
print(array[:, 1::2]) # selects every other element from all rows
print(array[::-1, ::-1]) # selects all rows in reverse order AND every element in reverse order
print(array[2:4, 2:4]) # center quadrant
print(array[::5, ::5]) # corners
print(array[:, ::3])
