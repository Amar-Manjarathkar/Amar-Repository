class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        
        # Dictionary to store first occurrence of prefix sum
        prefix_map = {}
        
        prefix_sum = 0
        max_len = 0
        
        for i in range(n):
            # Compute difference
            prefix_sum += (a1[i] - a2[i])
            
            # If prefix sum becomes 0, span is from 0 to i
            if prefix_sum == 0:
                max_len = i + 1
            
            # If prefix sum seen before
            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i
        
        return max_len
