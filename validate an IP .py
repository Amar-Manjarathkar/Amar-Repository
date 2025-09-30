class Solution:
    def isValid(self, s):
        # code here
        parts = s.split(".")
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part.isdigit():
                return False
                
            if len(part) > 1 and part[0] == '0':
                return False
            
            num = int(part)
            if not (0 <= num <= 255):
                return False
                
        
        return True
        
        
