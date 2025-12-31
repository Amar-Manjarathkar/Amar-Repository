class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Compare the first and second halves
        # 'prev' is now the head of the reversed second half
        left, right = head, prev
        is_palin = True
        
        while right: # Only need to compare until the end of the second half
            if left.data != right.data:
                is_palin = False
                break
            left = left.next
            right = right.next
            
        # Step 4 (Optional): Reverse the second half back to restore original list
        # This part is omitted for brevity but follows the same logic as Step 2
            
        return is_palin
        
