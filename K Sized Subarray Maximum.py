# class Solution:
#     def maxOfSubarrays(self, arr, k):
#         # code here
#         if k == 1 or k == 0:
#             return arr
#         res = []
#         window = arr[:k]
#         for i in range(1,len(arr)):
#             if len(window) == k:
#                 res.append(max(window))
#                 window = arr[i:i+k]
#         return res
#         # [3, 3, 4, 5, 5, 5, 6, 6]

from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        if n == 0: return []
        if k == 1: return arr
        
        res = []
        dq = deque()  # Stores indices of elements
        
        for i in range(n):
            # 1. Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # 2. Remove indices of all elements smaller than the current 
            # element from the back (they can't be the maximum)
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # 3. Add current element's index to the back
            dq.append(i)
            
            # 4. The front of the deque is the maximum for the current window
            # Start adding to results once we have processed at least k elements
            if i >= k - 1:
                res.append(arr[dq[0]])
                
        return res
