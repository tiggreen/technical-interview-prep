#@tiggreen
class Node:
	__slots__ = ('data', 'next')
	
class LinkedList:
	__slots__ = ('head')
	
class Stack:
	__slots__ = ('head')

def pop(st):
	if st.head is None:
		return None
	dt = st.head.data
	st.head  = st.head.next
	return dt 

def push(st, data):
	if st.head is None:
		st.head = createNode(data, None)
		return st
	st.head = createNode(data, st.head)
	return st

def printStack(st):
	if st.head is None:
		return None
		
	temp = st.head
	while temp is not None:
		print(temp.data)
		temp = temp.next
	
	
	
def createNode(d, n):
	nd = Node()
	nd.data = d
	nd.next = n
	return nd

def createLinkedList():
	ll = LinkedList()
	ll.head = None
	return ll
	
def createStack():
	st = Stack()
	st.head = None
	return st

def addNode(lst, nodeData):
	if lst.head is None:
		lst.head = createNode(nodeData,None)
		return lst
	hd = lst.head
	while hd.next is not None:
		hd = hd.next
	hd.next = createNode(nodeData, None)
	return hd
	

def printList(lst):
	if lst is None:
		print("The list is empty.")
	while lst.head is not None:
		print(lst.head.data)
		lst.head = lst.head.next
	
"""	
Check if two link lists converge together. 
If yes, return the interection Node.
"""  
def ifListsConverged(head1, head2):
	if head1 is None or head2 is None:
		return False
	
	p1 = head1
	p2 = head2
	# O(m*n)
	while p1 is not None:
		p2 = head2
		while p2 is not None:
			if p1.data == p2.data:
				return (p1.data)
			p2 = p2.next
		p1 = p1.next
	
	return False
	
"""
Let's implement a queue with two stacks. We'll make dequeue 
operation costly, to be 0(n) and enqueue O(1).
"""
class Queue:
	__slots__ = ('stack1', 'stack2')
	
def createQueue():
	qu = Queue()
	qu.stack1 = createStack()
	qu.stack2 = createStack()
	return qu

# O(1)
def enqueue(qu,data):
	push(qu.stack1, data)
	return qu
# O(n)
def dequeue(qu):
	if qu.stack1 is None and qu.stack2 is None:
		return None
	# if stack2 is empty
	if qu.stack2.head is None:
		while qu.stack1.head is not None:
			popDat = pop(qu.stack1)
			push(qu.stack2, popDat)
		retData = pop(qu.stack2)
		return retData
	# if stack2 is not empty just pop the head and return it.
	return pop(qu.stack2)
	
"""
The end of Queue implementation
"""

def main():
	pass
	

if __name__ == '__main__':
	main()
	
		
	
		 