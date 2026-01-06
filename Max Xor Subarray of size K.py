class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        if n < k:
            return 0
        
        # 1. Calculate the XOR sum of the first window
        current_xor = 0
        for i in range(k):
            current_xor ^= arr[i]
        
        max_xor = current_xor
        
        # 2. Slide the window from index k to n-1
        for i in range(k, n):
            # XOR out the element that is leaving (arr[i - k])
            # XOR in the element that is entering (arr[i])
            current_xor = current_xor ^ arr[i - k] ^ arr[i]
            
            max_xor = max(max_xor, current_xor)
            
        return max_xor
