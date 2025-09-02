class Solution:
    def isBalanced(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        
        for ch in s:
            if ch in pairs.values():   # opening
                stack.append(ch)
            elif ch in pairs:          # closing
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack
