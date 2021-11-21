# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, node): # Function to determine the length of node.
        data = 0
        while node is not None:
            data += 1
            node = node.next
        return data
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_head = self.length(head)
        idx_to_delete = len_head - n # index of the node to delete from behind, 0 base index
        # We create 2 pointers.
		first = head # point to the first node
        second = first.next # point to the second node 
        i = 1
        
        if idx_to_delete==0: # if the node to delete is in the front
            return head.next # we just move the head to the next node 
        
        while i < idx_to_delete and second is not None: # we iterate i until idx_to_delete and second not point to end
            first = first.next # we move the pointer
            second = second.next # we move the pointer
            i += 1

        # here we have first point to the node before the node to delete 
        # and second point to the node to delete
        if second is not None: # if the second not point to end (nothing)
            second = second.next # so we move to his next node
        else: # if second point to the end
            first.next = None # we just point first.next to None because that's mean we delete the last node
            second = first.next # we just move second to first
            
        first.next = second # we match first to second
        return head
        