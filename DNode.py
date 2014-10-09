"""
author @tiggreen

Node class for Doubly linled list.
"""


class DNode():
    __slots__ = ('data', 'next', 'prev')


def mkDNode(data, next, prev):
    n = DNode()
    n.data = data
    n.next = next
    n.prev = prev
    return n
