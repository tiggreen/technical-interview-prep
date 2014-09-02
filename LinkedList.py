"""
author @tiggreen 

Single LinkedList class with its methods.

It's always great to code all data structures from scratch.
We start from LinkedList as it's the most common data structure
to be asked during tech inteviews. 

"""
from Node import *
from DNode import *

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
	lst.size += 1 

#print the linkedlist
def printList(lst):
	curr = lst.head
	while not isinstance(curr, EmptyNode):
		print("{0}".format(curr.data)),
		curr = curr.next
	

"""
deleteNode. Finds the node with 'data' data and removes it from the list.
"""
def deleteNode(lst, data):
	curr = lst.head
	
	if curr.data == data:
		lst.size -= 1 
		#moved head
		lst.head = lst.head.next
		return lst
	
	while not isinstance(curr.next, EmptyNode):
		if curr.next.data == data:
			# head didn't change.
			curr.next = curr.next.next
			lst.size -= 1 
			return lst.head
			
		curr = curr.next
		
#Do delete and insert operations for doubly linkedList
"""
There're 2 cases:
1. Deleted node is the head
2. The other case. 

Or 
Insert a node in a give position of a singly linked list. 
def insertAt(lst, data, i)
"""
def insertAt(lst, data, i):
	
	curr = lst.head
	if i < 0 or i > lst.size:
		return lst
	elif i == 0:
		lst.head = mkNode(data, lst.head)
		return lst
	else:
		pos = 0
		while pos != i - 1:
			curr = curr.next
			pos += 1
		temp = curr.next
		curr.next = mkNode(data, temp)
		return lst

#appendAt for a doubly linked List
def appendAt(lst, data, i):
	curr = lst.head
	if i < 0 or i > lst.size:
		return lst
	elif i == 0:
		lst.head = mkDNode(data, lst.head, mkEmptyNode())
		lst.size += 1 
		return lst
	else:
		pos = 0
		while pos != i - 1:
			curr = curr.next
			pos += 1
		temp = curr.next
		n = mkDNode(data, temp, curr)
		curr.next  = n
		if not isinstance(temp, EmptyNode):
			temp.prev = n
		lst.size += 1 
		return lst
		

def main():
	l = mkLinkedList()
	append(l, 12)
	append(l,22)
	append(l,44)
	append(l, 33)
	deleteNode(l,22)
	deleteNode(l,44)
	insertAt(l, 777, 0)
	printList(l)
	print()
	dl = mkLinkedList()
	appendAt(dl, 24, 0)
	appendAt(dl, 55, 1)
	appendAt(dl, 77, 2)
	printList(dl)

#if __name__ == "__main__":		
main()


