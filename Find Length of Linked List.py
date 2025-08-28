'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        return count
