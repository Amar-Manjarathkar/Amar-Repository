from collections import defaultdict, deque

class Solution:
    def safeNodes(self, V, edges):
        # Build adjacency list from edge list input
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)

        # Reverse graph + outdegree logic
        rev_graph = defaultdict(list)
        outdegree = [0] * V
        
        for u in range(V):
            for v in graph[u]:
                rev_graph[v].append(u)
                outdegree[u] += 1
        
        q = deque()
        for i in range(V):
            if outdegree[i] == 0:
                q.append(i)
        
        safe = [False] * V
        while q:
            node = q.popleft()
            safe[node] = True
            for prev in rev_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    q.append(prev)
        
        return [i for i in range(V) if safe[i]]
