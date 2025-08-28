# User function Template for python3

class Solution:
    def removeChars(ob, str1, str2):
        # Put all characters of str2 in a set for O(1) lookups
        remove_set = set(str2)
        
        # Build result by keeping only characters not in str2
        result = []
        for ch in str1:
            if ch not in remove_set:
                result.append(ch)
        
        return "".join(result)
