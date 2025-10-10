class Solution:
    def zigZagTraversal(self, root):
        if not root:
            return []
        
        # Initialize result list and queue
        result = []
        queue = [root]
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.pop(0)  # Dequeue the front node
                current_level.append(node.data)  # Add node value to current level
                
                # Add children to queue (left then right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add current level to result, reversing if right-to-left
            if not left_to_right:
                current_level.reverse()
            result.extend(current_level)
            
            # Toggle direction for the next level
            left_to_right = not left_to_right
        
        return result
