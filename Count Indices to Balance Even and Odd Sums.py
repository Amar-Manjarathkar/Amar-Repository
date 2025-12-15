class Solution:
    def cntWays(self, arr):
           
        n = len(arr)
        
        # Optimization 1: Use Slicing for super-fast initial summation
        # arr[::2] gets all even indices, arr[1::2] gets all odd indices
        right_even = sum(arr[::2])
        right_odd = sum(arr[1::2])
        
        left_even = 0
        left_odd = 0
        count = 0
        
        for i in range(n):
            val = arr[i]
            
            # Step 1: Remove current element from Right sums
            # Use bitwise & 1 to check for odd (faster than % 2)
            if i & 1: 
                right_odd -= val
            else:
                right_even -= val
            
            # Step 2: Check the Balance Condition
            # If we remove index i:
            # New Even Sum = Left Even + Right Odd (shifted)
            # New Odd Sum  = Left Odd + Right Even (shifted)
            if left_even + right_odd == left_odd + right_even:
                count += 1
            
            # Step 3: Add current element to Left sums for next iteration
            if i & 1:
                left_odd += val
            else:
                left_even += val
                
        return count # Output: 1
