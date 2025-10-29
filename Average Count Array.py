#User function Template for python3
from collections import Counter # Be sure to import Counter at the top

class Solution:
    def countArray (self, arr, x) : 
        
        # 1. Count all element occurrences in O(N) time.
        # Example: [2, 4, 8, 6, 2] becomes {2: 2, 4: 1, 8: 1, 6: 1}
        counts = Counter(arr)
        
        result = []
        
        # 2. Iterate the array again (O(N) time)
        for n in arr:
            
            # 3. Calculate the average using FLOOR division (//)
            avg_val = (x + n) // 2
            
            # 4. Get the count from the map. This is an O(1) lookup.
            # If avg_val isn't in the map, counts.get() correctly returns 0.
            result.append(counts.get(avg_val, 0))
            
        return result
