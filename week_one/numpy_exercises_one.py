import numpy as np
import os

print("--- Commencing Consolidated NumPy Script ---")

# --- Exercise 1: Create a 1D Array and Check Attributes ---
print("\n--- Exercise 1 ---")
my_list = [1, 5, 9, 13]
a = np.array(my_list)
print(f"Array: {a}")
print(f"Dimensions: {a.ndim}")
print(f"Shape: {a.shape}")
print(f"Data Type: {a.dtype}")

# --- Exercise 2: Create a 2D Array and Check Attributes ---
print("\n--- Exercise 2 ---")
list_of_lists = [[1, 2, 3], [4, 5, 6]]
b = np.array(list_of_lists)
print(f"Array:\n{b}")
print(f"Dimensions: {b.ndim}")
print(f"Shape: {b.shape}")

# --- Exercise 3: Placeholder and Sequence Arrays ---
print("\n--- Exercise 3 ---")
# 1. Zeros
d = np.zeros((3, 4))
print(f"Zeros:\n{d}")
# 2. Arange
f = np.arange(10, 30, 2)
print(f"\nArange (Evens): {f}")
# 3. Linspace
g = np.linspace(0, 5, 10)
print(f"\nLinspace (10 numbers): {g}")

# --- Exercise 4: Upcasting ---
print("\n--- Exercise 4 ---")
c = np.array([1, 2, 3.14, 4])
# Note how 1, 2, and 4 are converted to floats
print(f"Array: {c}")
print(f"Data Type: {c.dtype.name}")

# --- Exercise 5: Element-wise Operations (Fahrenheit to Celsius) ---
print("\n--- Exercise 5 ---")
fahrenheit = np.array([32, 68, 95, 104, 212])
celsius = (fahrenheit - 32) * (5 / 9)
print(f"Fahrenheit: {fahrenheit}")
print(f"Celsius: {celsius}")

# --- Exercise 6: Boolean Indexing (Masking) ---
print("\n--- Exercise 6 ---")
# We use the 'celsius' variable from Ex 5
# If this were a real application, we might pass this data
# or redefine it for a standalone exercise.
# celsius = np.array([0., 20., 35., 40., 100.]) # Redefining for safety
mask = celsius > 30
print(f"Boolean Mask: {mask}")
hot_temps = celsius[mask]
print(f"Hot Temps (>30C): {hot_temps}")

# --- Exercise 7: Element-wise vs. Matrix Product ---
print("\n--- Exercise 7 ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# 1. Element-wise product (*)
elem_product = A * B
print(f"Element-wise Product (*):\n{elem_product}")
# 2. Matrix product (@)
matrix_product = A @ B
print(f"\nMatrix Product (@):\n{matrix_product}")

# --- Exercise 8: Aggregation Functions ---
print("\n--- Exercise 8 ---")
scores = np.array([[80, 92, 88],
                   [75, 95, 89],
                   [91, 81, 85]])
avg_score = scores.mean()
max_score = scores.max()
total_sum = scores.sum()
print(f"Scores:\n{scores}")
print(f"\nAverage Score: {avg_score:.2f}")
print(f"Max Score: {max_score}")
print(f"Sum of Scores: {total_sum}")

# --- Exercise 9: Slicing and Views (The 🚩 Trap) ---
print("\n--- Exercise 9 ---")
# 1. Create original array
original = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Original Array:\n{original}")
# 2. Create a slice (view) of the second row (index 1)
sub_array_view = original[1, :]
print(f"\nSub-array (View): {sub_array_view}")
# 3. Modify the slice
sub_array_view[0] = 99
print(f"Modified Sub-array: {sub_array_view}")
# 4. Print the original array
print(f"\nOriginal Array After Slice Modification:\n{original}")

# --- Exercise 10: genfromtxt, Slicing, and Aggregation ---
print("\n--- Exercise 10 ---")
# 1. Create the dummy CSV file
file_content = """fixed_acidity;alcohol;quality
7.4;9.4;5
7.8;9.8;5
7.8;9.8;5
11.2;9.8;6
7.4;9.4;5
"""
file_name = "sim_wine.csv"
with open(file_name, "w") as f:
    f.write(file_content)
print(f"Created dummy file: {file_name}")

# 2. Load data, skipping header
wines = np.genfromtxt(file_name, delimiter=';', skip_header=1)
print(f"\nLoaded data:\n{wines}")

# 3. Select the last column (Quality)
quality_column = wines[:, -1]
print(f"\nQuality Column: {quality_column}")

# 4. Calculate the mean
mean_quality = quality_column.mean()
print(f"\nMean Quality: {mean_quality:.2f}")

# Cleanup
os.remove(file_name)
print(f"Cleaned up {file_name}")

print("\n--- Consolidated Script Execution Complete ---")