class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        result = []
        
        for num in arr:
            if num < k and num >= 10:  # at least two digits and less than k
                n = num
                prev = n % 10
                n //= 10
                valid = True
                
                while n > 0:
                    curr = n % 10
                    if abs(curr - prev) != 1:
                        valid = False
                        break
                    prev = curr
                    n //= 10
                
                if valid:
                    result.append(num)
        
        return result
