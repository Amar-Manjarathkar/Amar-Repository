class Solution:
    def minTime(self, arr, k):
        # Edge case
        if not arr:
            return 0
        
        low = max(arr)      # Minimum possible time
        high = sum(arr)     # Maximum possible time
        
        while low < high:
            mid = (low + high) // 2
            
            if self.canPaint(arr, k, mid):
                high = mid   # Try smaller maximum time
            else:
                low = mid + 1   # Increase time
        
        return low
    
    def canPaint(self, arr, k, max_time):
        painters = 1
        current_sum = 0
        
        for board in arr:
            if current_sum + board <= max_time:
                current_sum += board
            else:
                painters += 1
                current_sum = board
                
                if painters > k:
                    return False
        
        return True
