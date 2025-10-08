#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        index_map = {}
        
        for i, num in enumerate(arr):
            if num in index_map:
                last_index = index_map[num]
                if i - last_index <= k:
                    return True
            index_map[num]=i
        return False
