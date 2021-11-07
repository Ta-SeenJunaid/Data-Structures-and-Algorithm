
class Node:

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left_child = None
        self.right_child = None


class AVL:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        return self.settle_violation(data, node)

    def settle_violation(self, data, node):

        balance = self.calc_balance(node)

        if balance > 1 and data < node.left_child.data:
            print("Left left heavy situation")
            return self.rotate_right(node)
        if balance < -1 and data > node.right_child.data:
            print("Right right heavy situation")
            return self.rotate_left(node)
        if balance > 1 and data > node.left_child.data:
            print("Left right heavy situation")
            node.left_child = self.rotate_left(node)
            return self.rotate_right(node)
        if balance < -1 and data < node.right_child.data:
            print("Right left heavy situation")
            node.right_child = self.rotate_right(node)
            return self.rotate_left(node)

        return node


    @staticmethod
    def calc_height(self, node):
        if not node:
            return -1

        return node.height

    def calc_balance(self, node):

        if not node:
            return 0

        return self.calc_height(node.left_child) - self.calc_height(node.right_child)

    def rotate_right(self, node):

        new_parent_node = node.left_child
        new_parent_node_previous_right_child = new_parent_node.right_child

        new_parent_node.right_child = node
        node.left_child = new_parent_node_previous_right_child

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        new_parent_node.height = max(self.calc_height(new_parent_node.left_child),
                                     self.calc_height(new_parent_node.right_child)) + 1
        return new_parent_node

    def rotate_left(self, node):

        new_parent_node = node.right_child
        new_parent_node_previous_left_child = new_parent_node.left_child

        new_parent_node.left_child = node
        node.right_child = new_parent_node_previous_left_child

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        new_parent_node.height = max(self.calc_height(new_parent_node.left_child),
                                     self.calc_height(new_parent_node.right_child)) + 1

        return new_parent_node




