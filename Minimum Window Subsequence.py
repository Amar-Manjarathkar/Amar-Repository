class Solution:
    def minWindow(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        i, j = 0, 0
        min_len = float('inf')
        start_index = -1

        while i < n1:
            # 1. Forward Pass: Find s2 as a subsequence in s1
            if s1[i] == s2[j]:
                j += 1
                
                # If we found the entire subsequence s2
                if j == n2:
                    end = i
                    j -= 1
                    
                    # 2. Backward Pass: Optimize the start to find the smallest window
                    while j >= 0:
                        if s1[i] == s2[j]:
                            j -= 1
                        i -= 1
                    
                    # Move i back to the start of the window (i was decremented one extra time)
                    i += 1
                    current_len = end - i + 1
                    
                    # 3. Update minimum window
                    if current_len < min_len:
                        min_len = current_len
                        start_index = i
                    
                    # Reset j to 0 to start searching for the next potential window
                    j = 0
            
            # Continue searching from the next character after the optimized start
            i += 1

        return "" if start_index == -1 else s1[start_index : start_index + min_len]
