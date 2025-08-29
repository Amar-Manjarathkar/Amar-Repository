# User function Template for python3
class Solution:
    def removeVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = [ch for ch in s if ch.lower() not in vowels]
        return ''.join(result)
