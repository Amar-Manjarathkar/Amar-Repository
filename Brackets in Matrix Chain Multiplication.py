import sys

class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr)
        num_matrices = n - 1
        
        # 1. Initialize DP and Split tables
        # dp[i][j] stores the minimum cost of multiplying matrices from M_i to M_j
        # M_i has dimension arr[i] * arr[i+1]
        # The matrix indices run from 0 to num_matrices - 1
        dp = [[0] * num_matrices for _ in range(num_matrices)]
        
        # split[i][j] stores the optimal split point k (0 <= k < num_matrices)
        # where the optimal multiplication is (M_i...M_k) * (M_{k+1}...M_j)
        # The stored value 'k' is an index into the matrix chain.
        split = [[0] * num_matrices for _ in range(num_matrices)]

        # L is the chain length (from 2 to num_matrices)
        for L in range(2, num_matrices + 1):
            # i is the starting matrix index
            for i in range(num_matrices - L + 1):
                j = i + L - 1  # j is the ending matrix index
                dp[i][j] = sys.maxsize
                
                # k is the split point: M_i...M_k | M_{k+1}...M_j
                for k in range(i, j):
                    # Cost of multiplying the two resulting matrices: 
                    # (M_i...M_k) dim: arr[i] x arr[k+1] 
                    # (M_{k+1}...M_j) dim: arr[k+1] x arr[j+1]
                    cost = dp[i][k] + dp[k+1][j] + arr[i] * arr[k+1] * arr[j+1]
                    
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        split[i][j] = k  # Store the optimal split point
                        
        # 2. Reconstruct the parenthesization string
        
        def get_string(i, j):
            # Base Case: Single matrix
            if i == j:
                # Convert matrix index i (0, 1, 2, ...) to character ('A', 'B', 'C', ...)
                return chr(ord('A') + i)
            
            k = split[i][j] # Optimal split point
            
            # Recursive Step: ( Left_Subchain * Right_Subchain )
            left_part = get_string(i, k)
            right_part = get_string(k + 1, j)
            
            return "(" + left_part + right_part + ")"

        # Start the reconstruction for the entire chain (M_0 to M_{N-1})
        return get_string(0, num_matrices - 1)
