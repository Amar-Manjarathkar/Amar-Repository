from typing import List, Tuple, Dict
import math

class DSU:
    # Standard Disjoint Set Union implementation (path compression & union by rank)
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Simple union (without rank/size optimization for brevity)
            self.parent[root_i] = root_j
            return True
        return False

class Solution:
    def secondMST(self, V: int, edges: List[List[int]]) -> int:
        # Sort edges by weight: [(u, v, w), ...]
        edges.sort(key=lambda x: x[2])
        
        # 1. FIND PRIMARY MST
        dsu = DSU(V)
        mst_weight = 0
        mst_edges = []
        non_mst_edges = []
        
        for u, v, w in edges:
            if dsu.union(u, v):
                mst_weight += w
                mst_edges.append((u, v, w))
            else:
                non_mst_edges.append((u, v, w))

        # Check for disconnected graph (no MST possible)
        if len(mst_edges) != V - 1:
            return -1

        # Build MST Adjacency List
        mst_adj = {i: [] for i in range(V)}
        for u, v, w in mst_edges:
            mst_adj[u].append((v, w))
            mst_adj[v].append((u, w))
        
        # 2. HELPER FUNCTION: Get all edge weights on the unique path u -> v in the MST
        def getAllPathEdgeWeights(u: int, v: int, adj: Dict) -> List[int]:
            # Simple BFS/DFS to find the path and collect all edge weights
            # Returns a list of weights on the path u -> v.
            queue = [(u, -1, [])] # (current, parent, path_weights)
            visited = {u}
            
            while queue:
                curr, parent, path_weights = queue.pop(0) # BFS
                
                if curr == v:
                    return path_weights
                
                for neighbor, weight in adj[curr]:
                    if neighbor != parent:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            new_path_weights = path_weights + [weight]
                            queue.append((neighbor, curr, new_path_weights))
            
            return [] # Should not happen

        # 3. FIND SECOND BEST MST
        second_mst_weight = math.inf
            
        for u, v, w_prime in non_mst_edges:
            # Get all edge weights on the unique MST path between u and v
            path_weights = getAllPathEdgeWeights(u, v, mst_adj)
            
            # Iterate through all possible edges on the path for replacement
            for w_remove in path_weights:
                # The key condition: the new tree weight must be STRICTLY GREATER than MST weight.
                # This is equivalent to checking: w_prime > w_remove
                if w_prime > w_remove:
                    candidate_weight = mst_weight - w_remove + w_prime
                    second_mst_weight = min(second_mst_weight, candidate_weight)

        # Final result check
        if second_mst_weight == math.inf:
            return -1
        else:
            # We cast to int as the problem deals with integer weights
            return int(second_mst_weight)
