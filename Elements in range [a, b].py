# class Solution:
#     def cntInRange(self, arr, queries):
#         # code here
#         res = []
#         for l, r in queries:
#             count=0
#             for num in arr:
#                 if l <= num <= r:
#                     count+=1
#             res.append(count)
            
#         return res
        
import bisect

class Solution:
    def cntInRange(self, arr, queries):
        # Step 1: Sort the array for binary search
        arr.sort()
        res = []
        
        for l, r in queries:
            # Step 2: Use binary search to find the boundaries
            left = bisect.bisect_left(arr, l)  # First index where arr[index] >= l
            right = bisect.bisect_right(arr, r)  # First index where arr[index] > r
            
            # Step 3: The count of elements in the range [l, r]
            res.append(right - left)
        
        return res

        
