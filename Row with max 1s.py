class Solution:
    def rowWithMax1s(self, arr):
        # code here
        res = 0
        index = -1
        n = len(arr)
        for i in range(n):
            if 1 in arr[i]:
                cnt = arr[i].count(1)
                if res < cnt:
                    res = cnt
                    index = i
        return index
            
