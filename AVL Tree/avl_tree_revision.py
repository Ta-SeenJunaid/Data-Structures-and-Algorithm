
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


