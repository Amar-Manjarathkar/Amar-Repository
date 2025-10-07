class Solution:
    def findMissing(self, a, b):
        b_set = set(b)
        return [n for n in a if n not in b_set]
