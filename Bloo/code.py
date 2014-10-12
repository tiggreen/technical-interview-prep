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
	
#The end of Queue implementation


"""
Find the longest palindrome in a string.
"""
def isPalindrome(st):
	if st is None:
		return None
	ln = len(st)
	for i in range(ln//2):
		if st[i] != st[ln-i-1]:
			return False
	return True
	
# Finds the longest polindrom in a string. Brute force.
# O(n3) complexity.
def longestPalindrome(st):
	if st is None:
		return None
	
	maxPalindrome = ""
	for i in range(len(st)):
		for j in range(1,len(st)+1):
			if st[i:j] != "":
				if isPalindrome(st[i:j]):
					if len(st[i:j]) > len(maxPalindrome):
						maxPalindrome = st[i:j]
	return maxPalindrome	
	
# We can do this using Dynamic Programming method.
def longestPalindromeDP(st):
	if st is None:
		return None
	ln = len(st)
	table = [[ False for j in range(ln)] for i in range(ln)]
	
	# all substrins length of 1 are palindrome.
	maxLength = 1
	for i in range(ln):
		table[i][i] = True
		
	# check for substring of length 2.
	start  = 0
	for i in range(ln-1):
		if st[i] == st[i+1]:
			table[i][i+1] = True
			start = i
			maxLength = 2
			
	# check for lengths greater than 2. k is length of substring
	for k in range(3,ln+1):
		for i in range(ln-k+1):
			# get the ending index of substring from
			# starting index i and length k
			j = i + k - 1
			
		    # checking for sub-string from i-th index to j-th index 
			# if st[i+1] to str[j-1] is a palindrome
			if table[i+1][j-1] and st[i] == st[j]:
				table[i][j] = True
				if k > maxLength:
					start = i
					maxLength = k
					
	return st[start:start+maxLength]
#End

def main():
	pass
	

if __name__ == '__main__':
	main()
	
		
	
		 