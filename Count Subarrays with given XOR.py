class Solution:
    def subarrayXor(self, arr, k):
        prefix_xor = 0
        count = 0
        freq = {0: 1}   # Important! For subarrays starting from index 0
        
        for num in arr:
            prefix_xor ^= num
            
            # Check if there exists a prefix with XOR = prefix_xor ^ k
            if (prefix_xor ^ k) in freq:
                count += freq[prefix_xor ^ k]
            
            # Store current prefix_xor
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count
