"""
author @tiggreen 

Hashtable implementation.
"""
# [[] for i in range(size)] craetes array of arrays
class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hashtable():
    # number of entries in the hashtable.
    entries = 0
    # the size of the hash table.
    size = 0
    # hashtable is a list of entry lists.
    hashtable = []

    def __init__(self, size):
        self.size = size
        self.hashtable = [[] for i in range(size)]

    """
    Probably this is the worst possible hash function ever.
    Think about a better hash function to avoid many collisions.
    """

    def str2Int(self, st):
        sm = 0
        for s in st:
            sm += ord(s)
        return sm

    def hashf(self, key):
        v = self.str2Int(key)
        return v % self.size

    """
    Returns the value of the entry with the given key.
    If the value is not in the hashtable then returns False.
    """

    def get(self, key):
        bucketId = self.hashf(key)
        # this returns a list of entries.
        entryList = self.hashtable[bucketId]
        for e in entryList:
            if e.key == key:
                return e.value
        return False


    """
    We want to create an entry object and store it in the hashtable.
    """

    def put(self, key, value):
        entry = Entry(key, value)
        bucketId = self.hashf(key)
        entryList = self.hashtable[bucketId]
        entryList.append(entry)

    """
    Searches to find the value with the given key. It could be a list of values.
    if it doesn't exist it returns False, otherwise it returns the
    value.
    """

    def search(self, key):

        bucketId = self.hashf(key)
        result = []

        if self.hashtable[bucketId] != []:
            entryList = self.hashtable[bucketId]
            for e in entryList:
                result.append(e.value)
            return result
        else:
            return False


def main():
    ht = Hashtable(256)
    ht.put("Tigran", 25)
    ht.put("Tigran", 40)
    ht.put("Ani", 10)
    # print(ht.get("Tigran"))
    print(ht.search("Tigran"))

#print(ht.hashtable)

main()