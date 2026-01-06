"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def _helper(self,node):
        curr = node
        temp = curr.next
        if curr.child:
            pass

    def flatten(self, head):
        if not head:
            return None
        curr = head
        pass


        