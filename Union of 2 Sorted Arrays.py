class Solution:
    def findUnion(self, a, b):
        # code here 
        seenA = []
        
        for num in a:
            if num not in seenA:
                seenA.append(num)
        
        for num in b:
            if num not in seenA:
                seenA.append(num)
        return seenA
