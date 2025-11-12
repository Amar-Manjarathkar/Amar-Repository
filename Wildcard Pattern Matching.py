class Solution:
    def wildCard(self, txt, pat):
        m = len(txt)
        n = len(pat)
        
        # Create a DP table, initialized to False
        # dp[i][j] will be True if the first i chars of txt
        # match the first j chars of pat
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # === BASE CASES ===
        
        # 1. Empty text and empty pattern always match
        dp[0][0] = True
        
        # 2. Empty text vs non-empty pattern
        # Only True if the pattern chars are all '*'
        for j in range(1, n + 1):
            if pat[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            # else it remains False
            
        # === FILL THE DP TABLE ===
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # Current characters we are comparing
                # (using i-1 and j-1 for 0-based string indexing)
                txt_char = txt[i - 1]
                pat_char = pat[j - 1]
                
                if pat_char == '?':
                    # '?' matches any char. 
                    # The result depends on the match *before* these chars.
                    dp[i][j] = dp[i - 1][j - 1]
                    
                elif pat_char == '*':
                    # '*' has two choices:
                    # 1. Match zero characters (dp[i][j-1])
                    # 2. Match one or more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    
                else:
                    # Normal character match
                    # They must be equal, AND the previous part must match.
                    if txt_char == pat_char:
                        dp[i][j] = dp[i - 1][j - 1]
                    # else it remains False
                            
        # The final answer is in the bottom-right corner
        return dp[m][n]

# # Example usage (based on your problem description):
# sol = Solution()
# print(f"txt = 'abcde', pat = 'a?c*'  ->  {sol.wildCard('abcde', 'a?c*')}")
# print(f"txt = 'abc', pat = 'ab?'     ->  {sol.wildCard('abc', 'ab?')}")
# print(f"txt = 'abc', pat = 'ab*'     ->  {sol.wildCard('abc', 'ab*')}")
# print(f"txt = 'a', pat = 'aa'        ->  {sol.wildCard('a', 'aa')}")
# print(f"txt = 'abc', pat = 'a*c'     ->  {sol.wildCard('abc', 'a*c')}")
# print(f"txt = 'mississippi', pat = 'm*si*' -> {sol.wildCard('mississippi', 'm*si*')}")
