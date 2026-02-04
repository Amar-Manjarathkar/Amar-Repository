class Solution:
    def getLastMoment(self, n, left, right):
        # Time for the furthest ant moving left to reach 0
        max_left = max(left) if left else 0
        
        # Time for the furthest ant moving right to reach n
        # This is n minus the smallest position in the right array
        max_right = (n - min(right)) if right else 0
        
        return max(max_left, max_right)
