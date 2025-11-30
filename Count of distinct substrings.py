class Solution:
    def countSubs(self, s):
        # code here
        result = set()
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                result1 = s[i:j]
                result.add(result1)
        return len(result)
