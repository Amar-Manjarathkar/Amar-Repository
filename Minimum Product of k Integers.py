import heapq

class Solution:
    def minProduct(self, arr, k): 
        MOD = 10**9 + 7
        
        # Step 1: Use heapq.nsmallest to get k smallest efficiently
        k_smallest = heapq.nsmallest(k, arr)
        
        # Step 2: Compute product modulo MOD
        result = 1
        for num in k_smallest:
            result = (result * num) % MOD
        
        return result
