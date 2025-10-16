'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        """
        Removes nodes with values outside the range [l, r] from a BST.

        Args:
            root: The root node of the BST.
            l: The lower bound of the range (inclusive).
            r: The upper bound of the range (inclusive).

        Returns:
            The root of the modified BST.
        """
        
        # Base case: If the tree or subtree is empty, return None.
        if not root:
            return None

        # If the current node's value is too small, the valid nodes
        # can only be in the right subtree.
        if root.data < l:
            return self.removekeys(root.right, l, r)

        # If the current node's value is too large, the valid nodes
        # can only be in the left subtree.
        if root.data > r:
            return self.removekeys(root.left, l, r)

        # If the node's value is within the range, keep the node.
        # Recursively trim the left and right subtrees.
        root.left = self.removekeys(root.left, l, r)
        root.right = self.removekeys(root.right, l, r)
        
        return root
