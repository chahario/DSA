"""
Docstring for DoubleLL.L146

design a data structure that implement the Least recently used .
implement the LRUCache class:
all operation in O(1)
Use LRU and MRU sentials- (senitals are dummy nodes , that doesnot store any data.. used to keep the track of sart and end of LL)
"""


class LRUCache:
    class Node:
        def __init__(self, key , value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):# assume capacity > 2:
        self.capacity = capacity
        self.cache = {}
        self.l, self.r = self.Node(0,0), self.Node(0,0)
        self.l.next = self.r
        self.r.prev = self.l
    # here two functionality required 
    # one is to remove the node
    # and other one is add the node at the MRU (last)
    def _remove(self,node):
        p,n = node.prev, node.next
        p.next = n 
        n.prev = p
    def _addMRU(self,node):
        p = self.r.prev
        p.next = node
        node.next = self.r
        self.r.prev = node
    def get(self,key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._addMRU(node)
        return node.val
    def put(self,key,value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._addMRU(node)
            return
        node = self.Node(key,value)
        self.cache[key] = node
        self._addMRU(node)
        if len(self.cache) > self.capacity:
            lru = self.l.next
            self._remove(lru)
            del self.cache[lru.key]






