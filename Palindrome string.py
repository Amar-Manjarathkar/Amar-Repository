class Solution:
    def isPalindrome(self, s):
        n = len(s)
        
        # Compare characters from start and end
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True
