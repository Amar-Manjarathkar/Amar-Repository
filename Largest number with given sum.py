class Solution:
    # Function to return the largest possible number of n digits
    # with sum equal to given sum.
    def largestNum(self, n, s):
        
        # 1. The ONLY impossible case is if the sum 's' is greater 
        #    than the max possible sum (a string of all 9s).
        if s > 9 * n:
            return "-1"
            
        # 2. Handle the case where the sum is 0. Based on the test case,
        #    this should result in a string of 'n' zeros. The main loop
        #    below handles this correctly, so no special 'if s==0' check is needed.
        #    For example, if n=6, s=0, the loop will append "0" six times.

        # 3. Build the result as a string
        res = ""
        for i in range(n):
            # Greedily pick the largest possible digit for the current position
            if s >= 9:
                res += "9"
                s -= 9
            else:
                res += str(s)
                s = 0
        
        return res
