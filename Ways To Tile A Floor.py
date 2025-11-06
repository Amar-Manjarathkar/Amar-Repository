class Solution:
    def numberOfWays(self, n):
        # This problem is a classic Fibonacci sequence.
        # dp[n] = dp[n-1] + dp[n-2]
        
        # Base Cases
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # Initialize variables for the space-optimized DP
        # 'a' will hold the (i-2)th value
        # 'b' will hold the (i-1)th value
        
        a = 1  # This corresponds to dp[1]
        b = 2  # This corresponds to dp[2]
        
        # Iterate from 3 up to n
        for i in range(3, n + 1):
            # Calculate dp[i] = dp[i-1] + dp[i-2]
            # We do not use modulo, as per the test case failure.
            current = a + b
            
            # Shift the variables for the next iteration
            a = b       # The old dp[i-1] becomes the new dp[i-2]
            b = current # The new dp[i] becomes the new dp[i-1]
            
        # After the loop, 'b' holds the final answer for dp[n]
        return b
