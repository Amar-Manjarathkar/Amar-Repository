class Solution:
    def getPairs(self, arr):
        arr.sort()               # Step 1: sort array → O(n log n)
        res = []
        n = len(arr)
        
        left, right = 0, n - 1   # Step 2: two pointers
        
        while left < right:
            s = arr[left] + arr[right]
            
            if s == 0:
                res.append([arr[left], arr[right]])   # valid pair
                
                # Step 3: skip duplicates
                left_val, right_val = arr[left], arr[right]
                while left < right and arr[left] == left_val:
                    left += 1
                while left < right and arr[right] == right_val:
                    right -= 1
                    
            elif s < 0:
                left += 1
            else:
                right -= 1
                
        return res
