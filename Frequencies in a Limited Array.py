class Solution:
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        res = [0] * n
        for num in arr:
            if 1 <= num <= n:
                res[num-1] += 1
            
        return res
        

