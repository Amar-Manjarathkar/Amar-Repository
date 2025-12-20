class Solution:
    def searchInsertK(self, arr, k):
        # code here
        n = len(arr)
        res = 0
        for i in range(n):
            if arr[i] == k:
                return i
            elif arr[i]<k :
                res= i+1
        return res
