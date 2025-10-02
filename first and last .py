class Solution:
    def find(self, arr, x):
        
        # code here
        n = len(arr)
        first, last = -1, -1
        for i in range(n):
            if arr[i] == x:
                first = i
        for i in range(n-1, -1, -1):
            if arr[i] == x:
                last = i
        return (last, first)
