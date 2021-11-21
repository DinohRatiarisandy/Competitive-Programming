from sys import stdin
from collections import deque

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


class Node:
	def __init__(self, val=0, left=None, right=None, next=None):
		self.val   = val
		self.left  = left
		self.right = right
		self.next  = next

def traversal(root):
	res = []
	stack = [root]
	while stack:
		node = stack.pop(0)
		if node.left:
			stack.append(node.left)
		while node:
			res.append(node.val)
			node = node.next
		res.append('#')
	return '->'.join(map(str, res))

def connect(root):
	if root:
		queue = deque()
		queue.append(root)
		while queue:
			for i in range(1, len(queue)):
				queue[i-1].next = queue[i]
			queue[-1].next = None
			next_level = deque()
			for node in queue:
				if node.left:
					next_level.append(node.left)
				if node.right:
					next_level.append(node.right)
			queue = next_level
	return root

if __name__ == "__main__":

	root 			 = Node(1)
	root.left 		 = Node(2)
	root.left.left       	 = Node(4)
	root.left.right      	 = Node(5)
	root.right            	 = Node(3)
	root.right.right     	 = Node(7)
	# root2
	root2 			 = Node(1)
	root2.left 		 = Node(2)
	root2.left.left 	 = Node(4)
	root2.left.left.left 	 = Node(10)
	root2.left.right 	 = Node(5)
	root2.right 		 = Node(3)
	root2.right.left 	 = Node(7)
	root2.right.right 	 = Node(0)
	
	print(traversal(connect(root2)))
