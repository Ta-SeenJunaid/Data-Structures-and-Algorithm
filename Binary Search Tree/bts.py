class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)




    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)


    def getMin(self, node):
         if node.leftChild:
             return self.getMin(node.leftChild)

         return node.data;


    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)


    def getMax(self, node):
         if node.rightChild:
             return self.getMax(node.rightChild)

         return node.data;


    def traverse(self):
        if self.root:
            self.traverseINOrder(self.root)

    def traverseINOrder(self, node):
        if node.leftChild:
            self.traverseINOrder(node.leftChild)

        print("%s " % node.data)

        if node.rightChild:
            self.traverseINOrder(node.rightChild)


bst = BinarySearchTree()
bst.insert(43)
bst.insert(3)
bst.insert(343)
bst.insert(23)
bst.insert(54)
bst.insert(21)
bst.insert(4)
bst.insert(34)

print(bst.getMinValue())
print(bst.getMaxValue())
bst.traverse()
