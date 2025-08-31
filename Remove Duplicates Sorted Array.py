class Solution:
    def removeDuplicates(self, arr):
        seen = set()
        res = []
        
        for num in arr:
            if num not in seen:
                seen.add(num)
                res.append(num)
                
        return res
