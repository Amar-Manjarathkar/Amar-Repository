class Solution:
    def kthMissing(self, arr, k):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Calculate how many numbers are missing before arr[mid]
            missing_before_mid = arr[mid] - (mid + 1)
            
            if missing_before_mid < k:
                low = mid + 1
            else:
                high = mid - 1
        
        # After the loop, 'low' is the index where the missing count exceeds or equals k
        # The k-th missing number is calculated as low + k
        return low + k
