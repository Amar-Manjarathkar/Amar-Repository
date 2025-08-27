'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        new_node = Node(x) # Step 1 - create a new node with 
                           #data to insert at end
        
        if head is None: # Check if list is empty or not 
            return new_node
        
        temp = head # step -3 chnage head to a temp var
        
        while temp.next: # step -4 traverse the list to find the end
            temp = temp.next
        
        temp.next = new_node # step -5 change the temp to new_node 
                            # to insert at end 
        
        return head
