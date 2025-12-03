import math
from typing import List
class Solution:
	def tsp(self, cost):
		# code here



# class Solution:
# 	def tsp(self, cost: List[List[int]]) -> int:
		N = len(cost)
		
		# Set a large integer for infinity. Max cost is less than 150,000. 10^9 is safe.
		INF = 10**9 
		
		# DP table: dp[mask][i] is the minimum cost to visit cities in 'mask', ending at city 'i'.
		# Size: 2^N rows x N columns
		dp = [[INF] * N for _ in range(1 << N)]
		
		START_CITY = 0
		
		# 1. Base Case: Starting the tour at city 0.
		# dp[1][0] = 0 (1 << 0 is 1)
		dp[1 << START_CITY][START_CITY] = 0
		
		# 2. Iterate through all masks (subsets of cities visited)
		# Start from mask 1 (only city 0) up to 2^N - 1 (all cities)
		for mask in range(1, 1 << N):
			# Iterate through all possible ending cities 'i'
			for i in range(N):
				
				# Check if city 'i' is included in the current 'mask'
				# (i-th bit is set)
				if (mask & (1 << i)):
					
					# previous_mask is the set of cities visited before reaching city 'i'.
					# It's 'mask' with the i-th bit turned off using XOR.
					previous_mask = mask ^ (1 << i)
					
					# If previous_mask is 0, we are at the base case, so skip
					if previous_mask == 0:
						continue
					
					# Find the minimum cost to reach city 'i' from any city 'j' 
					# that was visited in the previous_mask.
					
					current_min_cost = dp[mask][i]
					
					for j in range(N):
						# Check if city 'j' was in the previous_mask
						if (previous_mask & (1 << j)):
							
							# Cost to move from j to i
							travel_cost = cost[j][i]
							
							# Minimum cost to reach city j in the previous state
							cost_to_j = dp[previous_mask][j]
							
							# New cost = Min cost to reach j + cost from j to i
							new_cost = cost_to_j + travel_cost
							
							if new_cost < current_min_cost:
								current_min_cost = new_cost
					
					# Update DP table after checking all possible 'j' predecessors
					dp[mask][i] = current_min_cost


		# 3. Final Answer: Minimum cost to return to city 0.
		
		# The final mask where all cities are visited
		FINAL_MASK = (1 << N) - 1
		min_total_cost = INF
		
		# The final step is moving from any city 'i' back to city 0.
		for i in range(N):
            # i must be in the final mask, which is always true here, 
            # but we use the DP value to calculate the final step.
			
			# Cost of the path that ends at city i, having visited all cities.
			cost_to_i = dp[FINAL_MASK][i]
			
			# Cost of returning from city i to city 0.
			return_cost = cost[i][START_CITY]
			
			total_cost = cost_to_i + return_cost
			
			if total_cost < min_total_cost:
				min_total_cost = total_cost
				
		return min_total_cost
