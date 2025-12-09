class Solution:
    def findDuplicates(self, arr):
        # code here
        res = []
        from collections import Counter
        element_counts = Counter(arr)
        res = [k for k, v in element_counts.items() if v == 2]
        return res
