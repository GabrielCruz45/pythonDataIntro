# Your role as a data scientist is to understand what the data means (it's context and collection), 
# and transform it into a different representation to be used for sensemeaking.

import numpy as np
import math
a = np.array([1, 2, 3, 4, 5])

print(a.ndim)

b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10] ])
print(b.ndim)

print(b.dtype)

c = np.array([1.1, 5, 2.2]) # numpy will convert all the data into the same data type!
print(c.dtype)

d = np.zeros((2, 3))
print(d)

e = np.ones((2, 3))
print(e)

print(np.random.rand(2,3))


# arange(a, b, c) a starting number (inclusive), b ending number (exclusive), c steps -> (a, b] by c steps
f = np.arange(0, 420, 69)
print(f)

# linspace(a, b, c) a starting point, b ending point, c how many numbers within these confinements
np.linspace(0, 2, 15) # 15 numbers from 0 (inclusive) to 2 (inclusive)

# We can do many things on arrays, such as mathematical manipulation (addition, subtraction, square, exponnets) 
# as well as use boolean arrays, which are binary values. 
# We can also do matric manipulation such as product, transpose, inverse and so forth.

g = np.array([10, 20, 30, 40])
h = np.array([1, 2, 3, 4])

i = g - h
j = g * h


print(i, j)


farenheit = np.array([0, -10, -5, -15, 0])

celcius = (farenheit - 31) * (5/9)
print(celcius)

print(celcius > -20) # use check to get boolean values

print(celcius % 2 == 0) # use modulo to check if numbers are even

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

# use @ to multiply matrices
print(A @ B)

# A few more linear algebra concepts are worth layering here. 
# You might recall that the product of two matrices is only plausible when the inner dimensions of the two matrices are the same. 
# The dimensions refer to the number of elements both horizontally and vertically in the rendered matrices you've seen here. 
# We can use numpy to quickly see the shape of a matrix:

print(A.shape)

# When manipulating arrays of different types, the type of the resulting array will correspond 
# to the more general of the two types. This is called upcasting.

array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1.dtype)
array2 = np.array([[7.1, 8.2, 9.1], [10.4, 11.2, 12.3]])
print(array2.dtype)

array3 = array1 + array2
print(array3, array3.dtype) # notice how the items in the resulting array have been upcast into floating point numbers.

print(array3.sum(), array3.min(), array3.max(), array3.mean())


array4 = np.arange(1, 16, 1).reshape(3, 5)
print(array4)

print(f"This is another array :) \n{np.arange(1, 16, 1).reshape(3, 5)}")

mask = np.full((200, 200), 255, np.uint64)
print(mask, mask.dtype)


mask = mask.astype(np.uint8)
print(mask.dtype)

reshape = np.reshape(mask, (40000, 1))

print(reshape)



# Indexing, sclicing and iterating

array5 = np.array([[1, 2], [3, 4],[5, 6]])

print(array5[1, 1])

# if we want to get multiple elements, for example 1, 4, 6 
# and put them into a one-dimesional array, 
# we can enter the indices directly into an array function
print(np.array([array5[0, 0], array5[1, 1], array5[2, 1]]))

# we can do that by another form of array indexing, 
# which essentially zips the first list and the second list up
print(array5[[0, 1, 2], [0, 1, 1]])

# prints true true true
print(array5[[0, 1, 2], [0, 1, 1]] == np.array([array5[0, 0], array5[1, 1], array5[2, 1]]))

# Boolean indexing allows us to select arbitrary elements based on conditions. 
# For example, in the matrix we just talked about we want to find elements that are greater than 5 
# so we set up a condition array5 > 5

print(array5 > 5)

# We can then place this array of booleans, like a mask, 
# over the original array to return a one-dimensional array, relating to the true values
print(array5[array5 > 5])
# As we will see, this functionality is essential in the pandas toolkit, which is the bulk of this course!

# Slicing is a way of creating a sub-array based on the original array. 
# For one dimensional arrays, slicing works in similar ways to a list. To slice we use the colon : sign.
# For instance, if we put :3 in the indexing brackets we get the elements from index 0 to 2 -> essentially (]
array6 = np.array([0, 1, 2, 3, 4, 5, 6])
print(array6[0 : 3], array6[0 : 4 : 2])

# It works similarly for multi-dimensional arrays

array7 = np.array([
                [0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11]
        ])

# One argument -> E.G. [ : 2], we would get all the element from the first and second row; rows 0 and 1
print(array7[ : 2])

 # Two arguments -> E.G. [0 : 2, 1 : 3], we would get the second "[1 :"  and third column  ": 3]" values from rows 0 and 1
print(array7[0 : 2, 1 : 3])

 # ***In multi-dimensional arrays, the first argument is for selecting rows and the second for selecting columns***
 
# If you create a sub array from a slice, the information is passed by reference. If you change the sub array, the original array receives the same change.

sub_array = array7[0 : 2, 1 : 3]
print(f"{sub_array}\n{array7[0 : 2, 1 : 3]}")
sub_array[0, 0] = 50
print(sub_array[0, 0])
print(array7) # or
print(array7[0 : 2, 1 : 3])


# To load a dataset with NumPy, we can use the .genfromtxt() function. We can specify datafilename, 
# delimeter (optional but often used), and a number of rows to skip if we have a header row, hence it is 1 here.

# The genfromtex() function has a paremeter called dtype for specifying data types of each column. 
# This parameter is optional. Without specifying the types, all types will be casted the same into the more precise/general type.
wines = np.genfromtxt("./winequality-red.csv", delimiter=";", skip_header=1)
print(wines)

# Recall that we can use the integer indexing to get a certain column or a row. For example, 
# if we want to get the fixed acidity column, which is the first column, and if we just give one argument, 
# then we'll get a single dimensional list back.

# All rows combined, but only the first column.
print(wines[ : , 0]) # -> outputs a single list
# If we wanted the same values, but wanted to preserve that they sit in their own rows, we would write.
print(wines[:, 0 : 1]) # preserves the shape and outputs a the first column

# If we want the first, second and third column (0, 1, 2)
print(wines[ : , 0 : 3])

# If we want several, non-consecutive columns, use a list
print(wines[ : , [0, 2, 4]])



# We can also do basic summarization of the dataset. For example, if we want to find out the average quality of red wine, 
# we can select the quality column. We can do this in a couple of ways, the most appropiate (in this particular case) is to use
# negative numbers -> -1 (the wine quality is the last row), as negative numbers mean slicing from the end back to the start.
# Then we can call the aggregation functions on the data.

print(wines[ : , -1].mean())

graduate_admission = np.genfromtxt("Admission_predict.csv", dtype=None, delimiter=",", skip_header=1, 
                                   names=('Serial_No', 'GRE_Score', 'TOEFL_Score', 'University_Rating',
                                          'SOP', 'LOR', 'CGPA', 'Research', 'Chance_of_Admit'
                                    )
                    )

print(graduate_admission.shape)

# We can retrieve a column from the array using the column's name. Let's CGPA column and only the first five values.

print(graduate_admission['CGPA'][0 : 5])

# Since the GPA in the dataset range from 1 to 10, and in the US it's more common to use a scale of up to 4. 
# A common task might be to convert the GPA by dividing by 10 and then multiplying by 4.

graduate_admission['CGPA'] = (graduate_admission['CGPA'] / 10) * 4
print(graduate_admission['CGPA'][0 : 5])

# Recall boolean masking. We can use this to find out many students have had research experience 
# by creating a boolean mask and passing it to the array indexing operator.

print(len(graduate_admission[graduate_admission['Research'] == 1]))

# Since we have the data field "chance of admission", which ranges from 0 to 1, 
# we can try to see if students with high chance of admission (x > 0.8) on average 
# have higher GRE scores than those with lower chance of admission (x < 0.4)

# We can start by using boolean masking to pull out those students we are interested in (x > 0.8 chance of admission). After, we pull out their GPA scores. Thenm we print out the mean value.
print(graduate_admission[(graduate_admission['Chance_of_Admit'] > 0.8)]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['GRE_Score'].mean())

print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['CGPA'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['CGPA'].mean())
