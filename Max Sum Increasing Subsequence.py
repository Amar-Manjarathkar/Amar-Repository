class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        
        # Edge case: if array is empty (though constraints say size >= 1)
        if n == 0:
            return 0
            
        # Initialize dp array. 
        # dp[i] stores the max sum of an increasing subsequence ending at index i.
        # Initially, the max sum is just the element itself.
        dp = arr[:]
        
        # Iterate through the array
        for i in range(n):
            # Compare with all previous elements
            for j in range(i):
                # Check for strictly increasing condition
                if arr[j] < arr[i]:
                    # Update dp[i] if adding arr[i] to the sequence ending at j
                    # produces a larger sum
                    if dp[j] + arr[i] > dp[i]:
                        dp[i] = dp[j] + arr[i]
                        
        # The result is the maximum value in the dp array
        return max(dp)
