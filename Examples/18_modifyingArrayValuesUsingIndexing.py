# Example 18: NumPy - Modifying Array Values using Indexing
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Modifying values at specific indices
array[[1, 3]] = [100, 200]

print('Modified Array:', array)
