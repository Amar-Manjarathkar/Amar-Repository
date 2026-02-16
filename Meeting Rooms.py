class Solution:
    def canAttend(self, arr):
        # Code Here
        arr.sort()
        result = True
        for i in range(len(arr)-1):
            if arr[i][1] > arr[i+1][0]:
                return False
        return result
            
        
