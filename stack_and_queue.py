 
 class Node(object):
    """A node class for stack"""

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

class Stack(object):
    """Stack Data Structure"""

    def __init__(self, top=None):
        self.top = top
        self.size = 0

    def push(self, el):
        self.top = Node(el, top)
        self.size  = self.size + 1

    def pop():
        if self.is_empty():
            return None
        curr_top = self.top
        self.top = self.top.next
        return curr_top

    def peek(self):
        if self.top is not None:
            return self.top

    def is_empty():
        return self.size == 0:

if __name__ == "__main__":
    s = Stack()
