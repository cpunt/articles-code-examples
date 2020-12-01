class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__ (self):
        self.root = None

    def add (self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.addNode(self.root, data)

    def addNode (self, node, data):
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.addNode(node.right, data)
        else:
            if node.left is None:
                node.left = Node(data)
            else:
                self.addNode(node.left, data)

        return True

    def inOrder (node):
        if (node is not None):
            inOrder(node.left)
            print(node.data)
            inOrder(node.right)

    def preOrder (node):
        if (node is not None):
            print(node.data)
            preOrder(node.left)
            preOrder(node.right)

    def postOrder (node):
        if (node is not None):
            postOrder(node.left)
            postOrder(node.right)
            print(node.data)

    def bfs (root):
        queue = Queue()
        queue.put(root)
        node = queue.get()

        while node is not None:
            print(node.data)
            if node.left: queue.put(node.left)
                if node.right: queue.put(node.right)
                    node = None if queue.empty() else queue.get()

bst = BST()
bst.add(20)
bst.add(14)
bst.add(24)
bst.add(15)
bst.add(40)
bst.add(7)

inOrder(bst.root) # 7, 14, 15, 20, 24, 40
preOrder(bst.root) # 20, 14, 7, 15, 24, 40
postOrder(bst.root) # 7, 15, 14, 40, 24, 20
bfs(bst.root) # 20, 14, 24, 7, 15, 40
