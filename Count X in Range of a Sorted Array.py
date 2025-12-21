class Solution:
    def countXInRange(self, arr, queries):
        # code here
    #     n = len(queries)
    #     res = []
    #     for l, r, x in queries:
    # # Slice the array from l to r (inclusive) and count x
    #         count = arr[l : r + 1].count(x)
    #         res.append(count)

    #     return res
        import bisect

# def count_occurrences(arr, queries):
        res = []
    
        for l, r, x in queries:
        # Find the first occurrence of x within the range [l, r]
        # bisect_left returns the leftmost insertion point to maintain order
            start_idx = bisect.bisect_left(arr, x, lo=l, hi=r + 1)
        
        # Find the last occurrence (the point after the last x)
        # bisect_right returns the rightmost insertion point
            end_idx = bisect.bisect_right(arr, x, lo=l, hi=r + 1)
        
        # The number of occurrences is simply the difference in indices
            res.append(end_idx - start_idx)
        
        return res

# # Input
# arr = [1, 2, 2, 4, 5, 5, 5, 8]
# queries = [[0, 7, 5], [1, 2, 2], [0, 3, 7]]

# # Output: [3, 2, 0]
# print(count_occurrences(arr, queries))
        
        
