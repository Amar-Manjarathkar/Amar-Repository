'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructTree(self, pre, post):
        # Create a map for O(1) lookup of postorder indices
        self.post_map = {val: i for i, val in enumerate(post)}
        
        # Call the recursive helper function with initial indices
        # Preorder range: 0 to n-1
        # Postorder range: 0 to n-1
        return self.construct(pre, 0, len(pre) - 1, post, 0, len(post) - 1)

    def construct(self, pre, pre_start, pre_end, post, post_start, post_end):
        # Base Case 1: If the range is invalid, there's no node to create.
        if pre_start > pre_end:
            return None

        # The first element in the preorder traversal is the root of the current subtree.
        root = Node(pre[pre_start])
        
        # Base Case 2: If there's only one element, it's a leaf node. Return it.
        if pre_start == pre_end:
            return root

        # The next element in the preorder sequence is the root of the left subtree.
        left_subtree_root_val = pre[pre_start + 1]
        
        # Find the index of the left subtree's root in the postorder traversal.
        # This tells us where the left subtree's postorder sequence ends.
        left_subtree_post_end_idx = self.post_map[left_subtree_root_val]
        
        # Calculate the number of nodes in the left subtree.
        num_nodes_in_left = left_subtree_post_end_idx - post_start + 1

        # Recursively build the left subtree
        root.left = self.construct(
            pre, 
            pre_start + 1,                          # Preorder for left starts after the root
            pre_start + num_nodes_in_left,          # and ends after all its nodes
            post, 
            post_start,                             # Postorder for left starts at the beginning
            left_subtree_post_end_idx               # and ends at its root's index
        )

        # Recursively build the right subtree
        root.right = self.construct(
            pre,
            pre_start + num_nodes_in_left + 1,      # Preorder for right starts after the left subtree
            pre_end,                                # and goes to the end
            post,
            left_subtree_post_end_idx + 1,          # Postorder for right starts after the left subtree
            post_end - 1                            # and ends just before the main root
        )

        return root
