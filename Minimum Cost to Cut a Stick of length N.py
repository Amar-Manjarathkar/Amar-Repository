class Solution:
    def minCutCost(self, n, cuts):
        # Add boundaries
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        m = len(cuts)
        
        # dp[i][j] = min cost to cut segment from cuts[i] to cuts[j]
        dp = [[0] * m for _ in range(m)]
        
        # Try all segment lengths starting from 3 (since 2 points = no internal cut)
        for length in range(2, m):  # length = number of points in segment
            for i in range(m - length):
                j = i + length
                seg_len = cuts[j] - cuts[i]
                min_cost = float('inf')
                for k in range(i + 1, j):  # k is the first cut position
                    cost = seg_len + dp[i][k] + dp[k][j]
                    min_cost = min(min_cost, cost)
                dp[i][j] = min_cost
        
        return dp[0][m-1]
