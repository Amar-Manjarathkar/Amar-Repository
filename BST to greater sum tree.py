'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root: Node) -> Node:
        """
        Transforms the BST into a greater sum tree.
        Each node's value is replaced with the sum of all node values greater than it.
        """
        # A variable to track the cumulative sum of nodes visited so far.
        current_sum = 0

        def reverse_inorder_traversal(node: Node):
            """
            Traverses the tree in Right -> Root -> Left order to visit nodes
            in descending value, updating them along the way.
            """
            nonlocal current_sum
            if not node:
                return

            # 1. Recurse to the rightmost node.
            reverse_inorder_traversal(node.right)

            # 2. Process the current node.
            # Store the original value before it's overwritten.
            original_value = node.data
            
            # The current_sum holds the sum of all nodes greater than this one.
            node.data = current_sum
            
            # Update the sum for the next nodes (which will have smaller values).
            current_sum += original_value

            # 3. Recurse to the left subtree.
            reverse_inorder_traversal(node.left)

        reverse_inorder_traversal(root)
        return root
