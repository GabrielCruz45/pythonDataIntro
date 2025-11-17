import numpy as np

# aggregate functions summarize data and, typically, return a single value
array = np.array([
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10]
])

print(np.sum(array))
print(np.mean(array))
print(np.std(array)) # standard deviation
print(np.var(array)) # variance
print(np.min(array)) # minimum value
print(np.max(array)) # maximum value
print(np.argmin(array)) # minimum value's position
print(np.argmax(array)) # maximum value's position

print(np.sum(array, axis=0)) # the columns will be summed
print(np.sum(array, axis=1)) # the rows will be summed