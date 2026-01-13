class Solution:
    def canServe(self, arr):
        # code here
        ten = 0
        five = 0
        for num in arr:
            if num == 5:
                five +=1
            elif num == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >=3:
                    five -=3
                else:
                    return False
        return True    
            
        
            
        
        
                
            
        
