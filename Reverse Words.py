class Solution:
    def reverseWords(self, s):
        # Split by dot
        parts = s.split(".")
        
        # Remove empty words (caused by multiple dots / leading / trailing dots)
        words = [w for w in parts if w]
        
        # Reverse the list of words
        words.reverse()
        
        # Join with single dot
        return ".".join(words)
