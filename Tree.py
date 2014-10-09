
class Node:
	def __init__(self, data, left, right, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

class BinaryTree:

	def __init__(self, root):
		self.root = root

	"""
	Write an algorithm to find the 'next' node (i.e., in-order successor)
	of a given node in a binary search tree. You may assume that each
	node has a link to its parent.

	InOrder: left --> root --> right

	"""
	def findNextNode(root):
		pass

def main():
	pass

main()
