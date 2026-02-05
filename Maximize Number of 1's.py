class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zeros = 0
        max_len = 0
        n = len(arr)
        
        # 'right' pointer expands the window
        for right in range(n):
            # If we encounter a 0, increment our zero counter
            if arr[right] == 0:
                zeros += 1
            
            # If zeros exceed k, shrink the window from the left
            while zeros > k:
                if arr[left] == 0:
                    zeros -= 1
                left += 1
            
            # Update the maximum length of the window
            max_len = max(max_len, right - left + 1)
            
        return max_len
