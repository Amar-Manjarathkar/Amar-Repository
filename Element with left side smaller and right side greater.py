class Solution:
    def findElement(self, arr):
        n = len(arr)

        # Arrays to store prefix max and suffix min
        left_max = [0] * n
        right_min = [0] * n

        # Fill prefix max
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])

        # Fill suffix min
        right_min[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i])

        # Check the condition
        for i in range(1, n-1):  # first and last cannot be the answer
            if left_max[i-1] < arr[i] < right_min[i+1]:
                return arr[i]

        return -1
