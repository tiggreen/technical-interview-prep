"""
author @tiggreen 

Node class.
"""


class Node():
    __slots__ = ('data', 'next')

# def __init__(self, data, next):
# """
# 	Note: Doing self.__data = data will make data as private.
# 	"""
# 	self.data = data
# 	self.next = next


class EmptyNode():
    __slots__ = ()


def mkNode(data, next):
    n = Node()
    n.data = data
    n.next = next
    return n


def mkEmptyNode():
    return EmptyNode()