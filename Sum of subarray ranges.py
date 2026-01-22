class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)
        
        def get_sum(is_max):
            total = 0
            # left[i] stores the distance to the previous element 
            # that is larger/smaller than arr[i]
            left = [0] * n
            # right[i] stores the distance to the next element 
            # that is larger/smaller than arr[i]
            right = [0] * n
            stack = []
            
            # Find boundaries to the left
            for i in range(n):
                while stack and (arr[stack[-1]] < arr[i] if is_max else arr[stack[-1]] > arr[i]):
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)
            
            stack = []
            # Find boundaries to the right
            # Note: Use <= or >= on one side to handle duplicate elements correctly
            for i in range(n - 1, -1, -1):
                while stack and (arr[stack[-1]] <= arr[i] if is_max else arr[stack[-1]] >= arr[i]):
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)
                
            for i in range(n):
                total += arr[i] * left[i] * right[i]
            return total

        return get_sum(True) - get_sum(False)
