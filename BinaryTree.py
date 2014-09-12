# @tigreen

"""
 A class representing a Binary Tree (BT). Max 2 children. 
"""

# A class representing a tree node. 
class TreeNode():
	
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right
		
# A class represeting a binary tree class which consists of TreeNode objects.
class Tree():
	
	def __init__ (self, root, size):
		self.root = root
		self.size = size
	
	def inOrder(self, root, lst):
		if root == None:
			return
		self.inOrder(root.left, lst)
		lst.append(root.data)
		self.inOrder(root.right, lst)
		
	#root -> left -> right
	def preOrder(self,root):
		if root == None:
			return
			
		print(root.data)
		self.preOrder(root.left)
		self.preOrder(root.right)
	
	#left -> right -> current node
	def postOrder(self, root):
		if root == None:
			return
		self.postOrder(root.left)
		self.postOrder(root.right)
		print(root.data)
	
	#find the node that has the given data.
	#BST
	def findNode(self, root, data):
		if root == None:
			return None
		if root.data == data:
			return root.data
		if data < root.data:
			return self.findNode(root.left, data)
		elif data > root.data:
			return self.findNode(root.right, data)
	
	"""
	Delete a node from a binary search tree.
	Case 1: The removed node is a leaf node
	Case 2: The removed node has only one subtree
	Case 3: The removed node has its two subtrees.
	"""
	def deleteNode(self, root, dvalue):
		if root == None:
			return False
			
		if root.data == dvalue:
			# Case 1.
			if root.left == None and root.right == None:
				root = None
				return True
			# Case 2.
			if root.left == None or root.right == None:
				
				if root.left != None:
					tempLeft = root.left
					if tempLeft.isleftChild():
						root.parent.left = tempLeft
					if tempLeft.isrightChild():
						root.parent.right = tempLeft
						
				if root.right != None:
					tempRight = root.right
					if tempRight.isleftChild():
						root.parent.left = tempRight
					if tempRight.isrightChild():
						root.parent.right = tempRight
			# Case 3
			if root.left != None and root.right != None:
				# Some code here
				pass 
					 
			self.deleteNode(root.left, dvalue)
			self.deleteNode(root.right, dvalue)
			
		else:
			return False
	
	# A helper func for deleteNode.
	# In a BST the max node is the right most node. 
	def findMaxNode(self, root):
		if root == None:
			return None
			
		tempRoot = root
		while tempRoot.right != None:
			tempRoot = tempRoot.right
			
		return tempRoot.data
		
		
	
	#creates a new node with the given data and inserts in the tree.
	def insertNodeBST(self, root, data):
		
		if(root == None):
			self.size += 1
			root = TreeNode(data, None, None)
			
		elif data <= root.data:
			root.left = self.insertNodeBST(root.left, data)
		else:
			root.right =  self.insertNodeBST(root.right, data)
			
		return root
		 
	#Balanced if maxDepth - minDepth <= 1	
	def isBalancedTree(self, root):
		
		minDepth = self.minDepth(root)
		maxDepth = self.maxDepth(root)
		if maxDepth - minDepth <= 1:
			return True
		else:
			return False
		
	"""
	Option 1. 
	We can do inOrder traversal and see 
	if the array is sorted. If it is then
	the tree is a BST.
	"""
	
	def isBST(self, root):
		if root == None:
			return True
		lst = []
		self.inOrder(root, lst)
		if sorted(lst) == lst:
			return True
		else:
			return False
	
	"""
	Option 2.
	Recursive approach.
	Condition: Every left node is less than or equal its parent
	and every right node it greater than the parent.
	Any node in the left subtree must be less than any node in the
	right subtree. 
	"""
	def isValidBST(self, root):
		return self.isBSTUtil(root, -1000, 1000)
		
	def isBSTUtil(self, root, mn, mx):
		if root == None:
			return True
			
		return (root.data > mn and root.data <= mx and
			   self.isBSTUtil(root.left, mn,root.data) 
			   and self.isBSTUtil(root.right, root.data, mx))
	
	def maxDepth(self, root):
		if root == None:
			return -1
			
		leftMax = 1 + self.maxDepth(root.left)
		rightMax = 1 + self.maxDepth(root.right)
		
		return max(leftMax, rightMax)
	
	# the miniumum depth of the tree. 
	def minDepth(self, root):
		if root == None:
			return -1
			
		leftMin = 1 + self.minDepth(root.left)
		rightMin = 1 + self.minDepth(root.right)
		
		return min(leftMin, rightMin)
	
	def findLCA(root, data1, data2):
		pass
	


def main():

	root = TreeNode(15,None, None)
	tr = Tree(root,0)
	
	tr.insertNodeBST(tr.root, 10)
	tr.insertNodeBST(tr.root, 20)
	tr.insertNodeBST(tr.root, 7)
	tr.insertNodeBST(tr.root, 11)
	tr.insertNodeBST(tr.root, 25)
	tr.insertNodeBST(tr.root, 19)
	tr.insertNodeBST(tr.root, 40)
	tr.insertNodeBST(tr.root, 50)
	lst = []
	tr.inOrder(tr.root, lst)
	print(lst)
	print(tr.isValidBST(tr.root))

	# tr.preOrder(tr.root)

	#print(tr.minDepth(tr.root))
	#print(tr.isBalancedTree(tr.root))
	# print(tr.findMaxNode(tr.root))

main()