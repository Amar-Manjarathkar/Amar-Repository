class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, prev, strk = 0,0,1
        for i in range(1,len(s)):
            if s[i] == s[i - 1]: strk += 1
            else:
                prev = strk
                strk = 1
            if strk <= prev: res += 1
        
        return res

        
