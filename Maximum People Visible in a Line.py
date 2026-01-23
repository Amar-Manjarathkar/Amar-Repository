class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        if n == 0: return 0
        
        # left_visible[i] = how many people person i can see to their left
        left_visible = [0] * n
        stack = []
        
        for i in range(n):
            # While stack is not empty and the current person is taller than 
            # the person at the top of the stack, they can see that person.
            # However, we only care about people IMMEDIATELY visible.
            # A person sees everyone until they hit someone >= themselves.
            
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            
            if not stack:
                # Can see everyone to the left
                left_visible[i] = i
            else:
                # Can see everyone between current index and the blocking person
                left_visible[i] = i - stack[-1] - 1
            
            stack.append(i)
            
        # Clear stack for the right pass
        stack = []
        right_visible = [0] * n
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
                
            if not stack:
                right_visible[i] = (n - 1) - i
            else:
                right_visible[i] = stack[-1] - i - 1
                
            stack.append(i)
            
        # Result is Max(left + right + self)
        ans = 0
        for i in range(n):
            ans = max(ans, left_visible[i] + right_visible[i] + 1)
            
        return ans
