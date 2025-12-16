class Solution:
    def areRotations(self, s1, s2):
        # code here
        return s2 in (s1+s1)
