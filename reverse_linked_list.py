# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_Someone(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_node = prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev # or directly return prev
        return head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements_in_head = []
        while head is not None:
            elements_in_head.append(head.val)
            head = head.next
        it = reversed_list = ListNode()
        while elements_in_head:
            head_tmp = ListNode(elements_in_head.pop())
            it.next = head_tmp
            it = it.next
        return reversed_list.next