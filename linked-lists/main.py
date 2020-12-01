class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.listLen = 0

    def addToTail(self, data):
        self.listLen += 1
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

        return True

    def addToHead(self, data):
        self.listLen += 1
        node = Node(data)
        if self.head is not None:
            node.next = self.head
        else:
            self.tail = node

        self.head = node
        return True

    def addToIndex(self, data, index):
        if index < 0 or index > self.listLen:
            return False

        if index == 0:
            return self.addToHead(data)

        if index == self.listLen:
            return self.addToTail(data)

        self.listLen += 1
        node = Node(data)
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.next

        node.next = currentNode.next
        currentNode.next = node
        return True

    def removeTail(self):
        node = self.head

        if node is None:
            return False

        self.listLen -= 1

        if node.next is None:
            self.head = None
            self.tail = None
            return True

        while node.next.next is not None:
            node = node.next

        self.tail = node
        node.next = None
        return True

    def removeHead(self):
        if self.head is None:
            return False

        self.listLen -= 1
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return True

    def removeIndex(self, index):
        if index < 0 or index > self.listLen:
            return False

        if index == 0:
            return self.removeHead()

        if index == self.listLen:
            return self.removeTail()

        node = self.head
        for i in range(index-1):
            node = node.next

        node.next = node.next.next
        return True

    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.next

        return None

list = LinkedList()
list.addToTail('1')
list.addToTail('2')
list.addToTail('3')
list.addToHead('4')
list.addToIndex('5', 3)
list.removeTail()
list.removeHead()
list.removeIndex(3)
