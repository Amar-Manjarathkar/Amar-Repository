class Solution:
    def hasTripletSum(self, arr, target):
        # Edge cases
        if not arr or len(arr) < 3:
            return False

        # Sort array to use two-pointer method
        arr.sort()

        # Iterate for each element as first element of triplet
        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]

                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return False
