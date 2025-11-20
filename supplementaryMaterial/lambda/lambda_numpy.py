import numpy as np

# Instructions: Use numpy.vectorize with a lambda function for element-wise application on a NumPy array arr = np.array([5, -2, 10, -8, 0]).
array = np.array([5, -2, 10, -8, 0])



#     Cube and Clamp: Return the cube of a number, but clamp the result at a maximum of 100.
cube_and_clamp = np.vectorize(lambda x: x ** 3 if x ** 3 < 100 else 100)

processed_one = cube_and_clamp(array)
print(f"Cube and clamp: {processed_one}")



#     Odd/Even Factorial: If the number is even, return the number divided by 2. If it's odd, return the number multiplied by 3.
odd_even_factorial = np.vectorize(lambda x: x / 2 if x % 2 == 0 else x * 3)
processed_two = odd_even_factorial(array)
print(f"Sign check: {processed_two}")



#     Sign Check: Return 1 if the number is positive, -1 if negative, and 0 if zero.
processed_three = np.sign(array)
print(processed_three)



#     Threshold Boolean: Return True if the absolute value of the number is greater than 5, otherwise False.
threshold_bool = np.vectorize(lambda x: True if np.abs(x) > 5 else False)
processed_four = threshold_bool(array)
print(processed_four)



#     Log Transformation: Apply ln(x) (natural logarithm) to the number, but return 0 if the number is less than or equal to 0.
log_transform = np.vectorize(lambda x: np.log(x) if x > 0 else 0)
processed_five = log_transform(array)
print(processed_five)
