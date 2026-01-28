from collections import defaultdict
from typing import List

class Solution:
    def countSubset(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        # 1. Helper function: Generate all subset sums for a list
        # using a Dictionary (Map) to handle sparse/large/negative sums.
        def get_subset_sums(nums):
            # dp = {sum: count}
            dp = {0: 1}  
            for x in nums:
                # Iterate over existing sums and create new sums by adding x
                # We convert to list() to avoid "dictionary changed size during iteration"
                for s, count in list(dp.items()):
                    new_sum = s + x
                    dp[new_sum] = dp.get(new_sum, 0) + count
            return dp

        # 2. Split the array into two halves (Meet-in-the-Middle)
        # This reduces complexity from 2^40 (trillions) to 2^21 (millions)
        mid = n // 2
        left_part = arr[:mid]
        right_part = arr[mid:]
        
        # 3. Generate sums for both halves
        left_sums = get_subset_sums(left_part)
        right_sums = get_subset_sums(right_part)
        
        total_count = 0
        
        # 4. Merge results
        # Formula: left_sum + right_sum = k  =>  left_sum = k - right_sum
        for r_sum, r_count in right_sums.items():
            needed = k - r_sum
            if needed in left_sums:
                total_count += left_sums[needed] * r_count
                
        return total_count
