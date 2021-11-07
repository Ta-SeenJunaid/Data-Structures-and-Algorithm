
class Node:

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left_child = None
        self.right_child = None


class AVL:

    def __init__(self):
        self.root = None

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




