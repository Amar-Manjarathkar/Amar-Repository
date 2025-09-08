class Solution:
    def findUnion(self, a, b):
        # Convert both lists into sets (removes duplicates)
        union_set = set(a) | set(b)   # '|' is set union
        
        # If order matters, sort the result
        return sorted(union_set)
