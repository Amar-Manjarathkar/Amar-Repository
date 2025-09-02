class Solution:
    def isBalanced(self, s):
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ""
