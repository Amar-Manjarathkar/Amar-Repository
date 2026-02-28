class Solution:
    def findClosestPair(arr1, arr2, x):
        
        i = 0
        j = len(arr2) - 1
        
        min_diff = float('inf')
        result = [0, 0]
        
        while i < len(arr1) and j >= 0:
            
            curr_sum = arr1[i] + arr2[j]
            diff = abs(curr_sum - x)
            
            if diff < min_diff:
                min_diff = diff
                result = [arr1[i], arr2[j]]
            
            # Move pointers
            if curr_sum < x:
                i += 1
            else:
                j -= 1
                
        return result
