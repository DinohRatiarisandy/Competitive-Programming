from sys import stdin

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val   = val
		self.left  = left
		self.right = right

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())

def is_subtree(root, sub_root):
	stack = [root]
	while stack:
		node = stack.pop()
		if node:
			if node.val==sub_root.val:
				stack2 = [(node, sub_root)]
				# print(node.val, sub_root.val)
				valid = True
				while stack2:
					node1, node2 = stack2.pop()
					# print(node1.val, node2.val)
					if node1.val==node2.val:
						if node1.left and node2.left:
							stack2.append((node1.left, node2.left))

						if node1.right and node2.right:
							stack2.append((node1.right, node2.right))

						if node1.left is None and node2.left is not None or\
						node2.left is None and node1.left is not None:
							# dp.append(False)
							valid = False
							break

						if node1.right is None and node2.right is not None or\
						node2.right is None and node1.right is not None:
							# dp.append(False)
							valid = False
							break
					else:
						# dp.append(False)
						valid = False
						break
				# print(dp)
				if valid:
					return True
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
	return False

if __name__ == "__main__":
	# root1 				 = TreeNode(1)
	# root1.left 			 = TreeNode(2)
	# root1.left.left 	 = TreeNode(4)
	# root1.left.left.left = TreeNode(10)
	# root1.left.right 	 = TreeNode(5)
	# root1.right 		 = TreeNode(3)
	# root1.right.left 	 = TreeNode(7)
	# root1.right.right 	 = TreeNode(0)

	# root2 				 = TreeNode(2)
	# root2.left 			 = TreeNode(4)
	# root2.right 	     = TreeNode(5)
	# root2.left.left		 = TreeNode(10)
	#----------------------------------------
	root1 			 = TreeNode(3)
	root1.left 		 = TreeNode(4)
	root1.left.left  = TreeNode(1)
	root1.left.right = TreeNode(2)
	root1.right 	 = TreeNode(5)

	root2 			 = TreeNode(4)
	root2.left		 = TreeNode(1)
	root2.right 	 = TreeNode(2)
	#----------------------------------------
	# root1 				   = TreeNode(1)
	# root1.left 			   = TreeNode(2)
	# root1.left.left 	   = TreeNode(4)
	# root1.left.right 	   = TreeNode(5)
	# root1.left.left.right  = TreeNode(6)
	# root1.right 		   = TreeNode(3)
	# root1.right.right 	   = TreeNode(6)
	# root1.right.left 	   = TreeNode(2)
	# root1.right.right.left = TreeNode(2)
	# root1.right.left.right = TreeNode(8)
	# root1.right.left.left  = TreeNode(7)

	# root2 				= TreeNode(2)
	# root2.left 			= TreeNode(7)
	# root2.left.right 	= TreeNode(6)
	# root2.right 		= TreeNode(8)

	print(is_subtree(root1, root2))