class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)

        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)

        return node.data

    def in_order_traverse(self):
        if self.root:
            self.in_order_traverse_helper(self.root)

    def in_order_traverse_helper(self, node):
        if node.left_child:
            self.in_order_traverse_helper(node.left_child)

        print(node.data)

        if node.right_child:
            self.in_order_traverse_helper(node.right_child)

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):

        # Not sure, might be unnecessary
        if not node:
            return node

        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print("Removing a leaf node.")
                del node
                return None
            if not node.left_child:
                print("Removing a node with only right child.")
                temp_node = node.right_child
                del node
                return temp_node
            elif not node.right_child:
                print("Removing a node with only left child")
                temp_node = node.left_child
                del node
                return temp_node

            print("Removing node with 2 children")
            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data, node.left_child)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(14)
bst.insert(16)
bst.insert(4)
bst.insert(6)
bst.insert(7)
bst.insert(2)

bst.in_order_traverse()
print("Minimum value: ", bst.get_min_value())
print("Maximum value: ", bst.get_max_value())
bst.remove(14)
bst.remove(4)
bst.remove(6)
bst.in_order_traverse()
bst.remove(10)
bst.in_order_traverse()
