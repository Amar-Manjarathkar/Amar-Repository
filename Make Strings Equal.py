class Solution:
    ALPHABET_SIZE = 26
    INF = float('inf')
    
    def minCost(self, s: str, t: str, transform: list[list[str]], cost: list[int]) -> int:
        def idx(c):
            return ord(c) - ord('a')
        
        # Step 1: Build graph and run Floyd-Warshall
        graph = [[self.INF] * self.ALPHABET_SIZE for _ in range(self.ALPHABET_SIZE)]
        for i in range(self.ALPHABET_SIZE):
            graph[i][i] = 0
        
        for (u_char, v_char), c in zip(transform, cost):
            u, v = idx(u_char), idx(v_char)
            graph[u][v] = min(graph[u][v], c)
        
        # Floyd-Warshall
        for k in range(self.ALPHABET_SIZE):
            for i in range(self.ALPHABET_SIZE):
                for j in range(self.ALPHABET_SIZE):
                    if graph[i][k] < self.INF and graph[k][j] < self.INF:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        # Step 2: Precompute min cost to make any two chars equal
        # min_equal[a][b] = min over k (cost(a→k) + cost(b→k)), or INF if impossible
        min_equal = [[self.INF] * self.ALPHABET_SIZE for _ in range(self.ALPHABET_SIZE)]
        
        for a in range(self.ALPHABET_SIZE):
            for b in range(self.ALPHABET_SIZE):
                for k in range(self.ALPHABET_SIZE):
                    cost_a_k = graph[a][k]
                    cost_b_k = graph[b][k]
                    if cost_a_k < self.INF and cost_b_k < self.INF:
                        min_equal[a][b] = min(min_equal[a][b], cost_a_k + cost_b_k)
        
        # Step 3: Accumulate answer in O(N)
        total = 0
        for c1, c2 in zip(s, t):
            a, b = idx(c1), idx(c2)
            if min_equal[a][b] == self.INF:
                return -1
            total += min_equal[a][b]
        
        return total
