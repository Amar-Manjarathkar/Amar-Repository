#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        temp = n
        rem = 0
        count = 0
        while n > 0:
            rem = n % 10
            if rem != 0 and temp % rem == 0:
                count+=1
            n= n // 10
        return count
            
        
