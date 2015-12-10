# author @tiggreen

# Single LinkedList class with its methods.

# It's always great to code all data structures from scratch.
# We start from LinkedList as it's the most common data structure
# to be asked during tech inteviews. 

 class Node(object):
    """A Node class"""

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


class LinkedList():
    """
    class variable. Belongs to the class.
    Must be accessed via class name. Or self.__class__.size.
    """

    def __init__(self, head):
        self.head = head
        self.size = 0

    @classmethod
    def size(cls):
        print("The linkedlist has {} nodes.".format(cls.size))


# append
def append(lst, data):
    #checking if the linkedList is empty.
    if isinstance(lst.head, EmptyNode):
        lst.head = mkNode(data, mkEmptyNode())
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
        curr.next = n
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
            append(res, curr.data)
        curr = curr.next
    return res

#1 -> 2 -> 2-> 3 -> 2 -> 5 => 1 -> 2 -> 3 -> 2 -> 5
def remove_duplcates_inplace(lst):
	
	if isinstance(lst.head, EmptyNode):
		return lst
		
	prev = lst.head
	curr = prev.next
	
	while not isinstance(curr, EmptyNode):
		runner = lst.head
		while runner != curr:
			if runner.data == curr.data:
				tmp  = curr.next
				prev.next = tmp
				curr = tmp
				break	
			runner = runner.next	
		#current not updated
		if runner == curr:
			prev = curr
			curr = curr.next	
	return lst
		

#1 -> 2 -> 2-> 3 -> 2 -> 5 => 1 -> 2 -> 3 -> 2 -> 5
def remove_duplcates_inplace(lst):
	if lst is None:
		return None

	prev = lst.head
	curr = prev.next

	while curr is not None:
		while curr.data == prev.data:
			curr = curr.next
		prev = curr.next
		curr = curr.next

	return lst

def delete(head, position):
    # corner case
    if position == 0 and head is not None:
        return head.next

    curr_index = 0
    curr = head
    while curr_index != position - 1:
        head = head.next
        curr_index = curr_index + 1

    head.next = head.next.next
    return curr

def reverse(head):
    if head is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head

def compare_lists(headA, headB):
    if size(headA) != size(headB):
        return 0
    while headA is not None and headB is not None:
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    return 1

def size(head):
    if head is None:
        return 0
    size = 0
    while head is not None:
        size = size + 1
        head = head.next

    return size

def return_kth_to_last_node(head, k):
    if head is None:
        return None

    p1 = head
    p2 = head
    cnt = 1
    while p1 is not None:
        p1 = p1.next
        cnt = cnt + 1
        if cnt >= k:
            p2 = p2.next

    return p2

# m->a->d->a->m
def is_palindrome(head):
    if head is None:
        return None

    fast = head
    slow = head
    while fast.next is not None
        fast = fast.next.next
        slow = slow.next

    # at this point slow is in the middle
    # and fast is on the last node
    runner = head
    while slow is not None:
        if runner.data == slow.data:
            slow = slow.next
            runner = runner.next
        else:
            return False



