# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lenght(self, head):
        data = 0
        while head.next is not None:
            data += 1
            head = head.next
        return data
    
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return ListNode().next
        
        length_head = self.lenght(head)        
        first = head
        second = first.next
        i = 0
        
        while second is not None and i<length_head :
            while second is not None and second.val==val:
                second = second.next
            if second is None:
                first.next = None
                second = first
            else:
                first.next = second
                    
            first = second
            second = first.next
            i += 1
        
        if head.val==val:
            head = head.next
            
        return head