class Solution:
    def nCr(self, n, r):
        # code here
        if r > n :
            return 0
        def factorial(n):
            fact = 1
            if n == 0 or n == 1:
                return fact
            for i in range(1, n+1):  # start from 1 up to n
                fact = fact * i
            return fact
        return factorial(n) // (factorial(n - r) * factorial(r))
                
                
