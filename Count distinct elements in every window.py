# class Solution:
#     def countDistinct(self, arr, k):
        # Code here
        # from collections import Counter

        # window = arr[:k]
        # distinct_count = []
        # n = len(arr) - k
        # for i in range(1,n+2):
        #     items = Counter(window).keys()
        #     _count = len(items)
        #     distinct_count.append(_count)
        #     window = arr[i:k+i]
        # return distinct_count
from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        if k > n:
            return []
            
        res = []
        counts = defaultdict(int)
        distinct_in_window = 0
        
        # 1. Initialize the first window (0 to k-1)
        for i in range(k):
            if counts[arr[i]] == 0:
                distinct_in_window += 1
            counts[arr[i]] += 1
        
        res.append(distinct_in_window)
        
        # 2. Slide the window from index k to n-1
        for i in range(k, n):
            # Element entering the window
            new_val = arr[i]
            # Element leaving the window
            old_val = arr[i - k]
            
            # Remove the outgoing element
            counts[old_val] -= 1
            if counts[old_val] == 0:
                distinct_in_window -= 1
            
            # Add the incoming element
            if counts[new_val] == 0:
                distinct_in_window += 1
            counts[new_val] += 1
            
            res.append(distinct_in_window)
            
        return res
        
        
