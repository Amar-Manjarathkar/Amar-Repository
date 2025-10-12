class Solution:
    
    def maxStep(self, arr):
        n = len(arr)
        count = 0
        max_count = 0
        
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0  # reset when altitude doesn't increase
                
        return max_count
