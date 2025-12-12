import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Transpose using .T attribute
transposed_matrix = matrix.T

# Output
print(transposed_matrix)
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]
