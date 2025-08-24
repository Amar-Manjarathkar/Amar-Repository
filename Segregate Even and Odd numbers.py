# User function Template for python3
class Solution:
    def segregateEvenOdd(self, arr):
        # Step 1: Separate evens and odds
        evens = [x for x in arr if x % 2 == 0]
        odds = [x for x in arr if x % 2 != 0]

        # Step 2: Sort them individually
        evens.sort()
        odds.sort()

        # Step 3: Overwrite arr in-place
        arr[:] = evens + odds
