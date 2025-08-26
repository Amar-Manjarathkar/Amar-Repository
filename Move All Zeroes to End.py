class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        pos = 0  # index where next non-zero element should go

        for i in range(n):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        return arr
