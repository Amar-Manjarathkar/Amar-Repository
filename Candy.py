class Solution:
    def minCandy(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        # Initialize everyone with 1 candy
        candies = [1] * n
        
        # Left-to-Right: Compare with the left neighbor
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Right-to-Left: Compare with the right neighbor
        # We use max() to ensure we don't break the left-to-right condition
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # Return the sum of the candies array
        return sum(candies)
