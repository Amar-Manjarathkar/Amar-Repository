import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Build adjacency list: graph[u] = [(v, time), ...]
        graph = [[] for _ in range(n)]
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # dist[i] = shortest time to reach node i
        # ways[i] = number of ways to reach i with dist[i] time
        dist = [float('inf')] * n
        ways = [0] * n
        
        dist[0] = 0
        ways[0] = 1
        
        # Min-heap: (current_time, node)
        pq = [(0, 0)]  # (time, node)
        
        while pq:
            time, u = heapq.heappop(pq)
            
            # If we already found a better way, skip
            if time > dist[u]:
                continue
                
            for v, wt in graph[u]:
                new_time = time + wt
                
                if new_time < dist[v]:
                    # Found a better path
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_time, v))
                elif new_time == dist[v]:
                    # Found another shortest path
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n-1]
