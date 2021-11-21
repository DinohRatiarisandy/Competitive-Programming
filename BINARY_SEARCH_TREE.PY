class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val 	= val
		self.left 	= left
		self.right 	= right

def search_bst(root, target):
	"""
	if root:
		node = root
		while node:
			if node.val==target:
				return node
			elif target<node.val:
				node = node.left
			elif target>node.val:
				node = node.right
	return root
	"""
	if root:
		if root.val==target:
			return root
		elif target<root.val:
			return search_bst(root.left, target)
		elif target>root.val:
			return search_bst(root.right, target)

	return root

def inorder_traversal(root):
	res = []
	if root:
		stack = [(root, False)]
		while stack:
			node, visited = stack.pop()
			if node:
				if visited:
					res.append(node.val)
				else:
					stack.append((node.right, False))
					stack.append((node, True))
					stack.append((node.left, False))

	return res

def insert_into_bst(root, target):
	if root:
		if target<root.val:
			if root.left:
				root.left = insert_into_bst(root.left, target)
			else:
				root.left = TreeNode(target)
		else:
			if root.right:
				root.right = insert_into_bst(root.right, target)
			else:
				root.right = TreeNode(target)

	return root if root else TreeNode(target)

def level_order(root):
	order = []
	level = [root]

	while root and level:
		current_node = []
		next_level   = []

		for node in level:
			current_node.append(node.val)
			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)

		order.append(current_node)
		level = next_level

	return order

def is_valid_bst(root):
	# inorder traversal of BST return a sorted array
	out = inorder_traversal(root)
	for i in range(1, len(out)):
		if out[i-1]>=out[i]:
			return False
	return True

def lowest_common_ancestor(root, p, q):
	if max(p.val, q.val)<root.val:
		return lowest_common_ancestor(root.left, p, q)

	elif min(p.val, q.val)>root.val:
		return lowest_common_ancestor(root.right, p, q)

	return root.val

if __name__=="__main__":
	root 			 = TreeNode(5)
	root.left 		 = TreeNode(5)
	root.left.left 	 = TreeNode(2)
	root.left.right  = TreeNode(4)
	root.right 		 = TreeNode(6)
	root.right.right = TreeNode(7)

	root1 			 = TreeNode(1)
	root1.left 		 = TreeNode(1)
	root1.right 	 = TreeNode(3)

	root2			 		= TreeNode(6)
	root2.left 		 		= TreeNode(2)
	root2.left.left  		= TreeNode(0)
	root2.left.right 		= TreeNode(4)
	root2.left.right.left 	= TreeNode(3)
	root2.left.right.right 	= TreeNode(5)
	root2.right 			= TreeNode(8)
	root2.right.right 		= TreeNode(9)
	root2.right.left 		= TreeNode(7)

	# print(traversal(search_bst(root, 5)))

	# print(traversal(insert_into_bst(root, 8)))
	"""
	arr = list(map(int, input().split()))
	root1 = TreeNode(arr[0])
	for val in arr[1:]:
		insert_into_bst(root1, val)
	print(inorder_traversal(root1))
	"""
	p, q = TreeNode(2), TreeNode(8)
	print(lowest_common_ancestor(root2, p, q))