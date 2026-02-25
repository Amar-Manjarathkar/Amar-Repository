class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        prefix_sum = 0
        max_len = 0
        first_occurance = {}
        for i in range(len(arr)):
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            if prefix_sum > 0:
                max_len = i + 1
            if prefix_sum not in first_occurance:
                first_occurance[prefix_sum] = i
                
            if (prefix_sum - 1) in first_occurance:
                length = i - first_occurance[prefix_sum - 1]
                max_len = max(max_len, length)
        return max_len
        
