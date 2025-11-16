class Solution:
    def LCIS(self, a, b):
        # Get the lengths of the two arrays
        n = len(a)
        m = len(b)
        
        if n == 0 or m == 0:
            return 0
            
        # dp[j] will store the length of the LCIS
        # ending at b[j], considering elements a[0...i]
        dp = [0] * m
        
        # This will store the overall maximum length found
        max_len = 0
        
        # Iterate through each element in the first array 'a'
        for i in range(n):
            # For each a[i], we scan 'b'.
            # 'current_best_len' tracks the length of the longest
            # LCIS ending *before* the current b[j] with a value
            # *less than* a[i].
            current_best_len = 0
            
            # Iterate through each element in the second array 'b'
            for j in range(m):
                
                # Case 1: a[i] == b[j]
                # We found a common element.
                # The length of the LCIS ending at this element is
                # 1 + the length of the best LCIS we've seen so far
                # (which is 'current_best_len').
                if a[i] == b[j]:
                    dp[j] = current_best_len + 1
                
                # Case 2: a[i] > b[j]
                # The current element a[i] is greater than b[j].
                # This means that b[j] (and the LCIS ending at dp[j])
                # is a *potential predecessor* for a[i].
                # We update 'current_best_len' to be the max of
                # itself and the LCIS length ending at b[j].
                elif a[i] > b[j]:
                    current_best_len = max(current_best_len, dp[j])
                
                # Case 3: a[i] < b[j]
                # We do nothing. b[j] cannot be part of an increasing
                # subsequence that uses a[i], and the LCIS ending at b[j]
                # (dp[j]) cannot be a predecessor for a[i].
            
            # After checking all 'b' elements for a single 'a[i]',
            # update the overall max_len. We can also do this
            # inside the a[i] == b[j] block.
            # max_len = max(max_len, max(dp)) # This is less efficient
        
        # A more efficient way to track max_len is inside the loop
        # (Let's adjust the code above slightly for clarity and efficiency)
        
        # --- Re-written loop for better max_len tracking ---
        
        dp = [0] * m
        max_len = 0
        
        for i in range(n):
            current_best_len = 0
            for j in range(m):
                
                # We save the original value of dp[j] before
                # potentially updating it. This is important.
                # Or wait, no, the logic is simpler.
                
                if a[i] == b[j]:
                    # Update dp[j] based on the best sequence
                    # *before* this match
                    dp[j] = current_best_len + 1
                    
                    # Update the overall max
                    max_len = max(max_len, dp[j])
                    
                elif a[i] > b[j]:
                    # Update the best sequence *before* a match
                    # using the value of dp[j] (which represents
                    # the LCIS ending at b[j] from *previous*
                    # iterations of 'i').
                    current_best_len = max(current_best_len, dp[j])
                    
        return max_len
