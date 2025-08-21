class Solution:
    def getPairs(self, arr):
        seen = set(arr)
        res = set()
        
        zero_count = arr.count(0)  # count how many zeros

        for num in arr:
            if -num in seen:
                if num == 0 and zero_count < 2:
                    continue   # skip if only one zero
                res.add(tuple(sorted((num, -num))))
        
        return [list(pair) for pair in sorted(res)]
