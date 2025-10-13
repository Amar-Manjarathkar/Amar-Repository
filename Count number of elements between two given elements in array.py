class Solution:
    def getCount(self, arr, num1, num2):
        #Your code goes here
        n = len(arr)
        num_1_index = 0
        num_2_index = 0
        for i in range(n):
            if arr[i] == num1:
                num_1_index = i
                break
            
        for i in range(n-1,-1,-1):
            if arr[i] == num2:
                num_2_index = i
                break
        if num_1_index == -1 or num_2_index == -1:
            return 0
        res=len(arr[num_1_index:num_2_index]) -1
        return  max(0,res)
                
