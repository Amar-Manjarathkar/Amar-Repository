class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def intersectPoint(self, head1, head2):
        if not head1 or not head2:
            return None
        
        ptr1 = head1
        ptr2 = head2
        
        # Loop until the two pointers meet
        while ptr1 != ptr2:
            # Move ptr1 to head2 if it reaches the end, else move to next node
            ptr1 = ptr1.next if ptr1 else head2
            
            # Move ptr2 to head1 if it reaches the end, else move to next node
            ptr2 = ptr2.next if ptr2 else head1
            
        # Both pointers now point to the intersection node
        return ptr1
