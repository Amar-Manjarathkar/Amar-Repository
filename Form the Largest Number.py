class Solution:

    def findLargest(self, arr):
        # Convert to string
        arr = [str(num) for num in arr]

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] + right[j] > right[j] + left[i]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        sorted_arr = merge_sort(arr)
        result = ''.join(sorted_arr)

        return "0" if result[0] == '0' else result
