from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        
        if k == 0:
            return -1
        
        INF = 10**18
        dp = [INF] * k
        
        # paint the first wall
        for c in range(k):
            dp[c] = costs[0][c]
        
        for i in range(1, n):
            new_dp = [INF] * k
            
            # find best and second best from previous row
            best_val = second_val = INF
            best_idx = -1
            for c in range(k):
                if dp[c] < best_val:
                    second_val = best_val
                    best_val = dp[c]
                    best_idx = c
                elif dp[c] < second_val:
                    second_val = dp[c]
            
            for c in range(k):
                # minimum cost of previous wall with colour != c
                if best_idx != c:
                    prev_min = best_val
                else:
                    prev_min = second_val
                
                if prev_min == INF:          # impossible to reach this state
                    continue
                new_dp[c] = costs[i][c] + prev_min
            
            # check impossibility for current wall
            if all(x == INF for x in new_dp):
                return -1
            
            dp = new_dp
        
        ans = min(dp)
        return ans if ans < INF else -1
