class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = arr[i]
        
        for len_ in range(2, n + 1):
            for i in range(n - len_ + 1):
                j = i + len_ - 1
                # first player chooses the better end
                dp[i][j] = max(
                    arr[i] + min(dp[i+2][j] if i+2 <= j else 0,
                                 dp[i+1][j-1] if i+1 <= j else 0),
                    arr[j] + min(dp[i+1][j-1] if i <= j-1 else 0,
                                 dp[i][j-2] if i <= j-2 else 0)
                )
        
        return dp[0][n-1]
