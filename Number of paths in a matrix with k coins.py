class Solution:
    def numberOfPath(self, mat, k):
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns

        # -----------------------------------------------------------------
        # Approach 1: Top-Down Dynamic Programming (Memoization)
        # -----------------------------------------------------------------
        
        # memo[i][j][current_sum] will store the number of ways to
        # reach the destination (n-1, m-1) starting from cell (i, j)
        # given we have already collected 'current_sum' coins.
        # We initialize with -1 to indicate "not computed yet".
        memo = [[[-1 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

        def solve(i, j, current_sum):
            # i, j -> current cell coordinates
            # current_sum -> sum of coins collected *before* visiting (i, j)

            # 1. Base Case: Out of bounds
            # If we move off the grid, this path is invalid.
            if i >= n or j >= m:
                return 0

            # 2. Calculate the new total sum including the current cell
            new_sum = current_sum + mat[i][j]

            # 3. Pruning: If sum already exceeds k, this path is invalid.
            if new_sum > k:
                return 0

            # 4. Base Case: Reached the destination (bottom-right)
            if i == n - 1 and j == m - 1:
                # If the total sum is exactly k, we found one valid path.
                return 1 if new_sum == k else 0

            # 5. Check memoization table
            # If we've already computed the result for this state (i, j, current_sum),
            # return it directly to avoid redundant calculations.
            if memo[i][j][current_sum] != -1:
                return memo[i][j][current_sum]

            # 6. Recursive calls:
            # The total number of ways from (i, j) is the sum of:
            # - ways by moving down (i+1, j)
            # - ways by moving right (i, j+1)
            # In both cases, the 'new_sum' (which includes mat[i][j])
            # becomes the 'current_sum' for the next step.
            paths_down = solve(i + 1, j, new_sum)
            paths_right = solve(i, j + 1, new_sum)

            # 7. Store the result in the memo table and return it
            memo[i][j][current_sum] = paths_down + paths_right
            return memo[i][j][current_sum]

        # Initial call: Start at (0, 0) with a collected sum of 0.
        # The function will add mat[0][0] in the first step.
        return solve(0, 0, 0)


        # -----------------------------------------------------------------
        # Approach 2: Bottom-Up Dynamic Programming (Tabulation)
        # -----------------------------------------------------------------
        # This approach is often more efficient as it avoids recursion.
        
        # dp[i][j][s] = number of ways to reach cell (i, j)
        #                 with an exact total sum of 's'.
        dp = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

        # Base Case: Starting cell (0, 0)
        start_coins = mat[0][0]
        if start_coins <= k:
            # There is 1 way to be at (0, 0) with a sum of mat[0][0]
            dp[0][0][start_coins] = 1

        # Fill the DP table
        for i in range(n):
            for j in range(m):
                current_coins = mat[i][j]

                # Iterate through all possible sums 's' from 0 to k
                for s in range(k + 1):
                    # We are calculating dp[i][j][s].
                    # To have a sum 's' *at* (i, j), we must have had
                    # a sum of 's - current_coins' *before* arriving.
                    if s >= current_coins:
                        needed_sum = s - current_coins

                        # We only add ways from 'top' and 'left' if we are not
                        # in the first row or first column, respectively.
                        # We also skip adding to the base case (0,0) itself.
                        
                        # Ways from top (i-1, j)
                        if i > 0:
                            dp[i][j][s] += dp[i-1][j][needed_sum]

                        # Ways from left (i, j-1)
                        if j > 0:
                            dp[i][j][s] += dp[i][j-1][needed_sum]

        # The final answer is the number of ways to reach the
        # bottom-right cell (n-1, m-1) with an exact sum of 'k'.
        # Note: You can return the result from either approach.
        # Here, we return the result of the (uncommented) Approach 1.
        # To use this approach, uncomment it and comment out Approach 1.
        # return dp[n-1][m-1][k]
