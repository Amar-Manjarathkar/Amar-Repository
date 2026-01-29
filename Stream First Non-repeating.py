from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = {}      # To store frequency of each character
        q = deque()    # To store candidates for first non-repeating
        ans = []       # To store the result string
        
        for char in s:
            # 1. Update frequency
            freq[char] = freq.get(char, 0) + 1
            
            # 2. If first appearance, add to queue
            if freq[char] == 1:
                q.append(char)
            
            # 3. Clean up the front of the queue
            # Remove characters that have become repeating
            while q and freq[q[0]] > 1:
                q.popleft()
            
            # 4. Determine the answer for this step
            if q:
                ans.append(q[0])
            else:
                ans.append('#')
                
        return "".join(ans)
