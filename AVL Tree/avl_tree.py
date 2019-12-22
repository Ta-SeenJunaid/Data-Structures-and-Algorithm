

class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None


class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)

        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)


    def delete(self, data):
        if self.root:
            self.root = self.deleteNode(data, self.root)



    def deleteNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.deleteNode(data, node.leftChild)

        elif data > node.data:
            node.rightChild = self.deleteNode(data, node.rightChild)

        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node")
                del node
                return None

            elif not node.leftChild:
                print("Removing a node with only right child")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                print("Removing a node with only left child")
                tempNode = node.leftChild
                del node
                return tempNode

            else:
                print("Removing a node with both left and right child")
                tempNode = self.getPredecessor(node.leftChild)
                node.data = tempNode.data
                node.leftChild = self.deleteNode(tempNode.data, node.leftChild)

        #if it is an one node tree
        if not node:
            return node

        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        # left left situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)

        # left right situation
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # right right situation
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)

        # right left situation
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node


    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node



    def settleViolation(self, data, node):

        balance = self.calcBalance(node)

        if balance > 1 and data < node.leftChild.data:
            print("Left left situation")
            return self.rotateRight(node)

        if balance < -1 and data > node.rightChild.data:
            print("Right right situation")
            return self.rotateLeft(node)

        if balance > 1 and data > node.leftChild.data:
            print("Left right situation")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightChild.data:
            print("Right left situation")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node


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
        oldRootRightChild = newRoot.leftChild

        newRoot.leftChild = node
        node.rightChild = oldRootRightChild

        node.height = max(self.calcHeight(node.leftChild),self.calcHeight(node.rightChild))+1
        newRoot.height = max(self.calcHeight(newRoot.leftChild), self.calcHeight(newRoot.rightChild)) + 1

        return newRoot

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)


    def traverseInorder(self, node):

        if node.leftChild:
            self.traverseInorder(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverseInorder(node.rightChild)



avl = AVL()

avl.insert(50)
avl.insert(60)
avl.insert(40)
avl.insert(80)
avl.insert(90)
avl.insert(10)
avl.insert(9)
avl.insert(8)
avl.insert(6)
avl.insert(7)
avl.insert(5)
avl.insert(106)
avl.insert(104)
avl.insert(102)
avl.insert(106)

avl.traverse()

avl.delete(6)
avl.delete(90)
avl.delete(104)

avl.traverse()