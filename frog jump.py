class Solution:
    def minCost(self, height):
        n = len(height)
        if n == 1:
            return 0  # already at last stair
        
        # dp[i] = minimum cost to reach stair i
        dp = [0] * n
        dp[0] = 0
        dp[1] = abs(height[1] - height[0])

        for i in range(2, n):
            one_step = dp[i - 1] + abs(height[i] - height[i - 1])
            two_steps = dp[i - 2] + abs(height[i] - height[i - 2])
            dp[i] = min(one_step, two_steps)
        
        return dp[-1]
