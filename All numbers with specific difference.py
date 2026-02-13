class Solution:
    def getCount(self, n, d):
        # Helper to calculate sum of digits efficiently
        def get_sum(num):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        low = 1
        high = n
        first_occurrence = -1

        # Binary Search: O(log n * log10 n)
        while low <= high:
            mid = (low + high) // 2
            
            # Check the condition: number - sum_of_digits >= d
            if (mid - get_sum(mid)) >= d:
                first_occurrence = mid
                high = mid - 1  # Look for a smaller number to the left
            else:
                low = mid + 1   # Condition not met, look to the right

        # If no such number was found
        if first_occurrence == -1:
            return 0
            
        # All numbers from first_occurrence up to n satisfy the condition
        return n - first_occurrence + 1
