class Node:
	def __init__(self, val=0):
		self.val 	= val
		self.left 	= None
		self.right 	= None


def preorder_traversal(root):
	"""
	if root:
		print(str(root.val) + '->', end='')
		preorder_traversal(root.left)
		preorder_traversal(root.right)
	"""
	res 	= []
	stack 	= [(root, False)]
	while stack:
		node, visited = stack.pop()
		if node:
			if visited:
				res.append(node.val)
			else:
				stack.append((node.right, False))
				stack.append((node.left, False))
				stack.append((node, True))
	return '->'.join(map(str, res))

def inorder_traversal(root):
	"""
	if root:
		inorder_traversal(root.left)
		print(str(root.val) + '->', end='')
		inorder_traversal(root.right)
	"""
	res = []
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
	return '->'.join(map(str, res))
				
def postorder_traversal(root):
	"""
	if root:
		postorder_traversal(root.left)
		postorder_traversal(root.right)
		print(str(root.val) + '->', end='')
	"""
	res 	= []
	stack 	= [(root, False)]
	while stack:
		node, visited = stack.pop()
		if node:
			if visited:
				res.append(node.val)
			else:
				stack.append((node, True))
				stack.append((node.right, False))
				stack.append((node.left, False))
	return '->'.join(map(str, res))

# Longueur maximal d'un binary tree
def max_depth(root):
	""" 
	RECURSIVE
	if not root:
		return 0

	left_depth 	= max_depth(root.left)
	right_depth = max_depth(root.right)

	return max(left_depth, right_depth)+1
	"""
	# Iterative
	stack = [[root, 1]]
	level = max_depth = 0

	while stack and root:
		root, level = stack.pop(0)
		if not root.left and not root.right:
			max_depth = max(max_depth, level)

		if root.left:
			stack.append([root.left, level+1])

		if root.right:
			stack.append([root.right, level+1])

	return max_depth

# check whether it is a mirror of itself
def is_symetric(root):
	stack = [[root.left, root.right]]
	while stack:
		node 		= stack.pop()
		node_left 	= node[0]
		node_right 	= node[1]
		# reach the depth of a tree
		if node_left is None and node_right is None:
			continue

		if None in (node_left, node_right):
			return False

		if node_left.val==node_right.val:
			stack.append([node_left.right, node_right.left])
			stack.append([node_left.left, node_right.right])
		else:
			return False

	return True

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

def merge_trees(root1, root2):
	if None in (root1, root2):
		return root1 or root2
	
	if root1 is None and root2 is None:
		return []

	stack = [[root1, root2]]  

	while stack:

		node1, node2 = stack.pop()

		if not node1 or not node2:
			continue

		node1.val = node1.val+node2.val
		if not node1.left:
			node1.left = node2.left
		else:
			stack.append([node1.left, node2.left])
		if not node1.right:
			node1.right = node2.right
		else:
			stack.append([node1.right, node2.right])

	return root1

def invert_tree(root):
	if root:
		stack = [root]

		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack.extend([node.left, node.right])

	return root

def path_sum(root, target_sum):
	if root:
		stack = [(root, 0)] # [(root, root.val)]
		while stack:
			node, somme = stack.pop()
			if node:
				if node.left is None and node.right is None: # and somme==target_sum return True
					if somme+node.val==target_sum:
						return True

				stack.append((node.left, somme+node.val))  # (node.left, somme+node.left.val)
				stack.append((node.right, somme+node.val)) # (node.right, somme+node.right.val)

	return False

if __name__=='__main__':

	root2 				 = Node(1)
	root2.left 			 = Node(2)
	root2.left.left 	 = Node(4)
	root2.left.left.left = Node(10)
	root2.left.right 	 = Node(5)
	root2.right 		 = Node(3)
	root2.right.left 	 = Node(7)
	root2.right.right 	 = Node(0)
	"""
				 1
			   /   \
			  2     3
			 / \   / \
			4   5 7   0
		   /
		  10
	"""
	root1 				= Node(1)
	root1.left 			= Node(2)
	root1.left.left 	= Node(3)
	root1.left.right 	= Node(4)
	root1.right 		= Node(2)
	root1.right.left 	= Node(4)
	root1.right.right 	= Node(3)
	"""

				1
			  /   \
			 2     2
			/ \   / \
		   3   4 4   3
    """
	# root1 			  = Node(1)
	# root1.left 		  = Node(3)
	# root1.left.left   = Node(5)
	# root1.right 	  = Node(2)

	# root2 			  = Node(2)
	# root2.left 		  = Node(1)
	# root2.left.right  = Node(4)
	# root2.right 	  = Node(3)
	# root2.right.right = Node(7)

	root3 				    = Node(5)
	root3.left 			    = Node(4)
	root3.left.left 	    = Node(11)
	root3.left.left.left    = Node(7)
	root3.left.left.right   = Node(2)
	root3.right 		    = Node(8)
	root3.right.right 	    = Node(4)
	root3.right.right.right = Node(1)
	root3.right.left    	= Node(13)
	
	print("Preorder traversal:")
	print(preorder_traversal(root2))

	print("\nInorder traversal:")
	print(inorder_traversal(root2))

	print("\nPostorder traversal:")
	print(postorder_traversal(root2))

	print("\nMaximum depht:")
	print(max_depth(root2))

	print("\nIs symetric:")
	print(is_symetric(root2))

	print("\nMergre tree:\n", level_order(merge_trees(root1, root2)))

	print("\nInvert tree:\n", level_order(invert_tree(root2)))

	print("\nPath path sum:\n", path_sum(root3, 22))