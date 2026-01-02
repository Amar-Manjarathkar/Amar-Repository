class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                # Swap 0 to the front
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # 1 is in the middle, just move on
                mid += 1
            else: # arr[mid] == 2
                # Swap 2 to the back
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr
