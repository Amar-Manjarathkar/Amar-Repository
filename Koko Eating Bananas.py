import math

class Solution:
    def kokoEat(self, arr, k):
        # The lowest possible speed is 1
        # The highest speed needed is the max pile size
        low = 1
        high = max(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total hours spent at speed 'mid'
            hours_spent = 0
            for pile in arr:
                # This is a shorthand for math.ceil(pile / mid)
                hours_spent += (pile + mid - 1) // mid
            
            if hours_spent <= k:
                # Koko can finish, but let's see if she can go slower
                ans = mid
                high = mid - 1
            else:
                # Koko is too slow, must increase speed
                low = mid + 1
                
        return ans
