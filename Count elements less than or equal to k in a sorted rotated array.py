class Solution:
    def countLessEqual(self, arr, x):
        #code here
        count=0
        for r in arr:
            if r <= x:
                count+=1
        return count
