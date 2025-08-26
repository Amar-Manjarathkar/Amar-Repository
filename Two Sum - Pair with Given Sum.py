class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for num in arr:
            res = target - num
            if res in seen:
                return True
            seen.add(num)
        return False
