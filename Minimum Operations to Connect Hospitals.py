class Solution:
    def minConnect(self, V: int, edges: list[list[int]]) -> int:
        E = len(edges)

        # 1. Check for Feasibility: Need at least V-1 edges for connectivity.
        if E < V - 1:
            return -1

        # DSU structure setup
        parent = list(range(V))
        num_components = V
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]

        def union(i, j):
            nonlocal num_components
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                parent[root_j] = root_i
                num_components -= 1 # Two components merged into one
                return True
            return False

        # 2. Count Connected Components using DSU
        for u, v in edges:
            union(u, v)

        # 3. Calculate Minimum Operations
        # The number of operations needed to connect C components is C - 1.
        return num_components - 1
