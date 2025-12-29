class Solution:
    def kthElement(self, a, b, k):
        # code here
        c = a+b
        c.sort()
        for i in range(len(c)):
            if i == k-1:
                return c[i]
