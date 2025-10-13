class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getMaxSum(self, root):
        
        # Helper function returns (max_sum_with_root, max_sum_without_root)
        def dfs_solve(node):
            if not node:
                return (0, 0)

            # 1. Recurse for children
            left_I, left_E = dfs_solve(node.left)
            right_I, right_E = dfs_solve(node.right)

            # 2. Calculate I(node) - Max sum INCLUDING the current node
            # If we include the current node, we MUST exclude its children.
            I_node = node.data + left_E + right_E

            # 3. Calculate E(node) - Max sum EXCLUDING the current node
            # If we exclude the current node, its children can be either included or excluded 
            # (we take the max from each child's subtree).
            E_node = max(left_I, left_E) + max(right_I, right_E)
            
            return (I_node, E_node)

        # The result is the maximum of the two possibilities at the root.
        max_with_root, max_without_root = dfs_solve(root)
        
        return max(max_with_root, max_without_root)
