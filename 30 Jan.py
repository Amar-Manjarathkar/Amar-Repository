from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        # Get the size of the queue
        n = len(q)
        half = n // 2
        
        # Step 1: Extract the first half into a temporary list
        # Since q is a deque (based on your error), we use popleft()
        first_half = []
        for _ in range(half):
            first_half.append(q.popleft())
            
        # Step 2: Interleave elements back into the original q
        # Currently, q only contains the second half [3, 1]
        # first_half contains [2, 4]
        for val in first_half:
            # 1. Add element from the first half to the back
            q.append(val)
            
            # 2. Take the element from the front of the second half 
            # and move it to the back
            q.append(q.popleft())
            
        # The original object q is now modified in-place to [2, 3, 4, 1]
        return q
        
