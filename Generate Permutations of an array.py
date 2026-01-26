class Solution:
    def permuteDist(self, arr):
        res = []
        
        def backtrack(start):
            # Base case: if start reaches the end of the array, a permutation is complete
            if start == len(arr):
                res.append(arr[:])
                return
            
            for i in range(start, len(arr)):
                # Swap the current element with the element at the 'start' index
                arr[start], arr[i] = arr[i], arr[start]
                
                # Recursively generate permutations for the remaining elements
                backtrack(start + 1)
                
                # Backtrack: swap back to restore the original array for the next iteration
                arr[start], arr[i] = arr[i], arr[start]
        
        backtrack(0)
        return res
