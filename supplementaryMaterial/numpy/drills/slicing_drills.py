import numpy as np

array = np.array([
    [
        [1, 2, 3], 
        [4, 5, 6]
    ], 
    [
        [7, 8, 9], 
        [10, 11, 12]
    ]
])

print(array.ndim)
print(array.shape)

print(array[:, :, 1::2])

# fancy indexing; select non-contiguous pieces of data
D1_indices = [0, 0, 1, 1]  # The first dimension indices
D2_indices = [0, 0, 1, 1]  # The second dimension indices
D3_indices = [0, 2, 0, 2]
selected_elements = array[D1_indices, D2_indices, D3_indices]

print(selected_elements)