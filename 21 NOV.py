import heapq
import sys

class Solution:
    def shortestPath(self, V, a, b, edges):
        # 1. Build Adjacency List for STRAIGHT edges only
        # We only need w1 for the Dijkstra runs
        adj = [[] for _ in range(V)]
        for u, v, w1, w2 in edges:
            adj[u].append((v, w1))
            adj[v].append((u, w1))

        # 2. Helper function: Standard Dijkstra
        def get_dists(start_node):
            dists = [float('inf')] * V
            dists[start_node] = 0
            pq = [(0, start_node)]  # (current_cost, u)

            while pq:
                d, u = heapq.heappop(pq)

                # Optimization: If current d > stored dist, skip
                if d > dists[u]:
                    continue

                for v, weight in adj[u]:
                    if dists[u] + weight < dists[v]:
                        dists[v] = dists[u] + weight
                        heapq.heappush(pq, (dists[v], v))
            return dists

        # 3. Run Dijkstra from Source (a) and Destination (b)
        dist_from_a = get_dists(a)
        dist_from_b = get_dists(b)

        # 4. Initialize answer with the "All Straight" path cost
        ans = dist_from_a[b]

        # 5. Iterate over all edges to check the "One Curved Edge" shortcut
        for u, v, w1, w2 in edges:
            # Path: a -> u -> (curved) -> v -> b
            # Only valid if u is reachable from a and v is reachable from b
            if dist_from_a[u] != float('inf') and dist_from_b[v] != float('inf'):
                cost = dist_from_a[u] + w2 + dist_from_b[v]
                if cost < ans:
                    ans = cost
            
            # Path: a -> v -> (curved) -> u -> b (Since edges are undirected)
            if dist_from_a[v] != float('inf') and dist_from_b[u] != float('inf'):
                cost = dist_from_a[v] + w2 + dist_from_b[u]
                if cost < ans:
                    ans = cost

        # 6. Check if destination is unreachable
        if ans == float('inf'):
            return -1
            
        return ans
