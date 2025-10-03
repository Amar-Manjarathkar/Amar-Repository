class Solution:
    def findMaxProduct(self, arr: list[int], k: int) -> int:
        n = len(arr)

        if k > n or k <= 0:
            return 0
        
        # Initialize max_product to the smallest possible number
        max_product = -float('inf')
        current_product = 1
        
        # The left boundary of the sliding window
        left = 0
        
        # The right boundary of the sliding window (slides from 0 to n-1)
        for right in range(n):
            
            # 1. Expand the window (Multiplication)
            current_product *= arr[right]
            
            # 2. Check if the window is fully formed (size == k)
            if right - left + 1 == k:
                
                # Update the maximum product
                if current_product > max_product:
                    max_product = current_product
                
                # 3. Contract the window (Division)
                # To slide the window one step, we divide by the element leaving the window.
                # This works if the element leaving the window is not zero.
                
                element_leaving = arr[left]
                
                if element_leaving != 0:
                    # Division is safe: O(1) step
                    current_product //= element_leaving
                else:
                    # If the element leaving is 0, we can't divide.
                    # A '0' in the window made current_product = 0.
                    # Since we are moving past the 0, the next window must be recalculated
                    # by starting the product from the element at (left + 1).
                    # Recalculating the product for the *new* window (size k-1 + 1 = k) is simpler
                    # and necessary after a zero. The simplest way is to reset the product to 1
                    # and let the loop naturally multiply the new elements.
                    # Since we are already moving the window, we just need to ensure the product 
                    # for the new window is correct.
                    current_product = 1 
                    # We continue the loop, and the next iteration starts from the correct 'right'
                    # and a reset 'left', allowing the product to rebuild.
                    
                # 4. Slide the window forward
                left += 1

        return max_product
