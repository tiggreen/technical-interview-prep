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
"""
Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
I think we can keep two pointers and do in place removal. O(n2)
"""
#this function uses a temporary buffer.
def removeDuplicates(lst):
	#corner case
	if isinstance(lst.head, EmptyNode):
		return lst 
	curr = lst.head
	d = dict()
	res = mkLinkedList()
	while not isinstance(curr, EmptyNode):
		#hashtable doesn't contain the node data.
		if curr.data not in d.keys():
			d[curr.data] = True
			append(res,curr.data)
		curr = curr.next
	return res
	
def removeNthLast(lst, n):
	pnt1 = lst.head
	pnt2 = lst.head
	currPos = 0
	while not isinstance(pnt1.next, EmptyNode):
		pnt1 = pnt1.next
		currPos += 1
		#please note that this should be >= not ==.
		if currPos >= n:
			pnt2 = pnt2.next
	print("The node that should be removed has a data {}.".format(pnt2.data))
	return lst

def reverseLinkedList(lst):
	if isinstance(lst.head, EmptyNode):
		return lst
		
	curr = lst.head
	prev = mkEmptyNode()
	
	while not isinstance(curr, EmptyNode):
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
	
	lst.head = prev
		
	return lst

			
def main():
	l = mkLinkedList()
	append(l, 5)
	append(l,10)
	append(l,7)
	append(l, 3)
	append(l, 1)

	reverseLinkedList(l)
	printList(l)

#this can be handy when you want to import this module. 
# So in case if you import main won't be imported. 
if __name__ == "__main__":
	main()


