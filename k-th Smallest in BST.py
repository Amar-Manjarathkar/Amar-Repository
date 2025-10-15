'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            
            k -= 1
            if k == 0:
                return node.data
                
            node = node.right
            
        return -1
