class Solution:
    def findMaxSum(self, arr):
        # handle empty input
        if not arr:
            return 0

        incl = arr[0]   # max sum including previous house
        excl = 0        # max sum excluding previous house

        for i in range(1, len(arr)):
            # if we exclude current house, best is max(incl, excl)
            new_excl = max(incl, excl)
            # if we include current house, we must add arr[i] to previous excl
            incl = excl + arr[i]
            # update excl
            excl = new_excl

        return max(incl, excl)
