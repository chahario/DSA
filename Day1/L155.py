"""
Leetcode 155 . Min Stack

Design a stack that supports, push,pop,top and minimum element in constant time
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.minvalue = []
    def push(self,value):
        self.stack.append(value)
        if self.minvalue and (self.minvalue[-1]<= value):
            self.minvalue.append(self.minvalue[-1])
        else:
            self.minvalue.append(value)
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minvalue.pop()
        print("stack is empty")
    def top(self):
        return self.stack[-1]
    def minelement(self):
        return self.minelement[-1]

    