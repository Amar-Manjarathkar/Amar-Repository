#User function Template for python3

class Solution:
    def customSort(self, arr):
        # Find the midpoint of the array
        # n will be the index where the second half begins
        n = len(arr) // 2
        
        # Sort the first half (from index 0 up to n-1)
        # in ascending (default) order.
        # We slice the first half, sort it, and assign it back.
        arr[:n] = sorted(arr[:n])
        
        # Sort the second half (from index n to the end)
        # in descending order.
        # We slice the second half, sort it, and assign it back.
        arr[n:] = sorted(arr[n:], reverse=True)
        
        # Return the modified array
        return arr
