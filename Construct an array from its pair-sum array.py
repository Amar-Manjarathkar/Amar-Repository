class Solution:
    def constructArr(self, arr):
        n2 = len(arr)
        
        # Base Case 1: Empty input means original size was 0 or 1.
        # Returning a single element [0] is a safe bet for n=1.
        if n2 == 0:
            return [0] 
        
        # Calculate size of original array 'n'
        import math
        # n*(n-1)/2 = n2  => n^2 - n - 2*n2 = 0
        n = int((1 + math.isqrt(1 + 8*n2)) // 2)

        # Base Case 2: n=2 (arr has 1 element)
        # If arr=[S], then res=[0, S] works because 0+S = S
        if n == 2:
            return [0, arr[0]]

        # Logic for n >= 3
        S1 = arr[0]      # res[0] + res[1]
        S2 = arr[1]      # res[0] + res[2]
        S3 = arr[n-1]    # res[1] + res[2] (Start of the second "row" of pairs)

        # Calculate first three elements
        a = (S1 + S2 - S3) // 2  # res[0]
        b = S1 - a               # res[1]
        c = S2 - a               # res[2]

        res = [0] * n
        res[0], res[1], res[2] = a, b, c

        # Fill remaining elements
        # According to the problem structure, arr[0]...arr[n-2] are sums involving res[0]
        # arr[i-1] corresponds to res[0] + res[i]
        for i in range(3, n):
            res[i] = arr[i-1] - a

        return res  # <--- CHANGED: Return the list, not True
