class Solution:
    def chocolatePickup(self, mat):
        n = len(mat)
        
        # Use a dictionary for memoization. 
        # The state is (r1, c1, r2). c2 is derived.
        memo = {}

        def solve(r1, c1, r2):
            # Derive c2 using the constraint: r1 + c1 = r2 + c2
            c2 = r1 + c1 - r2
            
            # --- Base Cases ---
            
            # 1. Out of Bounds
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return -float('inf')  # Invalid path
            
            # 2. Blocked Cell
            if mat[r1][c1] == -1 or mat[r2][c2] == -1:
                return -float('inf')  # Invalid path
            
            # 3. Destination Reached
            if r1 == n - 1 and c1 == n - 1:
                # Both paths are at the end, return the chocolates at this cell
                return mat[n - 1][n - 1]
            
            # --- Memoization Check ---
            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]
            
            # --- Recursive Step ---
            
            # Calculate chocolates collected at the current cells
            chocolates = 0
            if r1 == r2:
                # Both paths are on the same cell (since r1==r2 and c1==c2)
                # Collect chocolates only once
                chocolates = mat[r1][c1]
            else:
                # Paths are on different cells
                chocolates = mat[r1][c1] + mat[r2][c2]
                
            # Explore all 4 possible next moves for the two paths:
            # (Down, Down), (Down, Right), (Right, Down), (Right, Right)
            max_future_chocolates = max(
                solve(r1 + 1, c1, r2 + 1),  # P1: Down, P2: Down
                solve(r1 + 1, c1, r2),    # P1: Down, P2: Right
                solve(r1, c1 + 1, r2 + 1),  # P1: Right, P2: Down
                solve(r1, c1 + 1, r2)     # P1: Right, P2: Right
            )
            
            # Total chocolates = current + max from future steps
            total = chocolates + max_future_chocolates
            
            # Store in memo and return
            memo[(r1, c1, r2)] = total
            return total

        # --- Initial Call ---
        
        # Handle edge case where the starting cell is blocked
        if n == 0 or mat[0][0] == -1:
            return 0
            
        # Start both paths at (0, 0)
        result = solve(0, 0, 0)
        
        # If the result is -inf (or any negative), no valid path exists.
        # Return 0 in that case, otherwise return the result.
        return max(0, result)
