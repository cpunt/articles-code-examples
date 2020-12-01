class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__ (self):
        self.top = None;

    def push (self, data):
        node = Node(data)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop (self):
        if self.top is not None:
            popped = self.top
            self.top = self.top.next
            return popped

class Queue:
    def __init__ (self):
        self.head = None
        self.tail = None

    def push (self, data):
        node = Node(data)

        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def shift (self):
        if self.head is not None:
            self.head = self.head.next

        if self.head is None:
            self.tail = None
