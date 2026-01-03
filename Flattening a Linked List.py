'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''

class Solution:
    def merge(self, a, b):
        # If one list is empty, return the other
        if not a: return b
        if not b: return a
        
        result = None
        
        # Compare data and link using the 'bottom' pointer
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
            
        # Ensure the 'next' pointer is always null in the flattened list
        result.next = None
        return result

    def flatten(self, root):
        # Base case: if list is empty or has only one horizontal node
        if not root or not root.next:
            return root
            
        # Recur for the list on the right
        root.next = self.flatten(root.next)
        
        # Merge the current vertical list with the flattened list on the right
        root = self.merge(root, root.next)
        
        return root
