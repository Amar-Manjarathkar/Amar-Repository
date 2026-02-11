class Solution:
    def minCost(self, heights, cost):
        def get_cost(h):
            total = 0
            for i in range(len(heights)):
                total += abs(heights[i] - h) * cost[i]
            return total

        # Search range based on actual tower heights
        low = min(heights)
        high = max(heights)
        ans = get_cost(low)

        while low <= high:
            mid = (low + high) // 2
            
            c_mid = get_cost(mid)
            c_next = get_cost(mid + 1)
            
            ans = min(ans, c_mid, c_next)
            
            # If cost is decreasing, move right
            if c_mid > c_next:
                low = mid + 1
            # If cost is increasing, move left
            else:
                high = mid - 1
                
        return ans
