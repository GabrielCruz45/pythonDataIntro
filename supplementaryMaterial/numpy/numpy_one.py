# under the hood, numpy is written in C, which is waaay faster
import numpy as np




#                                                  --simple n-dimensional array--
print(np.__version__)

py_array = [1, 2, 3, 4]

np_array = np.array([1, 2, 3, 4])

print(np_array)
print(np_array * 2) # you can multiply all the numbers inside
print(py_array * 2) # 'doubles' the array -> [1, 2, 3, 4, 1, 2, 3, 4]


print(type(py_array)) # prints <class 'list>
print(type(np_array)) # prints <class 'numpy.ndarray'> nd -> N dimensional






#                                                    --multi-dimensional arrays--
zeroDim_array = np.array('A')
print(zeroDim_array.ndim) # ndim -> number of dimensions


oneDim_array = np.array(['A', 'B', 'C'])
print(oneDim_array.ndim)


twoDim_array = np.array([
                        ['A', 'B', 'C'], 
                        ['D', 'E', 'F'], 
                        ['G', 'H', 'I']
                    ])
print(twoDim_array.ndim)


threeDim_array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                           [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                           [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]
                        ])
print(threeDim_array.ndim)

# you could go to 4, 5 and beyond dimensions


print(threeDim_array.shape) 
# returns a tuple of integers; it shows the depth, the number of rows and the number of columns



# usually in python you would access a value of the array as so
print(threeDim_array[0][0][0]) # this is know as *Chain Indexing*

# with NumPy we have access to multi-dimensional indexing
print(threeDim_array[0, 0, 0]) # prints 'A'
print(threeDim_array[0, 1, 0]) # prints 'D'
print(threeDim_array[2, 1, 0]) # prints 'W'

word = threeDim_array[0, 1, 0] + threeDim_array[1, 1, 2] + threeDim_array[0, 2, 0] + threeDim_array[0, 1, 1]
print(word)




#                                                    --slicing--
