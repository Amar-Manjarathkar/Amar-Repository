#User function Template for python3

class Solution:
    def longest(self, arr, n):
        #Code Here
        res = 1
        for i in range(n):
            res=res*arr[i]
        return res
    
