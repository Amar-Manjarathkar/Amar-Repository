class Solution:
    def andInRange(self, l: int, r: int) -> int:
        """
        Calculates the bitwise AND of all numbers in the range [l, r], inclusive.
        The result is the common binary prefix of l and r, padded with zeros.
        """
        if l == r:
            return l

        # 'shift' counts how many bits were shifted/removed from the right.
        shift = 0
        
        # Right shift l and r until they are equal.
        # This removes all the differing bits from the right, leaving the common prefix.
        while l != r:
            l >>= 1
            r >>= 1
            shift += 1
            
        # Once l == r, this value is the common prefix.
        # Shift it back to the left by the counted number of positions 
        # (which were the differing bits that must be 0 in the final result).
        return l << shift
