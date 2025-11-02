class Solution:
    def maxEdgesToAdd(self, V, edges):
        # code here
        E = len(edges)
        max_possible_edges = (V * (V - 1)) // 2
        return max_possible_edges - E
