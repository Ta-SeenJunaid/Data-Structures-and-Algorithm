

class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None


class AVL(object):

    def __init__(self):
        self.root = None

    def calcHeight(self, node):
        if not node:
            return -1

        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rotateRight(self, node):

        print("Rotating to the right on node  ", node.data)
        newRoot = node.leftChild
        oldRootLeftChild = newRoot.rightChild

        newRoot.rightChild = node
        node.leftChild = oldRootLeftChild

        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1
        newRoot.height = max(self.calcHeight(newRoot.leftChild), self.calcHeight(newRoot.rightChild)) + 1

        return newRoot

    def rotateLeft(self, node):

        print("Rotating to the left on node ", node.data)

        newRoot = node.rightChild
        oldRootRightChild = newRoot.leftchild

        newRoot.leftchild = node
        node.rightChild = oldRootRightChild

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        newRoot.height = max(self.calcHeight(newRoot.leftChild), self.calcHeight(newRoot.rightChild)) + 1

        return newRoot
