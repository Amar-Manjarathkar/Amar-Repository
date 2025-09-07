class Solution:
    def maxNtype(self , arr):
        n = len(arr)

        # Case 1: Ascending
        if arr == sorted(arr):
            return 1

        # Case 2: Descending
        if arr == sorted(arr, reverse=True):
            return 2

        # Case 3: Ascending Rotated
        if sorted(arr) == arr[arr.index(min(arr)):] + arr[:arr.index(min(arr))]:
            return 4

        # Case 4: Descending Rotated
        if sorted(arr, reverse=True) == arr[arr.index(max(arr)):] + arr[:arr.index(max(arr))]:
            return 3

        return -1
