class Solution:
    def nonRepeatingChar(self,s):
        #code here
        frequency_map = {}
        
        for char in s:
            frequency_map[char] = frequency_map.get(char,0)+1
            
        for char in s:
            if frequency_map[char] == 1:
                return char
        return '$'
    
    
