class Solution:
    def firstRepeated(self, arr):
        n = len(arr)
        
        # Step 1: Count frequencies
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Find first element with frequency > 1
        for i in range(n):
            if freq[arr[i]] > 1:
                return i + 1   # 1-based index
        
        return -1   # If no repeating element
