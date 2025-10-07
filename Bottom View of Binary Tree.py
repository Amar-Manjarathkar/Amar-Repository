# User function Template for python3
from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        # Map to store horizontal distance → node value
        hd_map = {}
        
        # Queue for level order traversal (node, horizontal_distance)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            
            # Update the map with the latest node at each horizontal distance
            hd_map[hd] = node.data
            
            # Traverse left child with hd - 1
            if node.left:
                q.append((node.left, hd - 1))
            
            # Traverse right child with hd + 1
            if node.right:
                q.append((node.right, hd + 1))
        
        # Extract the values in order of increasing horizontal distance
        return [hd_map[hd] for hd in sorted(hd_map.keys())]
