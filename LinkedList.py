"""
author @tiggreen 

LinkedList class with its methods.

It's always great to code all data structures from scratch.
We start from LinkedList as it's the most common data structure
to be asked during tech inteviews. 

"""
from Node import *

class LinkedList():
	
	"""
	class variable. Belongs to the class.
	Must be accessed via class name. Or self.__class__.size.
	"""
	
	@classmethod
	def getSize(cls):
		print("The linkedlist has {} nodes.".format(cls.size))
	
	__slots__ = ('head', 'size')
	
	# def __init__(self, head, size):
	# 	head = EmptyNode()
	# 	size = 0
	
def mkLinkedList():
	ll = LinkedList()
	ll.head = mkEmptyNode()
	ll.size = 0
	return ll
	

#append
def append(lst, data):
	#checking if the linkedList is empty. 
	if isinstance(lst.head, EmptyNode):
		lst.head  = mkNode(data, mkEmptyNode())
	else:
		tempHead = lst.head
		while not isinstance(tempHead.next, EmptyNode):
			tempHead = tempHead.next
		tempHead.next = mkNode(data, mkEmptyNode())

#print the linkedlist
def printList(lst):
	curr = lst.head
	while not isinstance(curr, EmptyNode):
		print("{0}".format(curr.data)),
		curr = curr.next
	

#deleteNode. Finds the node with 'data' data and removes it from the list.
def deleteNode(lst, data):
	
def main():
	l = mkLinkedList()
	append(l, 12)
	append(l,22)
	append(l, 33)
	printList(l)

		
main()


