import numpy as np

# Broadcasting allows NumPy to perform operations on arrays,
# with different shapes by virtually expanding the dimensions
# so they match the larger array' shape.

# Arrays are matching when:
# The dimensions have the same size
# or
# one of the dimensions is of size 1

array_one = np.array([[1, 2, 3, 4]])
array_two = np.array([[1], [2], [3], [4]])

print("Arrays one and two\n")
print(array_one.shape)
print(array_two.shape)

# these two arrays can be broadcasted because each of them have a dimension of size one

print(array_one * array_two)
print((array_one * array_two).ndim)


array_three = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
array_four = np.array([[1], [2], [3], [4]])

print("Arrays three and four\n")
print(array_three.shape)
print(array_four.shape)

# print(array_three * array_four) # this will throw an error! one array doesn't have a dimension of size 1!
array_five = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
array_six = np.array([[1], [2], [3], [4]])

print("Arrays five and six\n")
print(array_five.shape)
print(array_six.shape)

print(array_five * array_six) # this won't throw an error because dimensions either match or are of size 1

# multiplication table example
array_seven = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array_eight = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

# check if they match
print(array_seven.shape)
print(array_eight.shape)

print(array_seven * array_eight)