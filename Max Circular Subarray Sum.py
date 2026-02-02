class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)
        
        # Standard Kadane's for Max Subarray Sum
        def kadane_max(nums):
            max_so_far = nums[0]
            current_max = nums[0]
            for i in range(1, len(nums)):
                current_max = max(nums[i], current_max + nums[i])
                max_so_far = max(max_so_far, current_max)
            return max_so_far
        
        # Standard Kadane's for Min Subarray Sum
        def kadane_min(nums):
            min_so_far = nums[0]
            current_min = nums[0]
            for i in range(1, len(nums)):
                current_min = min(nums[i], current_min + nums[i])
                min_so_far = min(min_so_far, current_min)
            return min_so_far

        max_kadane = kadane_max(arr)
        
        # If max_kadane is negative, all numbers are negative. 
        # The max sum is just the largest single element (already in max_kadane).
        if max_kadane < 0:
            return max_kadane
            
        total_sum = sum(arr)
        min_kadane = kadane_min(arr)
        
        # Max of standard sum vs wrapped sum
        return max(max_kadane, total_sum - min_kadane)
