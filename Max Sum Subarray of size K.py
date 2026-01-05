class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(len(arr) - k):
            window_sum = window_sum - arr[i] + arr[i + k]
            max_sum = max(max_sum, window_sum)
        return max_sum
