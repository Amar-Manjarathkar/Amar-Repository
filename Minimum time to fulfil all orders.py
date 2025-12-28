import math

class Solution:
    def minTime(self, ranks, n):
        def can_make_donuts(time, ranks, target):
            total_donuts = 0
            for r in ranks:
                # Calculate k donuts using the quadratic formula derivation:
                # r * k * (k + 1) / 2 <= time
                # k^2 + k - (2 * time / r) <= 0
                k = int((-1 + math.sqrt(1 + (8 * time / r))) / 2)
                total_donuts += k
                if total_donuts >= target:
                    return True
            return total_donuts >= target

        low = 0
        high = 10**8  # Sufficient upper bound based on constraints
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_make_donuts(mid, ranks, n):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
