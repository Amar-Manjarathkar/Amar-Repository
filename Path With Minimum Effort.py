from typing import List
import heapq
import math # Used for infinity

class Solution:
    """
    Finds the minimum possible path cost (maximum absolute difference)
    from (0, 0) to (n-1, m-1) using Dijkstra's Algorithm.
    
    Time Complexity: O(N*M * log(N*M))
    """
    def minCostPath(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
            
        n, m = len(mat), len(mat[0])
        
        # dist[r][c] stores the minimum maximum absolute difference found 
        # on any path from (0, 0) to (r, c).
        # Initialize all distances to infinity.
        dist = [[math.inf] * m for _ in range(n)]
        
        # Priority Queue stores tuples: (max_diff_so_far, r, c)
        # We start at (0, 0) with an initial max_diff_so_far of 0.
        pq = [(0, 0, 0)]
        dist[0][0] = 0
        
        # Up, Down, Left, Right movement directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            # Pop the cell with the smallest max_diff_so_far
            max_diff_so_far, r, c = heapq.heappop(pq)
            
            # If we reached the destination, this is the minimum max difference
            if r == n - 1 and c == m - 1:
                return max_diff_so_far
                
            # Skip stale entries (an entry with a better max_diff has already been processed)
            if max_diff_so_far > dist[r][c]:
                continue
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries
                if 0 <= nr < n and 0 <= nc < m:
                    
                    # 1. Calculate the cost of the *current edge*
                    edge_cost = abs(mat[r][c] - mat[nr][nc])
                    
                    # 2. Calculate the *new path cost* (the max difference encountered so far)
                    # The new max difference is the maximum of the previous max difference 
                    # and the cost of the current edge.
                    new_max_diff = max(max_diff_so_far, edge_cost)
                    
                    # 3. Relaxation step (Dijkstra's update)
                    if new_max_diff < dist[nr][nc]:
                        dist[nr][nc] = new_max_diff
                        heapq.heappush(pq, (new_max_diff, nr, nc))
                        
        # Should not be reached if a path exists, but included for completeness
        return dist[n-1][m-1]
