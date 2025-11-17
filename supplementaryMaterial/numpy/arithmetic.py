import numpy as np

# linear algebra
# scalar arithmetic

array = np.array([1, 2, 3])

print(array + 1)
print(array - 1)
print(array * 1)
print(array / 2)
print(array ** 2)

# vectorize math functions; a vector is a single dimension

# square root
print(np.sqrt(array))

array_two = np.array([1.01, 2.5, 3.99])

# round
print(np.round(array_two))

# round down
print(np.floor(array_two))

# round up
print(np.ceil(array_two))


# there are constants in the library
print(np.pi)
print(np.e)
print(np.euler_gamma)
print(np.inf)
print(np.nan)
print(-np.inf)
print(-0.0)

# 
radii = np.array([1, 2, 3])
print(np.pi * radii ** 2) # area of a circle


# element-wise arithmetic

arithmetic_array_one = np.array([1, 2, 3])
arithmetic_array_two = np.array([4, 5, 6])

print(arithmetic_array_one + arithmetic_array_two)
print(arithmetic_array_one - arithmetic_array_two)
print(arithmetic_array_one * arithmetic_array_two)
print(arithmetic_array_one / arithmetic_array_two)
print(arithmetic_array_one ** arithmetic_array_two)
print(arithmetic_array_one % arithmetic_array_two)


# comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60) # students that passed example
print(scores < 60) # students that failed example
scores[scores < 60] = 0 # any student that has less than 60 will quantize that score to 0; primer for filtering
print(scores)