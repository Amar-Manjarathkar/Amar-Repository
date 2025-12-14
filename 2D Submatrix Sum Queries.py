def prefixSum2D(matrix, queries):
    if not matrix or not matrix[0]:
        return [0] * len(queries)

    R = len(matrix)
    C = len(matrix[0])
    
    # 1. Build the (R+1) x (C+1) 2D Prefix Sum Array
    # Time: O(R * C)
    prefix_sum = [[0] * (C + 1) for _ in range(R + 1)]
    
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            # Recurrence relation: PS[r][c] = matrix[r-1][c-1] + PS[r-1][c] + PS[r][c-1] - PS[r-1][c-1]
            prefix_sum[r][c] = (
                matrix[r-1][c-1] + 
                prefix_sum[r-1][c] + 
                prefix_sum[r][c-1] - 
                prefix_sum[r-1][c-1]
            )
            
    # The construction of the 2D Prefix Sum table can be visualized as:
    # 

    # 2. Process Queries in O(1) Time
    results = []
    for query in queries:
        r1, c1, r2, c2 = query
        
        # Inclusion-Exclusion Principle:
        # Sum(r1, c1 to r2, c2) = PS[r2+1][c2+1] - PS[r1][c2+1] - PS[r2+1][c1] + PS[r1][c1]
        
        sub_sum = (
            prefix_sum[r2 + 1][c2 + 1] -  # Area up to (r2, c2)
            prefix_sum[r1][c2 + 1] -      # Subtract area above r1
            prefix_sum[r2 + 1][c1] +      # Subtract area left of c1
            prefix_sum[r1][c1]            # Add back corner that was double-subtracted
        )
        results.append(sub_sum)
        
    # The query logic relies on geometric inclusion-exclusion:
    # 
    
    return results
