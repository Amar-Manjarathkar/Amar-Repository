class Solution:
    def isInterleave(self, s1, s2, s3):
        ns1, ns2, ns3 = len(s1), len(s2), len(s3)
        if ns1 + ns2 != ns3:
            return False

        # Memoization cache to store results of (i, j)
        memo = {}

        def solve(i, j):
            # i: current index in s1
            # j: current index in s2
            # k: current index in s3 (is always i + j)
            k = i + j
            
            # Base case: We've successfully reached the end of all strings
            if k == ns3:
                return True
            
            # Check cache
            if (i, j) in memo:
                return memo[(i, j)]

            res = False
            
            # Choice 1: Try to match s3[k] with s1[i]
            if i < ns1 and s1[i] == s3[k]:
                res = res or solve(i + 1, j) # Recurse, advancing s1's pointer
            
            # Choice 2: Try to match s3[k] with s2[j]
            if j < ns2 and s2[j] == s3[k]:
                res = res or solve(i, j + 1) # Recurse, advancing s2's pointer

            # Store result in cache and return
            memo[(i, j)] = res
            return res

        # Start the recursion from the beginning of all strings
        return solve(0, 0)
