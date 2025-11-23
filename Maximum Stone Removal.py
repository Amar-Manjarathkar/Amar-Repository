class Solution:
    def maxRemove(self, stones):
        # Total number of stones
        N = len(stones)
        
        # --- Disjoint Set Union (DSU) Structure ---
        # The parent dictionary stores the parent of each element.
        # Key: a coordinate (row or column)
        # Value: the parent coordinate/representative
        parent = {}
        
        # Helper to represent a column coordinate uniquely in the DSU
        # We assume max row/col is less than 10000.
        # R rows are [0, 10000], C columns are [10001, 20001]
        def col_to_int(y):
            return y + 10001
        
        # The 'find' operation with Path Compression
        def find(i):
            if i not in parent:
                # If i is not in the set, it's its own parent initially
                parent[i] = i
                return i
            
            # Path compression: make every node on the path point directly to the root
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        # The 'union' operation
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                # Union by merging root_j's set into root_i's set
                parent[root_j] = root_i
                return True # A union happened
            return False # Already in the same set

        # --- Union all stones ---
        # Iterate over all stones and perform union between the stone's row and column.
        for r, c in stones:
            # Union the stone's row 'r' with its column 'c_i'
            # Any two stones that share a row 'r' will be connected to 'r'.
            # Any two stones that share a column 'c' will be connected to 'c_i'.
            # Therefore, all stones that are connected directly or transitively
            # will end up in the same component, represented by a single root.
            union(r, col_to_int(c))
            
        # --- Count the number of connected components (C) ---
        # A connected component is represented by its single root element.
        # We only need to count the roots that are actually part of a stone connection.
        
        # The set of unique root representatives
        unique_roots = set()
        
        # The roots correspond to the actual components.
        # For each stone, the row coordinate (r) will be its representative.
        for r, c in stones:
            # Find the root of the row coordinate for this stone
            root = find(r) 
            unique_roots.add(root)
            
        # The number of connected components is the size of the set of unique roots
        C = len(unique_roots)
        
        # The maximum number of removable stones is N - C
        # where N is the total number of stones and C is the number of components.
        return N - C
