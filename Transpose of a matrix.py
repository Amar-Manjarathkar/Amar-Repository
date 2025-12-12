matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose using zip and convert tuples to lists
transposed_matrix = [list(row) for row in zip(*matrix)]

# Output
for row in transposed_matrix:
    print(row)
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
