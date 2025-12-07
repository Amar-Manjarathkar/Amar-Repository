class Solution:
    def distinctSubseq(self, s):
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i] = number of distinct subsequences of s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty subsequence
        
        # last occurrence index in dp-space (1..n), -1 means not seen
        last = [-1] * 26
        
        for i in range(1, n + 1):
            ch = s[i - 1]
            idx = ord(ch) - ord('a')
            
            # double the subsequences by adding or not adding s[i-1]
            dp[i] = (2 * dp[i - 1]) % MOD
            
            # if seen before, subtract the subsequences counted before its previous occurrence
            if last[idx] != -1:
                dp[i] = (dp[i] - dp[last[idx] - 1]) % MOD
            
            # update last occurrence of this character
            last[idx] = i
        
        return dp[n] % MOD
