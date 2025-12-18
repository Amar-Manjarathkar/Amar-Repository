class Solution:
    def sortIt(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        
        # Step 1: Partition - all odds to the left (in any order)
        left = 0
        for i in range(n):
            if arr[i] % 2 == 1:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        
        # Now: odds in arr[0:left], evens in arr[left:n]
        
        # Step 2: Sort odd portion in descending order (in-place)
        arr[:left] = sorted(arr[:left], reverse=True)
        
        # Step 3: Sort even portion in ascending order (in-place)
        arr[left:] = sorted(arr[left:])
        
        return arr
