class Solution:
    def findIndex(self, arr, key):
        n = len(arr)
        res = [-1, -1]  # Initialize result with [-1, -1]
        
        # Find first occurrence
        for i in range(n):
            if arr[i] == key:
                res[0] = i
                break
        
        # Find last occurrence
        for i in range(n - 1, -1, -1):
            if arr[i] == key:
                res[1] = i
                break
        
        return res
