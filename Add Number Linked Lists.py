'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def reverseList(self, head):
        prev = None 
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def trimLeadingZeros(self, head):
        while head and head.data == 0:
            head = head.next
        return head
    def addTwoLists(self, head1, head2):
        # code here
        head1 = self.trimLeadingZeros(head1)
        head2 = self.trimLeadingZeros(head2)
        if not head1 and not head2:
            return Node(0)
        if not head1: return head2
        if not head2: return head1
        
        l1 = self.reverseList(head1)
        l2 = self.reverseList(head2)
        
        dummy = Node(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            curr.next = Node(total % 10)
            
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return self.reverseList(dummy.next)
        
        
