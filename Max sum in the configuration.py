class Solution:
    def maxSum(self, arr): 
        n = len(arr)
        if n == 0:
            return 0

        # Step 1: Calculate the sum of all array elements
        arr_sum = sum(arr)
        
        # Step 2: Calculate the initial weighted sum (S0)
        curr_val = sum(i * arr[i] for i in range(n))
        
        # Initialize max_val with the initial configuration's value
        max_val = curr_val
        
        # Step 3: Iterate through all possible rotations
        # We use the derived formula to update the sum in O(1) time
        for i in range(1, n):
            # The element that moves from the end to the front is arr[n-i]
            # Formula: S_next = S_prev + sum_elements - n * element_moving_to_front
            curr_val = curr_val + arr_sum - (n * arr[n - i])
            
            # Update maximum if the new configuration is larger
            if curr_val > max_val:
                max_val = curr_val
                
        return max_val
