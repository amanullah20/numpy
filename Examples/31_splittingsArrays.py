# Example 31: NumPy - Splitting Arrays
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Splitting the array into three parts
split_arrays = np.array_split(array, 3)

print('Split Arrays:', split_arrays)
