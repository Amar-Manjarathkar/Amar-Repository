class Solution:
    def minCost(self, keys, freq):
        n = len(keys)
        
        # 1. Precompute the sum of frequencies
        # SumFreq[i][j] will store the sum of frequencies from freq[i] to freq[j] (inclusive)
        # We can also use a prefix sum array for O(1) lookups, but a 2D array is simpler
        # to conceptualize with the DP structure.
        SumFreq = [[0] * n for _ in range(n)]
        
        # Calculate SumFreq[i][j] for all i <= j
        for i in range(n):
            SumFreq[i][i] = freq[i]
            for j in range(i + 1, n):
                SumFreq[i][j] = SumFreq[i][j-1] + freq[j]
        
        # 2. Define the DP table
        # DP[i][j] stores the minimum cost of constructing an OBST
        # using keys from index i to j (inclusive).
        DP = [[0] * n for _ in range(n)]
        
        # 3. Fill the DP table
        
        # Base Case: Subtrees of length 1 (L=1)
        # The cost is just the frequency, as the key is at level 1.
        for i in range(n):
            DP[i][i] = freq[i]
            
        # Iterate over chain length (L) from 2 to n
        for L in range(2, n + 1):
            # Iterate over starting index (i)
            for i in range(n - L + 1):
                j = i + L - 1  # Ending index
                
                # Initialize DP[i][j] to infinity
                DP[i][j] = float('inf')
                
                # Try every key 'k' from i to j as the root of the current subtree
                for k in range(i, j + 1):
                    
                    # Cost of the left subtree (keys[i]...keys[k-1])
                    # If k=i, the left subtree is empty (cost 0)
                    left_cost = DP[i][k-1] if k > i else 0
                    
                    # Cost of the right subtree (keys[k+1]...keys[j])
                    # If k=j, the right subtree is empty (cost 0)
                    right_cost = DP[k+1][j] if k < j else 0
                    
                    # Recurrence Relation:
                    # Total cost = (Left Subtree Cost) + (Right Subtree Cost) + (Weight of the current Subtree)
                    # When a key is made a root, the level of all nodes (root, left, right) 
                    # increases by 1 relative to their previous structure. 
                    # This adds (Sum of all frequencies) to the total cost.
                    
                    current_cost = left_cost + right_cost + SumFreq[i][j]
                    
                    DP[i][j] = min(DP[i][j], current_cost)
                    
        # The minimum cost for all keys (from index 0 to n-1)
        return DP[0][n-1]
