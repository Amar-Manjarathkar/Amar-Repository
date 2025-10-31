import collections

class Solution:
    def shortCycle(self, V: int, edges: list[list[int]]) -> int:
        # Build the Adjacency List
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Initialize the minimum cycle length to a large value (infinity)
        min_cycle_len = float('inf')

        # Iterate through every vertex as a potential start of the shortest cycle
        for start_node in range(V):
            # For each start node, run a BFS
            
            # dist[v] stores the shortest path length from start_node to v
            dist = {i: float('inf') for i in range(V)}
            
            # parent[v] stores the predecessor of v in the shortest path from start_node
            parent = {i: -1 for i in range(V)}
            
            queue = collections.deque([start_node])
            dist[start_node] = 0
            
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    if dist[v] == float('inf'):
                        # Case 1: v is not visited (Standard BFS step)
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        queue.append(v)
                    elif v != parent[u]:
                        # Case 2: v is visited AND v is not the immediate parent of u.
                        # This means we found a cycle: start_node -> ... -> u -> v -> ... -> start_node
                        
                        # The length of this cycle is dist[u] + dist[v] + 1 (for edge u-v)
                        current_cycle_len = dist[u] + dist[v] + 1
                        
                        # Update the minimum cycle length found so far
                        min_cycle_len = min(min_cycle_len, current_cycle_len)

        # If min_cycle_len is still infinity, no cycle was found
        if min_cycle_len == float('inf'):
            return -1
        else:
            return min_cycle_len
