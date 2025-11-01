class Solution:
    def findOrder(self, n, prerequisites):
        # code here 
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        for x, y in prerequisites:
            adj[y].append(x)
            in_degree[x] += 1
            
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        order = []
        
        while queue:
            u = queue.popleft()
            order.append(u)
            
            for v in adj[u]:
                in_degree[v] -=1
                if in_degree[v] == 0:
                    queue.append(v)
        if len(order) == n:
            return order
        else:
            return []
        
