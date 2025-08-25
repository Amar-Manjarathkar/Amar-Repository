class Solution:    
    def findUnion(self, a, b):
        # code here
        
        arr_1 = set(a)
        arr_2 = set(b)
        res = []
        
        for num_1 in arr_1:
            if num_1 not in res:
                res.append(num_1)
        for num_2 in arr_2:
            if num_2 not in res:
                res.append(num_2)
        return res
                
