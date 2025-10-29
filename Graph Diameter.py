from collections import deque

class Solution:
    
    # Helper function to perform BFS from a given start node
    # It returns two values:
    # 1. The node that is farthest from the start_node
    # 2. The distance (number of edges) to that farthest node
    def _bfs(self, start_node, V, adj):
        # visited[i] = True if node i has been visited
        visited = [False] * V
        # queue stores tuples of (node, current_distance)
        queue = deque()
        
        # Start BFS from start_node with distance 0
        queue.append((start_node, 0))
        visited[start_node] = True
        
        max_dist = 0
        farthest_node = start_node
        
        while queue:
            curr_node, dist = queue.popleft()
            
            # Check if this node is the new farthest node
            if dist > max_dist:
                max_dist = dist
                farthest_node = curr_node
                
            # Add all unvisited neighbors to the queue
            for neighbor in adj[curr_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
                    
        return farthest_node, max_dist

    def diameter(self, V, edges):
        
        # 1. Build the adjacency list to represent the graph
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Pass 1: Run BFS from an arbitrary node (node 0)
        # Find the farthest node (node_A) from it.
        node_A, dist_A = self._bfs(0, V, adj)
        
        # 3. Pass 2: Run BFS again, starting from node_A
        # The distance to the farthest node from node_A is the diameter.
        node_B, diameter = self._bfs(node_A, V, adj)
        
        return diameter
