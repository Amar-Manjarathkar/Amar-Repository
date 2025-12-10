class Solution:
    def findTwoElement(self, arr):
        # code here
        seen = set(arr)
        dup = sum(arr)-sum(seen)
        miss = abs(sum(arr) - sum(range(1,len(arr)+1))- dup)
        return [dup,miss]

