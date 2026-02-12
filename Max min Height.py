class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def isPossible(target):
            # Track additions using a difference array logic
            water_added = [0] * n
            total_water_on_current = 0
            days_used = 0
            
            for i in range(n):
                # Remove the effect of watering that ended before this flower
                if i >= w:
                    total_water_on_current -= water_added[i - w]
                
                current_height = arr[i] + total_water_on_current
                
                if current_height < target:
                    needed = target - current_height
                    days_used += needed
                    
                    if days_used > k:
                        return False
                    
                    # Apply watering starting at i and lasting for w flowers
                    water_added[i] = needed
                    total_water_on_current += needed
            
            return days_used <= k

        # Binary Search for the maximum possible "minimum height"
        low = min(arr)
        high = min(arr) + k
        ans = low
        
        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
