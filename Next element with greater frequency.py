class Solution:
    def nextFreqGreater(self, arr):
        # code here
        n = len(arr)
        res = [-1] * n
        freq = {}
        stack = []
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        # print(frequency_map)
        for i in range(n - 1, -1, -1):
            curr_val = arr[i]
            curr_freq = freq[curr_val]
            
            while stack and freq[stack[-1]] <= curr_freq:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(curr_val)
            
        return res
