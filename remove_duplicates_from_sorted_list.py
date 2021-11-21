class ListNode:
	def __init__(self, val=0, next=None):
		self.val  = val
		self.next = next

def show_val(head):
	res = []
	while head:
		res.append(head.val)
		head = head.next
	return '->'.join(map(str, res))

def delete_duplicates(head):
	if head:
		it = sentinel = ListNode(0, head)
		while head:
			if head.next and head.val==head.next.val:
				while head.next and head.val==head.next.val:
					head = head.next
				it.next = head.next
			else:
				it = it.next
			head = head.next
			
	return sentinel.next if head else None

if __name__ == "__main__":

	head = ListNode(1)
	head.next = ListNode(1)
	head.next.next = ListNode(1)
	head.next.next.next = ListNode(2)
	head.next.next.next.next = ListNode(3)
	head.next.next.next.next.next = ListNode(3)
	head.next.next.next.next.next.next = ListNode(5)
	head.next.next.next.next.next.next.next = ListNode(5)
	
	print(show_val(delete_duplicates(ListNode().next)))