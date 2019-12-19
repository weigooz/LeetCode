#Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        current = head
        prev = None
        nextnode = None
        
        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            
            current = nextnode
        
        return prev
