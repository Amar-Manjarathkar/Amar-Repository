class Solution:
    def maxProduct(self, arr):
        # Handle edge case where array is empty
        if not arr:
            return 0
        
        # Initialize variables
        # curr_max: maximum product ending at the current position
        # curr_min: minimum product ending at the current position
        # result: global maximum product found so far
        curr_max = arr[0]
        curr_min = arr[0]
        result = arr[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            num = arr[i]
            
            # If the current number is negative, swapping curr_max and curr_min 
            # handles the sign flip logic elegantly.
            # Because: neg * max = small min, and neg * min = large max.
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            # Update curr_max: 
            # Either start a new subarray at 'num' OR extend the previous max product
            curr_max = max(num, curr_max * num)
            
            # Update curr_min:
            # Either start a new subarray at 'num' OR extend the previous min product
            curr_min = min(num, curr_min * num)
            
            # Update the global result
            result = max(result, curr_max)
            
        return result
