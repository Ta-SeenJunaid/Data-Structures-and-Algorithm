
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
            self.get_min(self.root)

    def get_min(self, node):
        if node.left_child:
            self.get_min(node.left_child)
        else:
            return node.data

    def get_max_value(self):
        if self.root:
            self.get_max(self.root)

    def get_max(self, node):
        if node.right_child:
            self.get_max(node.right_child)
        else:
            return node.data

    def in_order_traverse(self):
        if self.root:
            self.in_order_traverse_helper(self.root)

    def in_order_traverse_helper(self, node):
        if node.left_child:
            self.in_order_traverse_helper(node.left_child)

        print(node.data, " ")

        if node.right_child:
            self.in_order_traverse_helper(node.right_child)


