class Solution:
    def transitionPoint(self, arr): 
        # Code here
        n = len(arr)
        for i in range(n):
            if arr[i] == 1:
                return i
                
        return -1
