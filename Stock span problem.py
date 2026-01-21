class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        # res[i] will store the span for day i
        res = [0] * n
        # stack will store indices of stock prices
        stack = []
        
        for i in range(n):
            # Pop elements from stack while stack is not empty and 
            # arr[top] is less than or equal to arr[i]
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            # If stack is empty, then arr[i] is greater than all 
            # elements on left of it. Else, arr[i] is greater than 
            # all elements after the index at top of stack.
            if not stack:
                res[i] = i + 1
            else:
                res[i] = i - stack[-1]
            
            # Push this element's index to stack
            stack.append(i)
            
        return res
