class Solution:
    def findKRotation(self, arr):
        # code here
        n = len(arr)
        k =0
        small = min(arr)
        for i in range(n):
            if arr[i]==small:
                k = i;
        return k
