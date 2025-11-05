import math

class Solution:
	def minSquares(self, n):
		# Pre-calculate all perfect squares less than or equal to n
		squares = []
		j = 1
		while j * j <= n:
			squares.append(j * j)
			j += 1
		
		# dp[i] will store the min squares for i
		# Initialize with a large value
		dp = [float('inf')] * (n + 1)
		
		# Base case
		dp[0] = 0
		
		# This is the "knapsack" style DP
		# For each number i...
		for i in range(1, n + 1):
			# Try subtracting each square
			for s in squares:
				if i < s:
					# If the square is bigger than i, no need to check
					# further squares (since they are sorted)
					break
				
				# The result for i is the minimum of its current value
				# or (1 + the result for the remainder)
				dp[i] = min(dp[i], 1 + dp[i - s])
				
		return dp[n]
