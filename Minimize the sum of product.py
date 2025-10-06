class Solution:
    def minValue(self, arr1, arr2):
        # Sort arr1 in ascending order
        arr1.sort()
        # Sort arr2 in descending order
        arr2.sort(reverse=True)
        # Calculate the sum of products
        result = 0
        for i in range(len(arr1)):
            result += arr1[i] * arr2[i]
        return result
