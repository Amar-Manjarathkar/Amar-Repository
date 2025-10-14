"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        # code here
        if root is None:
            return 0
        current_val = root.data
        total_sum = 0 
        if l <= current_val <=r:
            total_sum += current_val
            
            total_sum += self.nodeSum(root.left, l, r)
            total_sum += self.nodeSum(root.right, l, r)
        elif current_val > r:
            total_sum += self.nodeSum(root.left, l, r)
        elif current_val < l:
            total_sum += self.nodeSum(root.right, l, r)
        return total_sum
        
        
