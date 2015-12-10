 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

class Bucket(object):
    """Hashtable is an array of buckets"""
    def __init__(self, head=None):
        self.head = head
        self.size = 0

class HashTable(object):
    """Hashtable Data Structure"""

    size = 1024
    # each bucket of the hash table is a linked list
    buckets = [Bucket() for i in range(size)]

    # hash the key and return the index of the busket
    def hash(self, key):
        ord_sum = 0
        for s in key:
            ord_sum = ord_sum + ord(s)
        return  ord_sum % self.size


    def search(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket is not None:
            return bucket.head.data
        else:
            return None

    def insert(key):
        pass

    def delete(key):
        pass
