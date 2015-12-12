#@tiggreen
class Node:
    __slots__ = ('data', 'next')

class DNode:
    __slots__ = ('data', 'next', 'previous')

class TreeNode:
    __slots__ =  ('data', 'left', 'right')
    
class LinkedList:
    __slots__ = ('head')
    
class Stack:
    __slots__ = ('head')
    
class BTree:
    __slots__ = ('root')


def pop(st):
    if st.head is None:
        return None
    dt = st.head
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

def createDNode(d, n, p):
    nd = DNode()
    nd.data = d
    nd.next = n
    nd.previous = p
    return nd
    
def createTreeNode(d, l, r):
    nd = TreeNode()
    nd.data = d
    nd.left = l
    nd.right = r
    return nd

def createLinkedList():
    ll = LinkedList()
    ll.head = None
    return ll
    
def createStack():
    st = Stack()
    st.head = None
    return st
    
def createBinaryTree():
    bt = BTree()
    bt.root = None
    return bt

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
        p2 = head2.next
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
    __slots__ = ('stack1', 'stack2', 'size')
    
def createQueue():
    qu = Queue()
    qu.stack1 = createStack()
    qu.stack2 = createStack()
    qu.size = 0
    return qu

# O(1)
def enqueue(qu,data):
    push(qu.stack1, data)
    qu.size+=1
    return qu
# O(n)
def dequeue(qu):
    if qu.stack1 is None and qu.stack2 is None:
        return None
    qu.size-=1
    # if stack2 is empty
    if qu.stack2.head is None:
        while qu.stack1.head is not None:
            popDat = pop(qu.stack1)
            push(qu.stack2, popDat.data)
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

"""
Find a local minimum in a given array for a given interval.
We can solve this problem in a linear time but let's try to 
improve our time performance.
O(log(n))
"""
def findLocalMinimum(arr, start, end):
    if (end != start + 1):
        middle = (start + end) // 2
        print(arr[middle])
        if ifLocalMinimum(arr, middle):
            return arr[middle]
        elif arr[middle] <= arr[middle-1]:
            # go to the right side
            return findLocalMinimum(arr, middle, end)
            # go to the left side and try to find the local minium there
        else:
            return findLocalMinimum(arr, start, middle)
    else:
        return False
        
def ifLocalMinimum(arr, ind):
    return arr[ind] <= arr[ind-1] and arr[ind] <= arr[ind+1]    
#end

"""
Print a givem matrix in spiral order.
""" 
def printMatrixSpiral(mx):
    pass
# end

"""
Reverse the digits of the integer
12345 -> 54321
"""
def reverseDigits(num):
    multiple = 1
    revNum = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        revNum = revNum*10 + digit
        
    return revNum
# end

"""
Delete a node from a doubly linkedList.
"""
def removeDNode(lst, rdata):
    if not lst:
        return None
    if lst.head.data == rdata:
        lst.head = lst.head.next
        lst.head.previous = None
        return lst
    hd = lst.head.next
    while hd is not None:
        if hd.data == rdata:
            hd.previous.next = hd.next
            hd.next.previous = hd.previous
        hd = hd.next
    return hd
        
#end
"""
Delete a node from a doubly linkedList.
"""
def addDNode(lst, ndata):
    if lst.head is None:
        lst.head = createDNode(ndata, None, None)
        return lst
    hd = lst.head
    while hd.next is not None:
        hd = hd.next
    hd.next = createDNode(ndata, None, hd)
    return hd
        
#end

"""
Remove duplicates from a singly linkedList.
Note: Preferably not using additional memory. 
"""
def removeDuplicatesInPlace(lst):
    if lst is None:
        return None

    prev = lst.head
    curr = prev.next
    while curr is not None:
        runner = lst.head
        while runner != curr:
            if runner.data == curr.data:
                tmp  = curr.next
                prev.next = tmp
                curr = tmp
                break
            runner = runner.next
        
        if runner == curr:
            prev = curr
            curr = curr.next

    return lst
#end

"""
Print nodes in a binary tree in level order.
"""
def addNodeBST(root, data):
    if root is None:
        root = createTreeNode(data, None, None)
    elif data <= root.data:
        root.left = addNodeBST(root.left, data)
    else:
        root.right = addNodeBST(root.right, data)
    return root
    
def printLevelOrder(root):
    if root is None:
        return None
    qu = []
    qu.append(root)
    while len(qu) > 0:
        r = qu.pop(0)
        print(r.data)
        if r.left is not None:
            qu.append(r.left)
        if r.right is not None:
            qu.append(r.right)
#end

"""
Implement integer square root calculation.
"""

def squareRoot(n):
    x = n
    y = 1
    e = 0.000001; #e decides the accuracy level
    while x - y > e:
        x = (x + y) / 2
        y = n / x
    
    return x
#end

""""
Given a binary tree (not a BST), print the nodes at a given level 
n passed as an input parameter.
"""
def print_level(root, level):
    if root is None:
        return
    if level == 0:
        print(root.data)
        return
    else:
        print_level(root.left, level-1)
        print_level(root.right, level-1)


def all_permutations(st):
    """
    Find all permutations of the given string.
    """
    if len(st) == 1:
        return st
    perms = []
    for i in range(len(st)):
        temp = st[:i] + st[i+1:]
        pms = all_permutations(temp)
        for j in pms:
            perms.append(st[i] + j)
    return perms


def power_set(s):
    if not s:
        return [[]]

    first = s[0]
    tail = s[1:]
    tail_power_set = power_set(tail)

    return tail_power_set + [w + [first] for w in tail_power_set]

def josephusProblem(n,k):
    p, i, seq = list(range(n)), 0, []
    while p:
        # getting the index to kill.
        i = (i+k-1) % len(p)
        seq.append(p.pop(i))
    return 'Prisoner killing order: %s. Survivor: %i' % (', '.join(str(i) for i in seq[:-1]), seq[-1])


def main():
    print(power_set(["a", "b", "c"]))
    print(all_permutations("abc"))

if __name__ == '__main__':
    main()
