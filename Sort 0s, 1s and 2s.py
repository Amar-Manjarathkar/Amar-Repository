class Solution:
    def sort012(self, arr):
        res0, res1, res2 = [], [], []
        
        for num in arr:
            if num == 0:
                res0.append(num)
            elif num == 1:
                res1.append(num)
            else:
                res2.append(num)
        
        res = res0 + res1 + res2
        for i in range(len(arr)):
            arr[i] = res[i]   # copy back to original
        
        return arr
